# Aplikasi Perpustakaan
Mata Kuliah : Pemrograman Berorientasi Objek  
Kelas       : B  
Kelompok    : 4  
Repositori  : KelasB_Kelompok4_TugasUTS  

---

## Anggota Kelompok

| Nama | NIM | Branch |
|------|-----|--------|
| Fajriyah Yulia Az Zahra | K3525005 | `main` |
| Fatimah Az Zahra | K3525006 | `fatimah-koleksi` |
| Riska Nur Rahmawati | K3525039 | `rahma-buku` |
| Vincensius Vicko Riska S | K3525042 | `viko-majalah` |
| Wijang Pratama Putra | K3525043 | `wijang-jurnal` |
| Abid Satriyo Maulana | K3525045 | `abid-perpustakaan` |

---

## Deskripsi Program

Aplikasi Perpustakaan adalah program berbasis terminal yang dibuat menggunakan Python dengan menerapkan konsep Pemrograman Berorientasi Objek (PBO). Program ini mampu mengelola data koleksi perpustakaan yang terdiri dari tiga jenis koleksi yaitu Buku, Majalah, dan Jurnal. Setiap koleksi memiliki atribut yang berbeda-beda namun tetap mengacu pada satu struktur induk yang sama.

Program mendukung tiga fitur utama yaitu menambah data koleksi, menghapus data koleksi berdasarkan kode, dan menampilkan seluruh data koleksi yang tersimpan. Terdapat pula validasi input agar data yang masuk tidak kosong, sesuai tipe data, dan tidak ada duplikasi kode koleksi.

---

## Struktur Folder

```
KelasB_Kelompok4_TugasUTS/
├── README.md
└── perpustakaan/
    ├── koleksi.py
    ├── buku.py
    ├── majalah.py
    ├── jurnal.py
    ├── perpustakaan.py
    └── main.py
```

---

## Penjelasan Setiap File

### koleksi.py (Fatimah)
Berisi abstract class `Koleksi` yang menjadi induk dari semua jenis koleksi. Class ini menyimpan atribut umum yaitu kode, judul, tahun, dan penerbit. Terdapat method `tampilkan_dasar()` untuk menampilkan atribut umum tersebut, serta abstract method `tampilkan()` yang wajib diimplementasikan oleh setiap subclass.

### buku.py (Rahma)
Berisi class `Buku` yang merupakan turunan dari `Koleksi`. Menambahkan atribut `pengarang` dan mengimplementasikan method `tampilkan()` sesuai kebutuhan data buku.

### majalah.py (Viko)
Berisi class `Majalah` yang merupakan turunan dari `Koleksi`. Menambahkan atribut `edisi` dan mengimplementasikan method `tampilkan()` sesuai kebutuhan data majalah.

### jurnal.py (Wijang)
Berisi class `Jurnal` yang merupakan turunan dari `Koleksi`. Menambahkan atribut `bidang` dan `impact` lalu mengimplementasikan method `tampilkan()` sesuai kebutuhan data jurnal.

### perpustakaan.py (Abid)
Berisi class `Perpustakaan` yang mengelola seluruh data koleksi. Menyediakan tiga method utama yaitu `tambah()`, `hapus()`, dan `tampil_semua()`. Class ini hanya bergantung pada abstraksi `Koleksi`, bukan pada class konkret seperti Buku, Majalah, atau Jurnal secara langsung.

### main.py (Fajriya)
File utama yang menjalankan program. Berisi menu interaktif, fungsi validasi input, dan integrasi seluruh komponen program.

---

## Struktur Class

```
Koleksi (Abstract Class)
├── Buku
├── Majalah
└── Jurnal

Perpustakaan
└── mengelola list of Koleksi
```

---

## Atribut Setiap Koleksi

### Buku
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| kode | str | Kode unik koleksi |
| judul | str | Judul buku |
| tahun | int | Tahun terbit |
| pengarang | str | Nama pengarang |
| penerbit | str | Nama penerbit |

### Majalah
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| kode | str | Kode unik koleksi |
| judul | str | Judul majalah |
| tahun | int | Tahun terbit |
| penerbit | str | Nama penerbit |
| edisi | str | Nomor atau nama edisi |

### Jurnal
| Atribut | Tipe | Keterangan |
|---------|------|------------|
| kode | str | Kode unik koleksi |
| judul | str | Judul jurnal |
| tahun | int | Tahun terbit |
| penerbit | str | Nama penerbit |
| bidang | str | Bidang studi jurnal |
| impact | float | Nilai impact factor |

---

## Penerapan Prinsip SOLID

### Single Responsibility Principle (SRP)
Setiap file dan class hanya memiliki satu tanggung jawab. `koleksi.py` hanya urusan struktur dasar koleksi, `perpustakaan.py` hanya urusan pengelolaan data, dan `main.py` hanya urusan alur program dan input user.

### Open/Closed Principle (OCP)
Class `Perpustakaan` terbuka untuk perluasan tapi tertutup untuk modifikasi. Jika ingin menambah jenis koleksi baru seperti DVD Film, cukup buat subclass baru tanpa mengubah kode `Perpustakaan` sama sekali.

### Liskov Substitution Principle (LSP)
Objek `Buku`, `Majalah`, dan `Jurnal` dapat menggantikan objek `Koleksi` di mana saja tanpa merusak jalannya program. Semua subclass mengimplementasikan method `tampilkan()` dengan benar sesuai kontrak dari superclass.

### Interface Segregation Principle (ISP)
Abstract method `tampilkan()` di class `Koleksi` berfungsi sebagai kontrak interface yang spesifik, memastikan setiap koleksi hanya diwajibkan mengimplementasikan method yang memang relevan dengan jenisnya.

### Dependency Inversion Principle (DIP)
Class `Perpustakaan` bergantung pada abstraksi `Koleksi`, bukan pada implementasi konkret seperti `Buku` atau `Majalah`. Hal ini membuat program lebih fleksibel dan mudah dikembangkan.

---

## Cara Menjalankan Program

1. Clone repositori ini
```
git clone https://github.com/namaakun/KelasB_Kelompok4_TugasUTS.git
```

2. Masuk ke folder repositori
```
cd KelasB_Kelompok4_TugasUTS
```

3. Jalankan program
```
python -m perpustakaan.main
```

---

## Cara Kerja Program

Program menampilkan menu utama dengan empat pilihan. User memilih menu yang diinginkan lalu mengikuti instruksi yang muncul di layar. Program akan terus berjalan sampai user memilih menu keluar.

Menu 1 - Tambah data: user memilih jenis koleksi lalu mengisi atribut yang diminta. Program memvalidasi setiap input sebelum data disimpan.

Menu 2 - Hapus data: user memasukkan kode koleksi. Jika ditemukan, data ditampilkan untuk dikonfirmasi sebelum dihapus.

Menu 3 - Tampilkan data: program menampilkan seluruh koleksi yang tersimpan beserta detailnya.

Menu 4 - Keluar: program berhenti.

---

## Pembagian Tugas dan Branch

| Nama | Branch | File | Prinsip SOLID |
|------|--------|------|---------------|
| Fajriya | `main` | `main.py` | SRP |
| Fatimah | `fatimah-koleksi` | `koleksi.py` | SRP, ISP |
| Rahma | `rahma-buku` | `buku.py` | LSP |
| Viko | `viko-majalah` | `majalah.py` | LSP |
| Wijang | `wijang-jurnal` | `jurnal.py` | LSP |
| Abid | `abid-perpustakaan` | `perpustakaan.py` | OCP, DIP |

---

## Alur Kerja GitHub

1. Fajriya membuat repositori dan push struktur awal ke branch `main`
2. Setiap anggota membuat branch masing-masing dari `main`
3. Setiap anggota mengerjakan file sesuai pembagian di branch masing-masing
4. Setelah selesai, masing-masing membuat pull request ke `main`
5. Fajriya melakukan review dan merge semua branch ke `main`