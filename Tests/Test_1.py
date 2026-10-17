class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age


class Dog(Animal):
    def make_sound(self):
        print("Dog sound: GAF!")

class Cat(Animal):
    def make_sound(self):
        print("Cat sound: Мяу!")


dog = Dog("Актош", 5)
cat = Cat("Мурка", 3)

dog.make_sound()
cat.make_sound()

print(f"Имя собачки: {dog.get_name()}")
print(f"Имя кошки: {cat.get_name()}")

dog.set_age(20)
cat.set_age(20)

print(f"Новый возраст собачки: {dog.get_age()}")
print(f"Новый возраст кошки: {cat.get_age()}")