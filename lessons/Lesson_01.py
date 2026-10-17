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



my_car1 = Car(3, 'blue', 'Mercedes')
print(my_car1.wheels, my_car1.color)

my_car2 = Car(2, 'red', 'Honda')
print(my_car2.wheels, my_car2.color)

my_car2.change_color("black")

print(my_car2.wheels, my_car2.color)

my_car1.drive_to("Казань")

class Passport:
    def __init__(self, surname, name, birth_year, current_year):
        self.surname = surname
        self.name = name
        self.birth_year = birth_year
        self.age = current_year - birth_year


    def print_passport(self):
        print(f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"Год рождения: {self.birth_year}\n"
              f"Возраст {self.age}\n")

maksat = Passport("Sarkulov", "Maksat", 2002, 2026)

maksat.print_passport()