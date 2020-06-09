import time


def rapih(dictionary):
    for key,value in dictionary.items():
        print (f'{key} : {value}' )


john = {
    "Fullname" : "John Smith",
    "Age" : "25",
    "Crime" : "Stealing"
    }



bill = {
    "Fullname" : "Bill Turner",
    "Age" : "30",
    "Crime" : "Drug Dealing"
}

rose = {
    "Fullname" : "Rose Miller",
    "Age" : "45",
    "Crime" : "Car Theft"
}

james = {
    "Fullname" : "James Richard",
    "Age" : "27",
    "Crime" : "Burglary"
}








real_password = "america"

b= 0
password =""
while password != real_password:
    password = input("password please: ") 

while b < 3:
    b += 1
    for x in range(0,4):
        time.sleep(0.5)
        print("logging in"+"." * x)
print("\n")
print("MOST WANTED LIST")
print("----------------")

rapih(john)
print(" \n")
rapih(bill)
print(" \n")
rapih(rose)
print(" \n")
rapih(james)




