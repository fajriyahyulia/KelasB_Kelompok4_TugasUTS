# dikerjakan oeh: Wijang Pratama Putra
# username: pratamaputra-pemula
from perpustakaan.koleksi import Koleksi

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang, impact):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang = bidang
        self.impact = impact

    def get_jenis(self):
        return "Jurnal"

    def tampilkan(self):
        print("=" * 40)
        print("Jenis       : Jurnal")
        self.tampilkan_dasar()
        print(f"Bidang Studi: {self.bidang}")
        print(f"Impact      : {self.impact}")
