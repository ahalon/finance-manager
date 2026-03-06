class Car:
    def __init__(self, carBrand, carModel, carIsAirBagOk, carISPaintingOk, carIsMechanicOk):
        self.carBrand = carBrand
        self.carModel = carModel
        self.carIsAirBagOk = carIsAirBagOk
        self.carISPaintingOk = carISPaintingOk
        self.carIsMechanicOk = carIsMechanicOk

    def IsDamaged(self):
        return not (self.carIsAirBagOk and self.carISPaintingOk and self.carIsMechanicOk)
    
    def GetInfo(self):
        print(f"Car brand: {self.carBrand}, model: {self.carModel}, airbag ok: {self.carIsAirBagOk}, painting ok: {self.carISPaintingOk}, mechanic ok: {self.carIsMechanicOk}")

car01 = Car("seat", "ibiza", True, True, True)
car02 = Car("opel", "corsa", True, False, True)

print(car01.IsDamaged())
print(car02.IsDamaged())
car01.GetInfo()
car02.GetInfo()
