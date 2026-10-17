class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu = f'Высшее образование есть' if self.higher_education else 'Высшего образования нету'
        print(f"Меня зовут {self.name}, я родился в {self.birth_date}., по профессии я {self.occupation}, {edu} ")

person1 = Person("Max", 2002, "Технарь", False)
person2 = Person("Alex", 2005, "Учитель", True)
person3 = Person("Кундуз", 2004, "ИП", False)

person1.introduce()
person2.introduce()
person3.introduce()