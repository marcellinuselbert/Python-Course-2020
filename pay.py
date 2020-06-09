class Pay:
    def __init__(self,name,age,pay):
        self.name = name
        self.age = age
        self.pay = pay
    def cetak(self):
        return f'nama {self.name} bayaran {self.pay}'
    
    def tambahan(self):
        self.pay = self.pay * 2

employee = Pay("Marcell","16",150000)
manager = Pay("Richard","16",200000)

print(employee.cetak())
manager.tambahan()
print(manager.cetak())

