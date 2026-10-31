import json
import numpy as np
import onnxruntime as ort

# Referans Girdiler (5 Farklı Senaryo)
reference_inputs = [
    {"seviye": 0, "karar_suresi_sn": 45.0, "onceki_yanlis_sayisi": 2, "ipucu_sayisi": 0, "sahne_no": 2},
    {"seviye": 1, "karar_suresi_sn": 10.0, "onceki_yanlis_sayisi": 0, "ipucu_sayisi": 0, "sahne_no": 1},
    {"seviye": 0, "karar_suresi_sn": 60.0, "onceki_yanlis_sayisi": 1, "ipucu_sayisi": 1, "sahne_no": 3},
    {"seviye": 1, "karar_suresi_sn": 5.0,  "onceki_yanlis_sayisi": 0, "ipucu_sayisi": 2, "sahne_no": 4},
    {"seviye": 0, "karar_suresi_sn": 30.0, "onceki_yanlis_sayisi": 0, "ipucu_sayisi": 0, "sahne_no": 1}
]

# ONNX Modelini Yükle
sess = ort.InferenceSession("model/model.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[1].name

parite_results = []

for inp in reference_inputs:
    x = np.array([[inp["seviye"], inp["karar_suresi_sn"], inp["onceki_yanlis_sayisi"], inp["ipucu_sayisi"], inp["sahne_no"]]], dtype=np.float32)
    prob = float(sess.run([label_name], {input_name: x})[0][0][1])
    parite_results.append({
        "input": inp,
        "oracle_probability": prob
    })

# Çıktıları tests/parite.json Dosyasına Yaz
with open("tests/parite.json", "w", encoding="utf-8") as f:
    json.dump(parite_results, f, indent=2)

print("BAŞARILI: tests/parite.json üretildi!")