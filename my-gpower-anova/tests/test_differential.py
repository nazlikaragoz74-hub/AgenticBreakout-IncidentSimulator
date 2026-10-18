import csv
import subprocess
import json
import os

def test_differential_gpower():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    oracle_file = os.path.join(base_dir, "oracle", "vectors.csv")
    cli_path = os.path.join(base_dir, "src", "cli.py")

    matches = 0
    total = 0

    if not os.path.exists(oracle_file):
        print(f"HATA: {oracle_file} dosyası bulunamadı!")
        return

    with open(oracle_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            cmd = [
                "python", cli_path,
                "--test", row["test"],
                "--mode", row["mode"],
                "--f", row["f"],
                "--alpha", row["alpha"],
                "--power", row["power"],
                "--groups", row["groups"]
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            stdout_str = result.stdout.strip()

            if result.returncode != 0 or not stdout_str:
                print(f"Hata (Satır {total}): CLI boş veya hatalı çıktı verdi!")
                print(f"STDERR: {result.stderr}")
                print(f"STDOUT: {result.stdout}")
                continue
            
            try:
                output = json.loads(stdout_str)
            except json.JSONDecodeError:
                print(f"JSON Parse Hatası (Satır {total}): Gelen metin -> '{stdout_str}'")
                continue
            
            expected_n = int(row["n_total"])
            actual_n = output.get("n_total")
            
            if expected_n == actual_n:
                matches += 1
            else:
                print(f"Uyuşmazlık (Satır {total}): Beklenen N={expected_n}, Bulunan N={actual_n}")

    accuracy = (matches / total) * 100 if total > 0 else 0
    print(f"\n--- DİFERANSİYEL TEST SONUCU ---")
    print(f"Toplam Test: {total} | Tam Eşleşen: {matches} | Uyum Oranı: %{accuracy:.2f}\n")

if __name__ == "__main__":
    test_differential_gpower()