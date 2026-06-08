# dikerjakan oleh: Vincensius Vicko R.S (K3525042)
# username: pikoopikk
from perpustakaan.koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi = edisi

    def get_jenis(self):
        return "Majalah"

    def tampilkan(self):
        print("=" * 40)
        print("Jenis    : Majalah")
        self.tampilkan_dasar()
        print(f"Edisi    : {self.edisi}")
