class Car:
    def __init__(self, carBrand, carModel, carIsAirBagOk, carISPaintingOk, carIsMechanicOk):
        self.carBrand = carBrand
        self.carModel = carModel
        self.carIsAirBagOk = carIsAirBagOk
        self.carISPaintingOk = carISPaintingOk
        self.carIsMechanicOk = carIsMechanicOk

car01 = Car("seat", "ibiza", True, True, True)
car02 = Car("opel", "corsa", True, False, True)

