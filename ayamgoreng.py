tepung = input("punya tepung (y/n)")
ayam = input("punya ayam(y/n)")

if tepung == "y" and ayam == "y":
    print("bisa bikin ayam goreng")

elif tepung == "y" and ayam == "n":
    print("tidak bisa buat ayam goreng cuman punya tepung")
elif tepung == "n" and ayam == "y":
    print("tidak bisa buat ayam goreng cuman punya ayam")
elif tepung == "n" and ayam == "n":
    print("tidak bisa buat ayam goreng gak punya apa apa")
else:
    print("invalid input")