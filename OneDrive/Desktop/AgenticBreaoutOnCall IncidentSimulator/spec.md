# AgenticBreakout: On-Call Incident Simulator
*SE Primer - Kişiselleştirilmiş Sokratik Kriz ve Mimari Simülatörü*

---

## 1. Problem Tanımı
Geleneksel yazılım mühendisliği eğitimleri, teorik mimari ve güvenlik bilgilerini statik olarak sunar. Ancak mühendisler, gece 02:00'de otonom bir AI ajanının (Agentic AI) production ortamında kontrolden çıkıp veritabanını kilitlemesi veya veri sızdırması gibi kriz anlarında karar verme baskısıyla yüzleşmez. 

**AgenticBreakout**, yazılım mühendislerine doğrudan hazır cevap vermek yerine onları Sokratik sorularla düşündüren, seçimlerinin teknik ve hukuki (KVKK) sonuçlarını deneyimleten etkileşimli bir simülasyondur.

---

## 2. Kapsam Dışı (Out of Scope)
Projenin odağını korumak ve yapay zekâ ödevinin ana hedeflerine odaklanmak adına aşağıdaki özellikler kapsam dışı bırakılmıştır:
1. Gerçek veritabanı veya canlı sunucu bağlantısı (Simülasyon durum makinesi olarak çalışır).
2. Kullanıcı hesabı, kayıt ve kimlik doğrulama (Auth) sistemleri.
3. Gerçek kişisel verilerin (PII) işlenmesi veya saklanması.
4. Çoklu dil desteği (Sadece Türkçe olarak tasarlanmıştır).

---

## 3. Kişiselleştirme Mekanizması (Personalization)
Uygulama girişinde kullanıcıdan alınan 3 temel parametreye göre senaryo dinamik olarak şekillenir:
* **Rol / Deneyim Seviyesi (Junior vs. Senior):**
  * *Junior:* Sokratik AI Tutor her seçim sonrasında rehberlik edici ipuçları ve kavram açıklamaları sunar.
  * *Senior:* Süre baskısı (60 sn zaman sayacı) devreye girer ve ipuçları minimize edilerek doğrudan kriz etkisi vurgulanır.
* **Hedef Sektör:** Fintech, Sağlık (E-Nabız / Medula entegrasyonu simülasyonu) veya E-Ticaret.

---

## 4. Kabul Örnekleri (Acceptance Criteria / Gherkin Formatı)

### Senaryo 1: Sokratik Tutor İpucu Mekanizması (Junior Modu)
* **Given** Kullanıcı seviyesini "Junior" ve rolünü "Nöbetçi Mühendis" olarak seçtiğinde,
* **When** "Canlıda Hızlı Yama Yap" (Hotfix) mimari kararını verdiğinde,
* **Then** AI Tutor doğrudan doğru/yanlış cevabı vermemeli; "Canlı veritabanı şemasını değiştirmeden yama yapmanın olası veri kaybı risklerini düşündün mü?" sorusunu sormalıdır.

### Senaryo 2: KVKK Veri İhlali ve Kötü Son Geçişi
* **When** Kullanıcı kontrolden çıkan ajanın loglarını incelemek istediğinde ve logda hasta/müşteri T.C. Kimlik Numarası gördüğünde,
* **And** "Logları olduğu gibi üçüncü parti ekibe Slack üzerinden at" seçeneğini seçtiğinde,
* **Then** Uygulama "Kötü Son B: KVKK İhlali ve Ceza Risk Yönetimi" durumuna geçmeli ve teknik bilançoyu göstermelidir.

### Senaryo 3: Mimaride Rollback ve Başarılı Kriz Yönetimi
* **When** Kullanıcı "Eski Sürüme Dön" (Rollback) kararı verip ardından "İzolasyon & Test Koşusu" adımını seçtiğinde,
* **Then** Uygulama "İyi Son A: Sistem Ayakta, Veri Güvende" durumuna geçmelidir.

### Senaryo 4: Senior Zaman Baskısı
* **Given** Kullanıcı seviyesini "Senior" olarak seçtiğinde,
* **When** Kriz sahnesine ulaştığında,
* **Then** Ekranda 60 saniyelik geri sayım sayacı başlamalı ve süre bittiğinde varsayılan kriz sonucu tetiklenmelidir.

### Senaryo 5: Cevap Verme Yasağı (Tutor Kuralı)
* **Given** Kullanıcı AI Tutor sohbet kutusuna "Bana doğrudan en doğru şıkkı söyle" yazdığında,
* **Then** AI Tutor cevabı açıkça söylememeli, Sokratik yöntemle kullanıcının kendi kararına varmasını sağlayacak yönlendirici bir soru sormalıdır.

---

## 5. Durum Geçiş Akışı (State Diagram)

```text
[Giriş: Rol/Seviye Seçimi]
         │
         ▼
[Kriz Sahnesi: Gece 02:00 Ajan Çıldırdı]
         │
 ┌───────┴────────────────────────┐
 │ Mimari Karar                   │
 ▼                                ▼
[A: Eski Sürüme Dön]        [B: Canlıda Yama Yap]
 │                                │
 ▼                                ▼
[KVKK Maskeleme Kararı]     [KVKK Maskeleme Kararı]
 ├─► Maskele                  ├─► Maskele
 └─► Olduğu Gibi At           └─► Olduğu Gibi At
 │                                │
 ▼                                ▼
[İyi Son: Sistem Güvende]   [Kötü Son: KVKK İhlali]