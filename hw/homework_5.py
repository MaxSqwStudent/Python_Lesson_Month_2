class Vehicle:
    @classmethod
    def start(cls):
        print(f"Vehicle starting")

class Car(Vehicle):
    @classmethod
    def start(cls):
        super().start()
        print(f"Car starting")


class ElectricCar(Vehicle):
    pass

class Tesla(ElectricCar, Car):
    @classmethod
    def start(cls):
        super().start()
        print(f"Tesla ready")

Tesla.start()