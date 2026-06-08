# dikerjakan oleh: 
# Fatimah Az Zahra K3525006
# username: @fatimahzahrara

from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun
        self.penerbit = penerbit
    
    def tampilkan_dasar(self):
        print(f"Kode     : {self.kode}")
        print(f"Judul    : {self.judul}")
        print(f"Tahun    : {self.tahun}")
        print(f"Penerbit : {self.penerbit}")
    
    @abstractmethod
    def tampilkan(self):
        pass

    @abstractmethod
    def get_jenis(self):
        pass
