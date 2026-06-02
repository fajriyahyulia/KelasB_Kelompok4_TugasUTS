# dikerjakan oleh: Vicko
# username: (pikoopikk)

from perpustakaan.koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi = edisi
    
    def tampilkan(self):
        print("Jenis    : Majalah")
        self.tampilkan_dasar()
        print(f"Edisi    : {self.edisi}")
