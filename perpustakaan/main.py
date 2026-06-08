# Dikerjakan oleh: Fajriyah Yulia Az Zahra
# NIM: K3525005
# Username: fajriyahyulia
from perpustakaan.perpustakaan import Perpustakaan
from perpustakaan.buku import Buku
from perpustakaan.majalah import Majalah
from perpustakaan.jurnal import Jurnal

def garis():
    print("=" * 40)

def menu():
    garis()
    print("   APLIKASI PERPUSTAKAAN")
    garis()
    print("1. Tambah Buku")
    print("2. Tambah Majalah")
    print("3. Tambah Jurnal")
    print("4. Tampil Semua Koleksi")
    print("5. Hapus Koleksi")
    print("0. Keluar")
    garis()

def main():
    perpus = Perpustakaan()

    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            garis()
            kode      = input("Kode      : ")
            judul     = input("Judul     : ")
            tahun     = input("Tahun     : ")
            pengarang = input("Pengarang : ")
            penerbit  = input("Penerbit  : ")
            perpus.tambah(Buku(kode, judul, tahun, pengarang, penerbit))

        elif pilihan == "2":
            garis()
            kode     = input("Kode     : ")
            judul    = input("Judul    : ")
            tahun    = input("Tahun    : ")
            penerbit = input("Penerbit : ")
            edisi    = input("Edisi    : ")
            perpus.tambah(Majalah(kode, judul, tahun, penerbit, edisi))

        elif pilihan == "3":
            garis()
            kode     = input("Kode         : ")
            judul    = input("Judul        : ")
            tahun    = input("Tahun        : ")
            penerbit = input("Penerbit     : ")
            bidang   = input("Bidang Studi : ")
            impact   = input("Impact       : ")
            perpus.tambah(Jurnal(kode, judul, tahun, penerbit, bidang, impact))

        elif pilihan == "4":
            garis()
            perpus.tampil_semua()

        elif pilihan == "5":
            garis()
            kode = input("Masukkan kode yang mau dihapus: ")
            perpus.hapus(kode)

        elif pilihan == "0":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()