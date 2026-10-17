import sqlite3 as sql

# def create_tables(conn):
#     conn.execute('''
#     CREATE TABLE IF NOT EXISTS students
#     (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         age INTEGER,
#         city TEXT
#     )
#     ''')
#
# def add_student(conn, name, age, city):
#     conn.execute('''
#     INSERT INTO students(name, age, city)
#         VALUES (?, ?, ?)
#     ''', (name, age, city))
#     conn.commit()
#
# if __name__ == "__main__":
#     connection = sql.connect("database.db")
#     create_tables(connection)
#     add_student(connection, "Max", 25, "Bishkek")
#     add_student(connection, "Arzy", 43, "Almaty")
#
#
#     connection.close()

import sqlite3 as sql

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
        """)

def create_products_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price INTEGER
        )
        """)


def add_product(cursor, name, price):
    cursor.execute("""
        INSERT INTO products (title, price)
        VALUES (?, ?)
        """, (name, price))

def get_all_products(cursor):
    cursor.execute("""
        SELECT * FROM products
        """)
    all_products = cursor.fetchall()
    return all_products

def get_one_product(cursor):
    cursor.execute("""
        SELECT * FROM products
        """)
    one_product = cursor.fetchone()
    return one_product


if __name__ == '__main__':
    with sql.connect("database.db") as connection:
        cursor = connection.cursor()
        create_table(cursor)
        create_products_table(cursor)
        add_product(cursor, "шашлык", 40)
        add_product(cursor, "Планета", 0)

        all_products = get_all_products(cursor)
        for i in all_products:
            print(f"ID: {i[0]} | Название: {i[1]} | Цена: {i[2]}")

        one_product = get_one_product(cursor)
        print(f"1 Продукт: Название - {one_product[1]}, цена {one_product[2]}")




    connection.close()
