# RELEASE.md - Dağıtım, Sürüm Yönetimi ve Ödünleşim Matrisi

## 1. Sürüm v2.0 Detayları
* **Hugging Face Model Reposu:** https://huggingface.co/nazl1/agenticbreakout-model
* **Commit'e Sabitlenmiş Doğrudan Model URL'i:**
  `https://huggingface.co/nazl1/agenticbreakout-model/resolve/9c0b87f7c8dd2b205389449134944466e6ce7346/model.onnx`
* **Değişiklik Özeti:** v1'deki sabit kural motoru kaldırılarak davranışsal parametrelere göre karar veren ONNX modeli devreye alındı[cite: 2].

## 2. Geri Alma (Rollback) Planı
Eğer canlı ortamda yeni model hatalı tahminler üretir veya yüksek gecikmeye sebep olursa:
1. Uygulama konfigürasyonundaki `MODEL_URL` adresi bir önceki stabil sürümün commit URL'ine çekilir[cite: 6].
2. İstemci önbelleği temizlenerek önceki model versiyonunun yüklenmesi sağlanır[cite: 6].

## 3. Güvenli Devreye Alma (Deployment) Stratejisi
* **Shadow Deployment (Gölge Dağıtım):** Model arka planda sessizce çalıştırılır[cite: 6]. Tahminleri kaydedilir ancak arayüze yansıtılmaz; v1 kuralları ile karşılaştırılır[cite: 6].
* **Canary Deployment (Kanarya Dağıtımı):** Trafiğin %5'lik kısmına yeni model sunulur[cite: 6]. Hata ve parite metrikleri izlenir[cite: 6].
* **Progressive Rollout (Aşamalı Geçiş):** Performans normalse kitle kademeli olarak %25 -> %50 -> %100 oranında yeni modele aktarılır[cite: 6].

## 4. Mimari Dağıtım Ödünleşim (Trade-off) Matrisi

| Kriter | Tarayıcı İçi (`onnxruntime-web`) | Sunucu Tarafı (Render / API) | Cihaz İçi Mobil (`React Native`) |
| :--- | :--- | :--- | :--- |
| **Ağ & Gecikme (Latency)** | İlk indirme sonrası **0ms gecikme**, offline çalışır[cite: 7]. | Her istekte **50-200ms ağ gecikmesi** oluşur[cite: 7]. | **0ms gecikme**, uygulama boyutu bir miktar artar[cite: 7]. |
| **KVKK & Veri Gizliliği** | **Mükemmel.** Kullanıcı verisi cihaz dışına çıkmaz[cite: 4, 7]. | Veri ağ üzerinden sunucuya taşınır (KVKK riski)[cite: 4, 7]. | **Mükemmel.** Cihaz üzerinde işlenir[cite: 4]. |
| **Model Gizliliği** | **Düşük.** Model istemciye indiği için tersine mühendislik riski var[cite: 7]. | **Yüksek.** Model sunucuda gizli kalır[cite: 7]. | **Orta.** Uygulama paketinden çıkarılabilir. |

> **Seçim Gerekçesi:** Bu projede sıfır ağ gecikmesi ve %100 KVKK uyumu önceliklendirildiği için **Tarayıcı İçi (`onnxruntime-web`)** mimarisi tercih edilmiştir[cite: 4, 7].