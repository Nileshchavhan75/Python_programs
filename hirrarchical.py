class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def showBrand(self):
        print("Brand: ",self.brand)

class Car(Vehicle):
    def __init__(self, brand,seats):
        super().__init__(brand)
        self.seats = seats

    def showCarInfo(self):
        print("Seats: ",self.seats)
    
class Bike(Vehicle):
    def __init__(self, brand,cc):
        super().__init__(brand)
        self.cc = cc
    
    def showBikeInfo(self):
        print("cc: ",self.cc)

C = Car("TATA",4)
C.showBrand()
C.showCarInfo()

B = Bike("Yamaha",160)
B.showBrand()
B.showBikeInfo()