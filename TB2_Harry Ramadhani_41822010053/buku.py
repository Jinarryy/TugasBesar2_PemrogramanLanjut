class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, konten, ikhtisar):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten
        self.ikhtisar = ikhtisar

    def read(self, halaman_awal, halaman_akhir):
        # Asumsi: konten adalah list dari string di mana setiap string mewakili konten dari satu halaman
        return self.konten[halaman_awal-1:halaman_akhir]

    def __str__(self):
        return f"{self.judul} by {self.penulis}"
