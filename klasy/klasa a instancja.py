class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, carBrand, carModel, carIsAirBagOk, carISPaintingOk, carIsMechanicOk):
        self.carBrand = carBrand
        self.carModel = carModel
        self.carIsAirBagOk = carIsAirBagOk
        self.carISPaintingOk = carISPaintingOk
        self.carIsMechanicOk = carIsMechanicOk
        self.numberOfCars += 1
        self.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.carIsAirBagOk and self.carISPaintingOk and self.carIsMechanicOk)
    
    def GetInfo(self):
        print(f"Car brand: {self.carBrand}, model: {self.carModel}, airbag ok: {self.carIsAirBagOk}, painting ok: {self.carISPaintingOk}, mechanic ok: {self.carIsMechanicOk}")

car01 = Car("seat", "ibiza", True, True, True)
car02 = Car("opel", "corsa", True, False, True)

print("Id of class is:", id(Car))
print("Id of car01 is:", id(car01))
print("Id of car02 is:", id(car02))

print('check if object belongs to class:', isinstance(car01, Car))
print('check if object belongs to class using type:', type(car01) == Car)
print("List of instances attributes with values:", vars(car01))

print(dir(car01))