import time

while True:
  
    try:
        
        pilih = (input("apakah ingin menggunakan timer(y/n)"))
    
        if pilih == "y":

            detik = int(input("masukkan berapa detik: "))
            menit = int(input("masukkan berapa menit: "))
            jam = int(input("masukkan berapa jam: "))

            waktu = detik + menit*60 + jam*3600
        elif pilih == "n":
            break
        for x in range(waktu+1):
            
            print(waktu-x)
            time.sleep(1)
        print("time's up")

    
        
    
    except ValueError:
        print("oops harus angka!")




