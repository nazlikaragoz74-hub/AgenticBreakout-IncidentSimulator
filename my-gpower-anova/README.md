# G*Power Teardown: One-Way ANOVA (3 Groups) CLI Clone

Yazılım Gerçekleme ve Test dersi Teardown Sprint kapsamında geliştirilmiş, G*Power 3.1.9.7 One-Way ANOVA ($k=3$) motorunun temiz oda (clean-room) yöntemiyle yazılmış CLI klonudur.

## Sürüm ve Doğrulama Bilgileri
- **Hedef Yazılım:** G*Power 3.1.9.7 (Windows)
- **GPower.exe SHA-256 Hash:** `3b8d1b9508e6047cf36655c65f973307e5f396e98711311099e03d350d75a8a1`
- **Diferansiyel Test Uyum Oranı:** %93.33+ (Kapı şartı olan %90 aşılmıştır)

## Kurulum ve Çalıştırma
```bash
# Bağımlılıkları kurun
pip install scipy pytest

# CLI Kullanım Örneği
python src/cli.py --test anova-oneway --mode a-priori --f 0.25 --alpha 0.05 --power 0.80 --groups 3

# Diferansiyel Testleri Çalıştırma
python tests/test_differential.py