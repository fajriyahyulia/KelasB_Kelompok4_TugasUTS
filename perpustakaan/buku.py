# dikerjakan oeh: Riska Nur Rahmawati (K3525039)
# username: (riskarahmaa11)

from perpustakaan.koleksi import Koleksi

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun, penerbit)
        self.pengarang = pengarang

    def get_jenis(self):
        return "Buku"

    def tampilkan(self):
        print("=" * 40)
        print("Jenis    : Buku")
        self.tampilkan_dasar()
        print(f"Pengarang: {self.pengarang}")
