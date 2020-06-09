import time


while True:
    
    pilihan = input("apakah ingin menggunakan kalkulator umur(y/n)")
    if pilihan == "n":
        break
    elif pilihan =="y":
        pass
        
    hari = int(input("masukkan tanggal berapa kalian lahir: "))
    bulan = int(input("masukkan bulan berapa kalian lahir: "))
    tahun = int(input("masukkan tahun berapa kalian lahir: "))

    print(f"Tanggal lahir kamu: {hari}-{bulan}-{tahun} ")

    tahunsekarang = int(time.strftime(" %Y "))
    bulansekarang = int(time.strftime("%m"))
    harisekarang= int(time.strftime("%d"))

    
    if bulansekarang > bulan and harisekarang > hari:
        
        tahunsekarang -= tahun
        harisekarang -= hari
        
        bulansekarang -= bulan 
        print(f'umur {abs(tahunsekarang)} tahun, lebih {abs(harisekarang)} hari,  lebih {abs(bulansekarang)} bulan')

    elif bulansekarang < bulan and harisekarang < hari:
        #abs = untuk membuat angkanya selalu positif 
       
        harisekarang -= hari
        bulansekarang -= bulan -1
        tahunsekarang -= tahun + 1
        print(f'{(tahunsekarang)} tahun,kurang {abs(30-harisekarang)} hari ,kurang {abs(bulansekarang)} bulan')

    elif bulansekarang > bulan and harisekarang < hari:
        #abs = untuk membuat angkanya selalu positif 
       
        harisekarang -= hari
        bulansekarang -= bulan + 1
        tahunsekarang -= tahun 
        print(f'{(tahunsekarang)} tahun, lebih {abs(30+harisekarang)} hari , lebih {abs(bulansekarang)} bulan')

    elif bulansekarang < bulan and harisekarang > hari:
        #abs = untuk membuat angkanya selalu positif 
       
        harisekarang -= hari
        bulansekarang -= bulan 
        tahunsekarang -= tahun + 1
        print(f'{(tahunsekarang)} tahun, kurang {abs(harisekarang)} hari ,kurang {abs(bulansekarang)} bulan')
    elif bulansekarang == bulan and harisekarang < hari or harisekarang > hari:
        
       
        harisekarang -= hari
        bulansekarang -= bulan 
        tahunsekarang -= tahun + 1
        print(f'{(tahunsekarang)} tahun, kurang {abs(harisekarang)} hari ,kurang {abs(bulansekarang)} bulan')
    
    elif bulansekarang == bulan and harisekarang == hari:
        tahunsekarang -= tahun
        print(f"Happy Birthday you are now {tahunsekarang} ")
    
    
    





