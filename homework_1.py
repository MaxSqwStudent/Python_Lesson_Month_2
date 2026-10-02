class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Меня зовут {self.name}, я родился в {self.birth_date}., по профессии я {self.occupation}, {'Высшее образование есть' if self.higher_education == True else 'Высшего образования нету'} ")

person1 = Person("Max", 2002, "Технарь", False)
person2 = Person("Alex", 2005, "Учитель", True)
person3 = Person("Кундуз", 2004, "ИП", False)

person1.introduce()
person2.introduce()
person3.introduce()