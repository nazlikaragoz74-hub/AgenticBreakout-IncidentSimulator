# Model Kartı: AgenticBreakout Hint Predictor (v2.0)

## Model Detayları
* **Geliştiren:** Nazlı Karagöz (Samsun Üniversitesi Yazılım Mühendisliği)
* **Model Mimari:** Lojistik Regresyon (`scikit-learn -> ONNX`)
* **Sürüm:** v2.0
* **Lisans:** MIT

## Kullanım Amacı (Intended Use)
* **Birincil Kullanım:** AgenticBreakout kriz simülatöründe oyuncunun davranışsal parametrelerine (karar süresi, yanlış sayısı vb.) bakarak dinamik Sokratik ipucu gereksinimini kestirmek.
* **Kapsam Dışı Kullanım:** Genel kullanıcı davranış/psikoloji analizi veya akademik başarı değerlendirmesinde kullanılamaz.

## Eğitim Verisi & Metrikler
* **Veri Seti:** `data/oturumlar.csv` (15 Gerçek + Sentetik Oturum Adımı)
* **Test Doğruluğu (Accuracy):** >= %80.0 (Kabul eşiği geçildi)
* **Hata Toleransı:** ONNX Runtime vs Python parite farkı `< 1e-4`

## Sınırlılıklar
* Model yalnızca 5 temel davranışsal niteliğe dayanarak tahmin yapar. Oyuncunun konu hakkındaki geçmiş bilgi birikimini ölçemez.