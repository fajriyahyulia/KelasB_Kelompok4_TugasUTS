# dikerjakan oleh: Abid Satriyo Maulana (K3525045)
# username: maurinho011
from perpustakaan.koleksi import Koleksi
from typing import List, Optional

class Perpustakaan:
    def __init__(self):
        self.data_koleksi: List[Koleksi] = []

    def kode_sudah_ada(self, kode: str) -> bool:
        for item in self.data_koleksi:
            if item.kode == kode:
                return True
        return False

    def tambah(self, koleksi: Koleksi) -> bool:
        if self.kode_sudah_ada(koleksi.kode):
            print("❌ Kode sudah digunakan!")
            return False
        self.data_koleksi.append(koleksi)
        print("✔ Data berhasil ditambahkan!")
        return True

    # Perbaikan SRP: Method ini sekarang mengembalikan objek jika ditemukan,
    # proses hapus & konfirmasi dilakukan di main.py agar class ini bebas dari UI input()
    def cari_per_kode(self, kode: str) -> Optional[Koleksi]:
        for item in self.data_koleksi:
            if item.kode == kode:
                return item
        return None

    def hapus_objek(self, koleksi: Koleksi) -> None:
        if koleksi in self.data_koleksi:
            self.data_koleksi.remove(koleksi)
            print("✔ Data berhasil dihapus!")

    def tampil_semua(self) -> None:
        if not self.data_koleksi:
            print("Belum ada data koleksi!")
            return
        for i, item in enumerate(self.data_koleksi, 1):
            print(f"\nKoleksi {i}")
            item.tampilkan()
