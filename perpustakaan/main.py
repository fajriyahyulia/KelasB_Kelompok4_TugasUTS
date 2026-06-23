# Dikerjakan oleh: Fajriyah Yulia Az Zahra
# NIM: K3525005
# Username: fajriyahyulia
from perpustakaan.perpustakaan import Perpustakaan
from perpustakaan.buku import Buku
from perpustakaan.majalah import Majalah
from perpustakaan.jurnal import Jurnal

def garis():
    print("=" * 40)

def input_tidak_kosong(label: str) -> str:
    while True:
        data = input(f"{label:<15} : ").strip()
        if data:
            return data
        print("❌ Tidak boleh kosong!")

def input_int(label: str) -> int:
    while True:
        data = input_tidak_kosong(label)
        if data.isdigit():
            return int(data)
        print("❌ Harus berupa angka bulat!")

def input_data_dasar(perpus: Perpustakaan):
    while True:
        kode = input_tidak_kosong("Kode")
        if not perpus.kode_sudah_ada(kode):
            break
        print("❌ Kode sudah digunakan! Gunakan kode lain.")
        
    judul = input_tidak_kosong("Judul")
    tahun = input_int("Tahun")
    penerbit = input_tidak_kosong("Penerbit")
    return kode, judul, tahun, penerbit

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

        if pilihan in ["1", "2", "3"]:
            garis()
            if pilihan == "1":
                print("[ TAMBAH DATA BUKU ]")
            elif pilihan == "2":
                print("[ TAMBAH DATA MAJALAH ]")
            else:
                print("[ TAMBAH DATA JURNAL ]")
            garis()
            
            # Memanggil fungsi helper input data dasar (Lebih rapi & menghemat baris)
            kode, judul, tahun, penerbit = input_data_dasar(perpus)
            
            # Cek spesifik atribut tambahan per jenis
            if pilihan == "1":
                pengarang = input_tidak_kosong("Pengarang")
                perpus.tambah(Buku(kode, judul, tahun, pengarang, penerbit))
            elif pilihan == "2":
                edisi = input_tidak_kosong("Edisi")
                perpus.tambah(Majalah(kode, judul, tahun, penerbit, edisi))
            elif pilihan == "3":
                bidang = input_tidak_kosong("Bidang Studi")
                impact = input_tidak_kosong("Impact") 
                perpus.tambah(Jurnal(kode, judul, tahun, penerbit, bidang, impact))

        elif pilihan == "4":
            garis()
            perpus.tampil_semua()

        elif pilihan == "5":
            garis()
            print("[ HAPUS DATA KOLEKSI ]")
            garis()
            kode = input_tidak_kosong("Masukkan kode yang mau dihapus")
            
            # Logika interaksi UI hapus
            koleksi = perpus.cari_per_kode(kode)
            if koleksi:
                print("\nData ditemukan:")
                koleksi.tampilkan()
                konfirmasi = input("\nYakin mau hapus? (y/n): ").lower()
                if konfirmasi == "y":
                    perpus.hapus_objek(koleksi)
                else:
                    print("❌ Dibatalkan!")
            else:
                print("❌ Data tidak ditemukan!")

        elif pilihan == "0":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
