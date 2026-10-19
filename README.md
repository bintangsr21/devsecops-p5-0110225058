# Task Manager CLI

## 1. Nama Aplikasi & Fungsi
**Task Manager CLI** adalah aplikasi baris perintah untuk mengelola daftar tugas
(menambah, melihat, menyelesaikan, dan menghapus tugas) dengan data tersimpan
dalam file JSON.

## 2. Bahasa / Framework
- Python 3.11 (hanya standard library)
- `unittest` untuk pengujian
- Bandit untuk analisis keamanan (SAST)

## 3. Cara Menjalankan
```bash
git clone https://github.com/bintangsr21/devsecops-p5-0110225058.git
cd devsecops-p5-0110225058
pip install -r requirements.txt

python main.py add "Belajar DevSecOps" --priority high
python main.py list
python main.py done 1
python main.py remove 1

# Menjalankan unit test
python -m unittest discover -s tests -v
```

## 4. Overview Pipeline CI/CD
Pipeline berada di `.github/workflows/devsecops.yml` dan terpicu pada
**push** dan **pull request** ke branch `main`.

| Job | Fungsi |
|---|---|
| `build` | Install dependencies dan menjalankan unit test |
| `sast-scan` | Menjalankan Bandit (SAST); bergantung pada job `build` (`needs: build`) |

Quality Gate: pipeline gagal bila Bandit menemukan temuan berseverity
**MEDIUM** atau lebih tinggi.