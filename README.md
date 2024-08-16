# Trans-Chain-Crawler

Alat Investigasi Transaksi Blockchain dirancang untuk menjelajahi jaringan dompet blockchain dengan merayapi riwayat transaksi secara rekursif. Data ditampilkan sebagai grafik untuk mengungkap sumber utama, penyebab, dan koneksi mencurigakan.

alat ini sangat berguna bagi peneliti, analis blockchain, atau pihak-pihak lain yang ingin memahami lebih dalam mengenai hubungan dan aktivitas dalam jaringan blockchain, termasuk untuk mendeteksi aktivitas mencurigakan atau untuk mendapatkan wawasan tentang dinamika dalam ekosistem blockchain.

**Catatan:**
- Alat ini hanya berjalan pada Python 3.2 dan yang lebih baru.
- Direktory Root

## Installing

**Kolining Repository**

```bash
git clone https://github.com/Yoga913/Trans-Chain-Crawler.git
```
**Masuk Direktory Unduhan**

```bash
cd Trans-Chain-Crawler
```

## Penggunaan

### **Opasi Perintah yang digunakan:**
- `-s` atau `--seeds`: Untuk menentukan alamat blockchain target.
- `-o` atau `--output`: Untuk menentukan file output yang akan menyimpan data JSON mentah.
- `-d` atau `--depth`: Untuk menentukan kedalaman perayapan, dengan nilai default 3.
- `-t` atau `--top`: Untuk menentukan jumlah alamat yang akan dirayapi dari hasil, dengan nilai default 20.
- `-l` atau `--limit`: Untuk menentukan jumlah maksimum alamat yang diambil dari satu alamat, dengan nilai default 100.

### **Contoh Pengunaan:**

**menelusuri riwayat transaksi dompet:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F
```

**Merayapi banyak dompet juga demikian:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F,1ETBbsHPvbydW7hGWXXKXZ3pxVh3VFoMaX
```

**mengambil 50 transaksi terakhir dari setiap dompet secara default, dengan ditambah opsi `-l`.:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -l 100
```

### **Kedalaman perayapan default ada 3 yaitu:**
mengambil riwayat dompet target, merayapi dompet yang baru ditemukan, dan kemudian merayapi dompet di hasilnya lagi.

**Kedalaman perayapan dapat ditingkatkan atau dikurangi dengan opsi `-d`.:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -d 2
```
**Dapat diperintahkan untuk merayapi dompet Nomer teratas di setiap level dengan menggunakan opsi `-t`.:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -t 20
```

**Jika Anda ingin melihat data yang dikumpulkan dengan penampil grafik pilihan Anda, Anda dapat menggunakan opsi -o.:**
```bash
python3 transchaincrawler.py -s 1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F -o keluaran.graphml
```

Format Dukungan
- `graphml` (Didukung oleh sebagian besar penampil grafik)
- `json` (Untuk pemrosesan mentah)


### Visualisasi

Setelah pemindaian selesai, grafik akan otomatis terbuka di browser default Anda. Jika tidak terbuka, buka `quark.html` secara manual.

Jangan khawatir jika grafik Anda terlihat berantakan,anda cukup Pilih opsi :
**Buat Klaster** untuk membentuk klaster menggunakan algoritma deteksi komunitas.Setelah itu, Anda dapat menggunakan **Color Clusters** untuk memberikan warna berbeda pada setiap komunitas, lalu menggunakan opsi **Spacify** untuk memperbaiki node & tepi yang tumpang tindih.

Ketebalan tepian bergantung pada frekuensi transaksi antara dua dompet, sedangkan ukuran node bergantung pada frekuensi transaksi dan jumlah koneksi node.

informasi selengkapnya tentang berbagai fitur dan kontrol anda bisa melihat:[Quark](https://github.com/s0md3v/Quark) untuk merender grafik.
