from abc import ABC, abstractmethod

# =========================
# UTIL / UX
# =========================
def garis():
    print("=" * 40)

def pause():
    input("\nTekan ENTER untuk kembali ke menu program")

# =========================
# INPUT RAPI
# =========================
def input_rata(label):
    return input(f"Masukkan {label:<20} : ").strip()

# =========================
# VALIDASI INPUT
# =========================
def input_tidak_kosong(label):
    while True:
        data = input_rata(label)
        if data:
            return data
        print("❌ Tidak boleh kosong!")

def input_int(label):
    while True:
        data = input_rata(label)
        if data.isdigit():
            return int(data)
        print("❌ Harus berupa angka!")

def input_float(label):
    while True:
        data = input_rata(label)
        try:
            return float(data)
        except:
            print("❌ Harus berupa angka (boleh desimal)!")

# =========================
# [❌ DIP] data_koleksi adalah variabel global, bukan bagian dari class.
# Seharusnya dikelola oleh class Perpustakaan (seperti di versi final).
# =========================
data_koleksi = []

# =========================
# [❌ SRP] Fungsi kode_sudah_ada() dan input_kode_unik() seharusnya
# menjadi method di dalam class Perpustakaan, bukan fungsi global.
# =========================
def kode_sudah_ada(kode):
    for item in data_koleksi:
        if item.kode == kode:
            return True
    return False

def input_kode_unik():
    while True:
        kode = input_tidak_kosong("Kode Koleksi")
        if not kode_sudah_ada(kode):
            return kode
        print("❌ Kode sudah digunakan!")

# =========================
# CLASS INDUK
# [❌ ISP] Belum ada abstract method get_jenis(),
# sehingga kontrak ke subclass belum lengkap.
# =========================
class Koleksi(ABC):
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun
        self.penerbit = penerbit

    def tampilkan_dasar(self):
        print(f"Kode        : {self.kode}")
        print(f"Judul       : {self.judul}")
        print(f"Tahun       : {self.tahun}")
        print(f"Penerbit    : {self.penerbit}")

    @abstractmethod
    def tampilkan(self):
        pass

    # [❌ ISP] Tidak ada abstract method get_jenis() di sini

# =========================
# CLASS TURUNAN
# [❌ ISP] Semua subclass belum mengimplementasi get_jenis()
# =========================
class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun, penerbit)
        self.pengarang = pengarang

    # [❌ ISP] Belum ada get_jenis()
    def tampilkan(self):
        garis()
        print("Jenis       : Buku")
        self.tampilkan_dasar()
        print(f"Pengarang   : {self.pengarang}")

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi = edisi

    # [❌ ISP] Belum ada get_jenis()
    def tampilkan(self):
        garis()
        print("Jenis       : Majalah")
        self.tampilkan_dasar()
        print(f"Edisi       : {self.edisi}")

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang, impact):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang = bidang
        self.impact = impact

    # [❌ ISP] Belum ada get_jenis()
    def tampilkan(self):
        garis()
        print("Jenis       : Jurnal")
        self.tampilkan_dasar()
        print(f"Bidang Studi: {self.bidang}")
        print(f"Impact      : {self.impact}")

# =========================
# [❌ SRP] Fungsi tambah_data(), hapus_data(), tampil_data()
# seharusnya menjadi method di dalam class Perpustakaan.
# Fungsi global ini mencampur logika data dengan logika UI.
# =========================
def tambah_data():
    garis()
    print("JENIS KOLEKSI")
    print("1. Buku")
    print("2. Majalah")
    print("3. Jurnal")

    pilih = input("Pilih: ")

    if pilih == "1":
        garis()
        print("TAMBAH DATA BUKU")
        kode = input_kode_unik()
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        pengarang = input_tidak_kosong("Pengarang")
        penerbit = input_tidak_kosong("Penerbit")
        data_koleksi.append(Buku(kode, judul, tahun, pengarang, penerbit))
        print("\n✔ Tambah Buku Sukses")

    elif pilih == "2":
        garis()
        print("TAMBAH DATA MAJALAH")
        kode = input_kode_unik()
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        penerbit = input_tidak_kosong("Penerbit")
        edisi = input_tidak_kosong("Edisi")
        data_koleksi.append(Majalah(kode, judul, tahun, penerbit, edisi))
        print("\n✔ Tambah Majalah Sukses")

    elif pilih == "3":
        garis()
        print("TAMBAH DATA JURNAL")
        kode = input_kode_unik()
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        penerbit = input_tidak_kosong("Penerbit")
        bidang = input_tidak_kosong("Bidang Studi")
        impact = input_float("Impact Factor")
        data_koleksi.append(Jurnal(kode, judul, tahun, penerbit, bidang, impact))
        print("\n✔ Tambah Jurnal Sukses")

    else:
        print("❌ Pilihan tidak valid")

    pause()

def hapus_data():
    garis()
    print("HAPUS DATA KOLEKSI")

    if not data_koleksi:
        print("❌ Tidak ada data")
        pause()
        return

    kode = input_tidak_kosong("Kode Koleksi")

    for item in data_koleksi:
        if item.kode == kode:
            print("\nData ditemukan:")
            item.tampilkan()
            konfirmasi = input("\nYakin mau hapus? (y/n): ").lower()
            if konfirmasi == "y":
                data_koleksi.remove(item)
                print("\n✔ Hapus data sukses")
            else:
                print("\n❌ Dibatalkan")
            break
    else:
        print("\n❌ Data tidak ditemukan")

    pause()

def tampil_data():
    garis()
    print("DATA KOLEKSI")

    if not data_koleksi:
        print("\nBelum ada data")
    else:
        for i, item in enumerate(data_koleksi, 1):
            print(f"\nKoleksi {i}")
            item.tampilkan()

    pause()

# =========================
# [❌ SRP] Loop utama program berjalan langsung di level global,
# seharusnya dibungkus dalam fungsi main() dan dipanggil
# dengan if __name__ == "__main__"
# =========================
while True:
    garis()
    print("MENU PROGRAM")
    print("1. Tambah data koleksi")
    print("2. Hapus data koleksi")
    print("3. Tampilkan semua data")
    print("4. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        hapus_data()
    elif menu == "3":
        tampil_data()
    elif menu == "4":
        print("Program selesai")
        break
    else:
        print("❌ Pilihan tidak valid")