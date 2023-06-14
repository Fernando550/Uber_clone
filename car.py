# Super class
class Car:
    id = int
    def __init__(self, driver, license):
        self.id = id
        self.driver = driver
        self.license = license


# childs classes
class UberX(Car):
    def __init__(self, driver, license, brand, model):
        super().__init__(driver, license)
        self.brand = brand
        self.model = model

class UberPool(Car):
    def __init__(self, driver, license, brand, model):
        super().__init__(driver, license)
        self.brand = brand
        self.brand = model

class UberBlack(Car):
    def __init__(self, driver, license, typeCarAccepted, seatMaterial):
        super().__init__(driver, license)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterial = seatMaterial
        
class UberBan(Car):
    def __init__(self, driver, license, typeCarAccepted, seatMaterial):
        super().__init__(driver, license)
        self.typeCarAccepted = typeCarAccepted
        self.seatMaterial = seatMaterial
