flowers= []
class Bunga:

    def __init__(self,nama,kelopak,harga):
        self.nama = nama
        self.kelopak = kelopak
        self.harga = harga
    
    def cetak(self):
        return f'nama bunga {self.nama}, jumlah kelopak {self.kelopak}, harganya {self.harga}'

    
while True:
    pilihan = input("masukkan (y/n)")
    if pilihan == "y":
    
        nama_bunga = input("nama bunga : ")
        kelopak_bunga = int(input("berapa kelopak bunga: "))
        harga_bunga = float(input("berapa harganya: "))

        flower = Bunga(nama_bunga,kelopak_bunga,harga_bunga)
        flowers.append(flower)
    elif pilihan == "n":
        break
for x in flowers:
    print(x.cetak())


   

   


'''
    @classmethod
    def class_method(cls):
        nama = input("Masukkan Nama bunga: ")
        kelopak = int(input("Masukkan jumlah kelopak: "))
        harga = float(input ("Masukkan Harga bunga: "))
        return (nama,kelopak,harga)
'''




