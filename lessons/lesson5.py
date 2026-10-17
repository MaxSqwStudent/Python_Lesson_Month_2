# Множественное наследование

class Flying:
    @staticmethod
    def fly():
        print("i flying")

class Swimming:
    @staticmethod
    def swim():
        print("i swimming")

class Duck(Flying, Swimming):
    pass

duck = Duck()
duck.swim()
duck.fly()

