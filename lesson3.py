class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        # атрибуты с __ называются приватные
        self.__password = password
        # атрибуты с _ называются защищенные
        self._balance = balance

    def get_balance(self, user_login, user_password):
        if self.login == user_login and self.__password == user_password:
            return self._balance
        return "Не верный логин или пароль"

    def __reset_pass(self):
        self.__password = "1234"
        return f"{self.login} Пароль сброшен, новый пароль 1234"

    def new_pass(self, old_pass):
        if old_pass == self.__password:
            return self.__reset_pass()
        return "Пароль неверный"




ardager = BankAccount(login='Max', password='123', balance=1000)

print(ardager.get_balance('Max', '123'))

print(ardager.new_pass('123'))


from abc import ABC, abstractmethod # декораторы

# Абстрактный класс
class Animal(ABC):
    # @abstractmethod - декораторы
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def voce(self):
        pass

class Dog(Animal):
    def move(self):
        print("Step")
    def voce(self):
        print("Gav Gav")

class Cat(Animal):
    def move(self):
        print("Step")
    def voce(self):
        print("Mew Mew")

gufi = Dog()