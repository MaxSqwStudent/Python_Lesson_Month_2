class Person:
    def __init__(self, name, birth_date, occupation, higher_education=None):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Меня зовут {self.name}, я родился в {self.birth_date}., по профессии я {self.occupation}, {'Высшее образование есть' if self.higher_education == True else 'Высшего образования нету'} ")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name, friend_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник {self.friend_name}, я родился {self.birth_date}, работаю {self.occupation}")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby, friend_name):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby
        self.friend_name = friend_name


    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.friend_name}, я родился {self.birth_date}, работаю {self.occupation}")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, friend_name, shared_memory):
        super().__init__(name, birth_date, occupation, hobby, friend_name)
        self.shared_memory = shared_memory

    def introduce(self):
        print("\n")
        super().introduce()
        print(f"Наше общее воспоминание с {self.friend_name}: {self.shared_memory}")


person1 = Person("Максат", 2002, "Технарь", False)

person1.introduce()

classmate1 = Classmate("Дастан", "12.02.1990", "Программистом", "71-1B", "Максат")
classmate2 = Classmate("Азирет", "18.04.1999", "Таксистом", "71-1B", "Максат")

friend1 = Friend("Сыймык", "11.01.2001", "Геодезистом", "Гольф", "Максат")
friend2 = Friend("Бегимай", "17.07.2006", "Дизайнером", "Рукоделие", "Максат")

best_friend= BestFriend("Нурсултан", "15.05.2005", "Механиком", "Фильмы", "Максат", "Мы дружили с садика")


users = [classmate1, classmate2, friend1, friend2, best_friend]


for i in users:
    i.introduce()

