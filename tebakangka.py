import random



pilihan = " "

while pilihan != "no":
    jawaban = int(random.randrange(1,11))

    angka_tebakan = int(input("masukkan angka tebakan: "))

    if angka_tebakan == jawaban:
        print("selamat")
        pilihan = input("apakah anda ingin mencoba lagi (yes/no) ")

    elif angka_tebakan > jawaban:
        print("kegedean")
        
    elif angka_tebakan < jawaban:
        print("kekecilan")
    
