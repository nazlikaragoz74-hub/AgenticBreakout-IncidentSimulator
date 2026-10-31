import os
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as ort

# 1. Sabit Tohum & Ayarlar (Tekrarlanabilirlik)
RANDOM_SEED = 42
EVAL_THRESHOLD = 0.80  # spec.md kabul eşiği (Altın Standart)

np.random.seed(RANDOM_SEED)

# 2. Veri Yükleme
if not os.path.exists("data/oturumlar.csv"):
    raise FileNotFoundError("data/oturumlar.csv bulunamadı! Lütfen önce veriyi ekleyin.")

df = pd.read_csv("data/oturumlar.csv")
features = ["seviye", "karar_suresi_sn", "onceki_yanlis_sayisi", "ipucu_sayisi", "sahne_no"]
X = df[features].astype(np.float32)
y = df["ipucu_gerekti"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_SEED)

# 3. Model Eğitimi (Lojistik Regresyon)
model = LogisticRegression(random_state=RANDOM_SEED)
model.fit(X_train, y_train)

# 4. Değerlendirme & Eval Kapısı (Eşik Altındaysa Durur)
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"[EVAL] Test Accuracy: {acc:.4f} (Kabul Eşiği: {EVAL_THRESHOLD})")

if acc < EVAL_THRESHOLD:
    raise ValueError(f"HATA: Model doğruluğu ({acc:.4f}) kabul eşiğinin ({EVAL_THRESHOLD}) altında kaldı! Artefakt yayınlanmayacak.")

# 5. ONNX Dönüştürme
initial_type = [('input', FloatTensorType([None, len(features)]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

os.makedirs("model", exist_ok=True)
onnx_path = "model/model.onnx"
with open(onnx_path, "wb") as f:
    f.write(onnx_model.SerializeToString())

# 6. Parite Testi Kontrolü (Sklearn vs ONNX < 1e-4)
sess = ort.InferenceSession(onnx_path)
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[1].name  # Olasılık çıktı kanalı

sample_x = X_test.iloc[:5].values
sk_probs = model.predict_proba(sample_x)[:, 1]
ort_probs = sess.run([label_name], {input_name: sample_x})[0]
ort_probs_class1 = [p[1] for p in ort_probs]

max_diff = np.max(np.abs(sk_probs - ort_probs_class1))
print(f"[PARİTE] Sklearn - ONNX Max Fark: {max_diff:.6f}")
assert max_diff < 1e-4, "HATA: ONNX ve Sklearn farkı 1e-4 toleransını aştı!"

# 7. config.json (Sözleşme & Şema) Oluşturma
config = {
    "model_name": "AgenticBreakout-HintPredictor",
    "version": "v2.0",
    "framework": "scikit-learn -> ONNX",
    "features": features,
    "target": "ipucu_gerekti",
    "threshold": 0.50,
    "eval_metrics": {
        "accuracy": float(acc),
        "threshold_passed": True
    },
    "classes": [0, 1]
}

with open("model/config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print("BAŞARILI: model/model.onnx ve model/config.json başarıyla üretildi!")