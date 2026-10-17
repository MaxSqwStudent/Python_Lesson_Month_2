def open_vault(password, money):
    print("Сейф открыт!")
    return f"Забирайте {money} сом"

def password_guard(name_func):
    SECRET_PASSWORD = "kitty_2007"

    def check_password(password, money):
        if password == SECRET_PASSWORD:
            return name_func(password, money)
        else:
            print("🚨 СИГНАЛИЗАЦИЯ! Доступ запрещён")
            return None

    return check_password



open_vault = password_guard(open_vault)


print(open_vault("123", 100))

print(open_vault("kitty_2007", 2134))