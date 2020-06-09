class Mobil:
    def __init__(self,nama,merk,tahun):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
    def changename(self,newname):
        self.nama = newname
    def cetak(self):
        return f'jenis mobil adalah {self.nama}, merk mobilnya adalah {self.merk}, tahun keluaran {self.tahun}'

mobil1 = Mobil("i4","bmw","2015")

print(mobil1.cetak())
mobil1.changename("fortuner")
print(mobil1.cetak())
