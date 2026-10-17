TRIP_COST = 20

class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, money):
        if money > 0:
            self.__balance += money
        else:
            print(f"{self.__owner}, Сумма пополнения должна быть положительной")

    def pay_for_trip(self):
        if self.__balance > TRIP_COST:
            self.__balance -= TRIP_COST
        else:
            print(f"{self.__owner}, у вас недостаточно средств на поездку.\n"
                  f"Ваш баланс: {self.__balance} монет")


card1 = TransportCard("Максат")
card2 = TransportCard("Айгерим")

card1.add_money(100)

print(f"Владелец карты card1: {card1.get_owner()}, баланс: {card1.get_balance()}")
print(f"Владелец карты card2: {card2.get_owner()}, баланс: {card2.get_balance()}")

card1.pay_for_trip()
print(f"После поездки карты card1: {card1.get_owner()}, баланс: {card1.get_balance()}")

card1.add_money(-50)