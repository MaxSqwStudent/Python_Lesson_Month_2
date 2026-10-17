class Test:
    # Атрибут класса
    class_names = "TEST"
    # Магический метод
    def __init__(self, value):
        #атрибуты экземпляра или объекта класса
        self.value = value

    def __str__(self):
        return str(self.value)


    def __add__(self, other):
        return self.value + other.value

    def __call__(self, *args, **kwargs):
        print("Меня вызвали " + str(self.value))
        print(kwargs.get("k"))

    def __getitem__(self, item):
        return self.value[item]

    #Статикметод просто действует как функция внутри класса, не использует объект
    @staticmethod
    def add(a, b):
        return a + b
    # использует атрибуты класса, а не атрибуты объекта
    @classmethod
    def class_name(cls):
        return cls.class_names


obj1 = Test(123)
obj2 = Test(321)

test_value = 1234

print(test_value)

print(obj1)
obj1(k=234234)

obj3 = Test([1,2,3,4,5,6,7])

print(obj3[3])

print(Test.class_name())
print(Test.add(1,1))

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

maksat = User("Max", "Smith")
print(maksat.full_name)