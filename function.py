
hour  = input("Masukan jam kerja: ")
salary = input("Masukan gaji anda: ")

def computepay(jam,gaji):
    
    if int(jam) > 40:
        return int(gaji) + 150
        
        
    else:
        return int(gaji)
    

print(computepay(hour,salary))

