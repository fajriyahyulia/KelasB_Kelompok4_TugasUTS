# Dikerjakan oeh: 
# Nama: Fajriyah Yulia Az Zahra 
# NIM: K3525005
# Username: fajriyahyulia

from perpustakaan.perpustakaan import Perpustakaan
from perpustakaan.buku import Buku
from perpustakaan.majalah import Majalah
from perpustakaan.jurnal import Jurnal

# ========================
# UTIL
# ========================
def garis():
    print("=" * 40)

def pause():
    input("\nTekan ENTER untuk kembali ke menu...")

# ========================
# VALIDASI INPUT
# ========================
def input_tidak_kosong(label):
    while True:
        data = input(f"Masukkan {label:<20} : ").strip()
        if data:
            return data
        print("❌ Tidak boleh kosong!")

def input_int(label):
    while True:
        data = input(f"Masukkan {label:<20} : ").strip()
        if data.isdigit():
            return int(data)
        print("❌ Harus berupa angka!")

def input_float(label):
    while True:
        data = input(f"Masukkan {label:<20} : ").strip()
        try:
            return float(data)
        except:
            print("❌ Harus berupa angka desimal!")

# ========================
# INPUT KODE UNIK
# ========================
def input_kode_unik(perpus):
    while True:
        kode = input_tidak_kosong("Kode Koleksi")
        if not perpus.kode_sudah_ada(kode):
            return kode
        print("❌ Kode sudah digunakan!")

# ========================
# MENU TAMBAH
# ========================
def menu_tambah(perpus):
    garis()
    print("JENIS KOLEKSI")
    print("1. Buku")
    print("2. Majalah")
    print("3. Jurnal")
    pilih = input("Pilih: ")

    if pilih == "1":
        garis()
        print("TAMBAH DATA BUKU")
        kode = input_kode_unik(perpus)
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        pengarang = input_tidak_kosong("Pengarang")
        penerbit = input_tidak_kosong("Penerbit")
        perpus.tambah(Buku(kode, judul, tahun, pengarang, penerbit))

    elif pilih == "2":
        garis()
        print("TAMBAH DATA MAJALAH")
        kode = input_kode_unik(perpus)
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        penerbit = input_tidak_kosong("Penerbit")
        edisi = input_tidak_kosong("Edisi")
        perpus.tambah(Majalah(kode, judul, tahun, penerbit, edisi))

    elif pilih == "3":
        garis()
        print("TAMBAH DATA JURNAL")
        kode = input_kode_unik(perpus)
        judul = input_tidak_kosong("Judul")
        tahun = input_int("Tahun Terbit")
        penerbit = input_tidak_kosong("Penerbit")
        bidang = input_tidak_kosong("Bidang Studi")
        impact = input_float("Impact Factor")
        perpus.tambah(Jurnal(kode, judul, tahun, penerbit, bidang, impact))

    else:
        print("❌ Pilihan tidak valid!")
    
    pause()

# ========================
# MENU HAPUS
# ========================
def menu_hapus(perpus):
    garis()
    print("HAPUS DATA KOLEKSI")
    if not perpus.data_koleksi:
        print("❌ Belum ada data!")
        pause()
        return
    kode = input_tidak_kosong("Kode Koleksi")
    perpus.hapus(kode)
    pause()

# ========================
# MENU TAMPIL
# ========================
def menu_tampil(perpus):
    garis()
    print("DATA KOLEKSI")
    perpus.tampil_semua()
    pause()

# ========================
# MAIN
# ========================
def main():
    perpus = Perpustakaan()

    while True:
        garis()
        print("MENU PROGRAM")
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampilkan semua data")
        print("4. Keluar")
        menu = input("Pilih menu: ")

        if menu == "1":
            menu_tambah(perpus)
        elif menu == "2":
            menu_hapus(perpus)
        elif menu == "3":
            menu_tampil(perpus)
        elif menu == "4":
            print("Program selesai!")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()