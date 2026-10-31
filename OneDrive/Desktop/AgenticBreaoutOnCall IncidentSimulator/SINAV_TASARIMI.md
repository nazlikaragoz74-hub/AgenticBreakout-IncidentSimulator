# SINAV_TASARIMI.md — Sizinle Uyumlanan Vize Sınavı Tasarımı

## 1. Özgün Vize Sınav Sorusu (Klasik / Senaryo Tabanlı)

> **Senaryo:** Bir savunma sanayii / sağlık yazılımı firmasında Kıdemli Yazılım Mühendisi olarak çalışıyorsunuz. Ekibiniz, sahadaki uç cihazlarda (edge devices / mobil) internet bağlantısı olmadan çalışması gereken ve kullanıcının anlık stres/hata durumuna göre arayüzü basitleştiren dikey bir makine öğrenmesi modelini (`sklearn -> ONNX`) geliştirmekle görevlendirildi. Model istemci tarafında yerel olarak çalıştırılacaktır.

### Soru Maddeleri (Toplam: 100 Puan)

1. **Doğrulama ve Geçerleme (Verification & Validation) [30 Puan]:**
   Bu projedeki *Doğrulama (Verification)* ve *Geçerleme (Validation)* süreçleri arasındaki farkı birer cümleyle açıklayınız[cite: 9]. Hazırladığınız `model.onnx` artefaktı ile tarayıcı arasındaki $< 1e-4$ parite testi hangi kapsama girer[cite: 5, 7]? Gerekçelendiriniz.

2. **ML Yaşam Döngüsü ve 3V (Velocity, Validation, Versioning) [35 Puan]:**
   Üretimdeki model zamanla kullanıcı davranışlarının değişmesiyle (Data Drift / Model Drift) performans kaybettiğinde, Amershi vd. (2019) Amershi-Microsoft ML yaşam döngüsüne uygun olarak **Validation** ve **Versioning** adımlarını nasıl kurgularsınız[cite: 9]? Rollback ve Canary Deployment mekanizmalarınızı mimari akışla açıklayınız.

3. **Diferansiyel Test ve Donanım Toleransı [35 Puan]:**
   Python Oracle (Test Kahini) ile mobil/web `onnxruntime` çıkarımı arasındaki farkı ölçerken tolerans eşiğini neden $0.0$ tam eşitlik yerine $1e-4$ ($10^{-4}$) aldığımızı floating-point (WASM / float32) mimarisi açısından açıklayınız[cite: 5, 7].

---

## 2. Beklenen Temel Kavramlar ve Çeldirici Analizi

### Beklenen Temel Kavramlar (Doğru Cevap Anahtarı)
* **Verification (Ürünü Doğru Yapmak):** Kodun, modelin ve artefaktın teknik gereksinimlere (spec) uygun üretilmesidir. Python `sklearn` ile `model.onnx`'in aynı girdilere $< 1e-4$ farkla aynı çıktıyı vermesi tam bir **Verification** örneğidir[cite: 5, 7, 9].
* **Validation (Doğru Ürünü Yapmak):** Modelin gerçek kullanıcının ihtiyacını karşılayıp karşılamadığıdır[cite: 9]. İpucu verildiğinde kullanıcının kriz anındaki hata oranının düşüp düşmediği **Validation** ile ölçülür[cite: 9].
* **Hata Toleransı ($1e-4$ Eşiği):** Farklı donanım mimarileri (x86 vs ARM) ve derleme ortamları (Python C-extensions vs WebAssembly / WASM) float32 matris çarpımlarında mikroskobik yuvarlama farkları üretir[cite: 5, 7]. Bu yüzden tam eşitlik ($0.0$) aramak hatalı bir test stratejisidir[cite: 5, 7].

### Çeldirici Analizi ve Sık Yapılan Hatalar
* **Çeldirici 1:** *"Modelin test seti doğruluğu %99 çıktığı için sistem doğrulanmıştır (verified)."*
  * **Analiz:** Yanlış. Offline accuracy sadece veri üzerindeki başarımı gösterir; `ONNX` aktarımındaki veri tipi dönüşüm hatalarını veya istemci ortamındaki çıkarım uyuşmazlıklarını garanti etmez[cite: 5, 7].
* **Çeldirici 2:** *"Sistemde hiç hata olmaması için tolerans $0.0$ seçilmelidir."*
  * **Analiz:** Yanlış. IEEE 754 kayan nokta standartlarındaki yuvarlama farklılıkları nedeniyle $0.0$ eşiği yanlış başarısızlık (false positive test failure) üretir[cite: 5, 7].