import random

while True:
    pilihan = input("wanna roll?(y/n): ")
    
    if pilihan == "y":
        print(f'you have rolled: {random.randint(1,6)}')    
    elif pilihan == "n":
        break
