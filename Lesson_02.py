# Родительский класс / Супер класс
class Car:
    # Конструктор / инициализатор
    def __init__(self, wheels, b, c):
        self.wheels = wheels
        self.color = b
        self.make = c

    def change_color(self, color):
        self.color = color

    def drive_to(self, destination):
        print(f"Машина: {self.make} едет в {destination}")


# Дочерние классы, подкласс, sub-class, наследный класс
class ElectricCar(Car):
    def __init__(self, wheels, b, c, battery):
        super().__init__(wheels, b, c)
        self.battery = battery

my_car1 = ElectricCar(3, 'blue', 'Mercedes', 500)
print(my_car1.battery, my_car1.color)

print(isinstance(my_car1, Car))
