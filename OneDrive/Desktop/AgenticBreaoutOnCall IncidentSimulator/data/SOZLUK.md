# Veri Sözlüğü (Data Dictionary) - `data/oturumlar.csv`

Bu dosya, oyuncuların simülasyondaki davranışsal verilerini ve modelin eğitime alacağı nitelikleri (features) açıklar[cite: 3].

| Sütun Adı | Veri Tipi | Birim / Format | Açıklama |
| :--- | :--- | :--- | :--- |
| `oturum` | String | UUID (8 hane) | Anonim oturum kimliği (KVKK gereği kişisel veri içermez, rastgele üretilir)[cite: 4]. |
| `sahne_no` | Integer | [1 - 5] | Simülasyondaki mevcut kriz sahnesi numarası[cite: 3]. |
| `seviye` | Integer | 0 veya 1 | Oyuncunun seçtiği zorluk (0: Junior, 1: Senior)[cite: 3]. |
| `karar_suresi_sn` | Float | Saniye (sn) | Oyuncunun o sahnede kararı vermeden önce harcadığı süre[cite: 3]. |
| `onceki_yanlis_sayisi` | Integer | Adet | Oyuncunun o ana kadar yaptığı toplam yanlış/kritik karar sayısı[cite: 3]. |
| `ipucu_sayisi` | Integer | Adet | Oyuncunun o ana kadar kullandığı ipucu sayısı[cite: 3]. |
| `ipucu_gerekti` | Integer | 0 veya 1 | **Hedef Etiket (Target):** 1 = Oyuncu zorlandı, Tutor ipucu vermeli[cite: 3]. |
| `kaynak` | String | `gercek` / `sentetik` | Verinin gerçek kullanıcı oturumundan mı yoksa sentetik üreticiden mi geldiği[cite: 4]. |