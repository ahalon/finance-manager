car_01 = {
    "carBrand" : "seat",
    "carModel" : "ibiza",
    "carIsAirBagOk" : True,
    "carISPaintingOk" : True,
    "carIsMechanicOk" : True}


def IsCarDamaged(aCar):
    return not (aCar["carIsAirBagOk"] and aCar["carISPaintingOk"] and aCar["carIsMechanicOk"])

print(IsCarDamaged(car_01))