# dikerjakan oeh: Abid
# username: maurinho011

from perpustakaan.koleksi import Koleksi

class Perpustakaan:
    def __init__(self):
        self.data_koleksi = []
    
    # ========================
    # VALIDASI
    # ========================
    def kode_sudah_ada(self, kode):
        for item in self.data_koleksi:
            if item.kode == kode:
                return True
        return False
    
    # ========================
    # TAMBAH
    # ========================
    def tambah(self, koleksi: Koleksi):
        if self.kode_sudah_ada(koleksi.kode):
            print("❌ Kode sudah digunakan!")
            return False
        self.data_koleksi.append(koleksi)
        print("✔ Data berhasil ditambahkan!")
        return True
    
    # ========================
    # HAPUS
    # ========================
    def hapus(self, kode):
        for item in self.data_koleksi:
            if item.kode == kode:
                item.tampilkan()
                konfirmasi = input("\nYakin mau hapus? (y/n): ").lower()
                if konfirmasi == "y":
                    self.data_koleksi.remove(item)
                    print("✔ Data berhasil dihapus!")
                else:
                    print("❌ Dibatalkan!")
                return
        print("❌ Data tidak ditemukan!")
    
    # ========================
    # TAMPIL
    # ========================
    def tampil_semua(self):
        if not self.data_koleksi:
            print("Belum ada data koleksi!")
            return
        for i, item in enumerate(self.data_koleksi, 1):
            print(f"\nKoleksi {i}")
            print("=" * 40)
            item.tampilkan()
