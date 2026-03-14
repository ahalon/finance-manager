brandOnSale = "opel"


class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, carBrand, carModel, carIsAirBagOk, carISPaintingOk, carIsMechanicOk, __isOnSale):
        self.carBrand = carBrand
        self.carModel = carModel
        self.carIsAirBagOk = carIsAirBagOk
        self.carISPaintingOk = carISPaintingOk
        self.carIsMechanicOk = carIsMechanicOk
        self.__isOnSale = __isOnSale
        self.numberOfCars += 1
        self.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.carIsAirBagOk and self.carISPaintingOk and self.carIsMechanicOk)
    
    def GetInfo(self):
        print(f"Car brand: {self.carBrand}")
        print(f"Car model: {self.carModel}")
        print(f"Airbag ok: {self.carIsAirBagOk}")
        print(f"Painting ok: {self.carISPaintingOk}")
        print(f"Mechanic ok: {self.carIsMechanicOk}")
        print(f"Is on sale: {self.__isOnSale}")

    def getIsItOnSale(self):
        return self.__isOnSale
    
    def SetIsOnSale(self, newIsOnSale):
        if self.carBrand == brandOnSale:
            self.__isOnSale = newIsOnSale
            print(f"Sale status for {self.carBrand} {self.carModel} has been changed to: {self.__isOnSale}")
        else:
            print("Changing sale status is not allowed for this car brand.")
    
    IsOnSale = property(getIsItOnSale, SetIsOnSale), None, "if set to true, the car is on sale, if set to false, the car is not on sale"

car01 = Car("seat", "ibiza", True, True, True, False)
car02 = Car("opel", "corsa", True, False, True, True)

car01.SetIsOnSale(True)
car02.SetIsOnSale(True) 