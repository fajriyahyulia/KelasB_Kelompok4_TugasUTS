# Aplikasi Perpustakaan

Mata Kuliah : Pemrograman Berorientasi Objek  
Kelas       : B  
Kelompok    : 4  
Repositori  : KelasB_Kelompok4_TugasUTS  

---

## Anggota Kelompok

| Nama | NIM | Username | File |
|------|-----|----------|------|
| Fajriyah Yulia Az Zahra | K3525005 | fajriyahyulia | `main.py` |
| Fatimah Az Zahra | K3525006 | fatimahzahrara | `koleksi.py` |
| Riska Nur Rahmawati | K3525039 | riskarahmaa11 | `buku.py` |
| Vincensius Vicko R.S | K3525042 | pikoopikk | `majalah.py` |
| Wijang Pratama Putra | K3525043 | pratamaputra-pemula | `jurnal.py` |
| Abid Satriyo Maulana | K3525045 | maurinho011 | `perpustakaan.py` |

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
    ├── __init__.py
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
Berisi abstract class `Koleksi` yang menjadi induk dari semua jenis koleksi. Menyimpan atribut umum yaitu kode, judul, tahun, dan penerbit. Terdapat method `tampilkan_dasar()` untuk menampilkan atribut umum, serta dua abstract method `tampilkan()` dan `get_jenis()` yang wajib diimplementasikan oleh setiap subclass.

### buku.py (Rahma)
Berisi class `Buku` turunan dari `Koleksi`. Menambahkan atribut `pengarang` dan mengimplementasikan method `tampilkan()` serta `get_jenis()` sesuai kebutuhan data buku.

### majalah.py (Viko)
Berisi class `Majalah` turunan dari `Koleksi`. Menambahkan atribut `edisi` dan mengimplementasikan method `tampilkan()` serta `get_jenis()` sesuai kebutuhan data majalah.

### jurnal.py (Wijang)
Berisi class `Jurnal` turunan dari `Koleksi`. Menambahkan atribut `bidang` dan `impact` lalu mengimplementasikan method `tampilkan()` serta `get_jenis()` sesuai kebutuhan data jurnal.

### perpustakaan.py (Abid)
Berisi class `Perpustakaan` yang mengelola seluruh data koleksi. Menyediakan tiga method utama yaitu `tambah()`, `hapus()`, dan `tampil_semua()`. Class ini bergantung pada abstraksi `Koleksi` dengan type hint `List[Koleksi]`, bukan pada class konkret seperti Buku, Majalah, atau Jurnal secara langsung.

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
└── mengelola List[Koleksi]
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

## Empat Pilar OOP

### 1. Encapsulation
Setiap atribut disimpan di dalam class masing-masing dan hanya bisa diakses melalui instance objek. Atribut `pengarang` hanya ada di `Buku`, `edisi` hanya ada di `Majalah`, `bidang` dan `impact` hanya ada di `Jurnal`.

### 2. Inheritance (Pewarisan)
`Buku`, `Majalah`, dan `Jurnal` mewarisi atribut dan method dasar dari `Koleksi` melalui `super().__init__()`. Tidak perlu menulis ulang atribut `kode`, `judul`, `tahun`, `penerbit` di setiap subclass.

### 3. Polymorphism
Method `tampilkan()` dan `get_jenis()` dimiliki semua class dengan nama yang sama, namun implementasinya berbeda-beda sesuai jenis koleksi. Class `Perpustakaan` memanggil `item.tampilkan()` tanpa perlu tahu jenis konkretnya.

### 4. Abstraction
Class `Koleksi` menggunakan `ABC` dan `@abstractmethod` sehingga tidak bisa diinstansiasi langsung. Subclass dipaksa mengimplementasikan `tampilkan()` dan `get_jenis()` sebelum bisa digunakan.

---

## Penerapan Prinsip SOLID

### S — Single Responsibility Principle
Setiap class hanya punya satu tanggung jawab. `Koleksi` hanya urusan kontrak/template, `Buku/Majalah/Jurnal` hanya urusan data masing-masing, `Perpustakaan` hanya urusan CRUD, dan `main.py` hanya urusan alur program dan input user.

### O — Open/Closed Principle
Class `Perpustakaan` terbuka untuk perluasan tapi tertutup untuk modifikasi. Menambah jenis koleksi baru cukup dengan membuat subclass baru tanpa mengubah kode `Perpustakaan` sama sekali.

```python
# Contoh: menambah Koran tanpa ubah kode lama
class Koran(Koleksi):
    def get_jenis(self): return "Koran"
    def tampilkan(self): ...
```

### L — Liskov Substitution Principle
Objek `Buku`, `Majalah`, dan `Jurnal` dapat menggantikan objek `Koleksi` di mana saja tanpa merusak program. Semua subclass mengimplementasikan `tampilkan()` dan `get_jenis()` sesuai kontrak superclass.

### I — Interface Segregation Principle
Abstract method di class `Koleksi` hanya berisi kontrak yang benar-benar dibutuhkan semua subclass yaitu `tampilkan()` dan `get_jenis()`. Tidak ada method yang terpaksa diimplementasikan tapi tidak terpakai.

### D — Dependency Inversion Principle
Class `Perpustakaan` bergantung pada abstraksi `Koleksi`, bukan pada implementasi konkret. Hal ini terlihat dari type hint `List[Koleksi]` dan parameter `koleksi: Koleksi` di method `tambah()`.

```python
self.data_koleksi: List[Koleksi] = []        # bergantung ke abstraksi
def tambah(self, koleksi: Koleksi) -> bool:  # bukan ke Buku/Majalah/Jurnal
```

---

## Cara Menjalankan Program

1. Clone repositori ini
```
git clone https://github.com/fajriyahyulia/KelasB_Kelompok4_TugasUTS.git
```

2. Masuk ke folder repositori
```
cd KelasB_Kelompok4_TugasUTS
```

3. Jalankan program
```
python -m perpustakaan.main
```
atau di Windows:
```
py -m perpustakaan.main
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

1. Fajriyah membuat repositori dan push struktur awal ke branch `main`
2. Setiap anggota membuat branch masing-masing dari `main`
3. Setiap anggota mengerjakan file sesuai pembagian di branch masing-masing
4. Setelah selesai, masing-masing membuat pull request ke `main`
5. Fajriyah melakukan review dan merge semua branch ke `main`