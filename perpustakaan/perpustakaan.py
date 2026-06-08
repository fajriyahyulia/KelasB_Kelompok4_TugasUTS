# dikerjakan oleh: Abid Satriyo Maulana (K3525045)
# username: maurinho011
from perpustakaan.koleksi import Koleksi
from typing import List

class Perpustakaan:
    def __init__(self):
        self.data_koleksi: List[Koleksi] = []

    # ========================
    # VALIDASI
    # ========================
    def kode_sudah_ada(self, kode: str) -> bool:
        for item in self.data_koleksi:
            if item.kode == kode:
                return True
        return False

    # ========================
    # TAMBAH
    # ========================
    def tambah(self, koleksi: Koleksi) -> bool:
        if self.kode_sudah_ada(koleksi.kode):
            print("❌ Kode sudah digunakan!")
            return False
        self.data_koleksi.append(koleksi)
        print("✔ Data berhasil ditambahkan!")
        return True

    # ========================
    # HAPUS
    # ========================
    def hapus(self, kode: str) -> None:
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
    def tampil_semua(self) -> None:
        if not self.data_koleksi:
            print("Belum ada data koleksi!")
            return
        for i, item in enumerate(self.data_koleksi, 1):
            print(f"\nKoleksi {i}")
            item.tampilkan()