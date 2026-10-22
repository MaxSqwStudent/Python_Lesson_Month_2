import sqlite3 as sql

def create_tables(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS students
    (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    ''')

def add_student(conn, name, age, city):
    conn.execute('''
    INSERT INTO students(name, age, city)
        VALUES (?, ?, ?)
    ''', (name, age, city))
    conn.commit()


def delete_student_by_name(conn, name):
    conn.execute('''
        DELETE FROM students WHERE name = ?
    ''', (name,))
    conn.commit()

def delete_student_by_age(conn, student_id):
    conn.execute('''
        DELETE FROM students WHERE id = ?
        ''', (student_id,)
                 )
    conn.commit()

def get_all_students(conn):
    cursor = conn.cursor()
    result = cursor.execute('''
        SELECT name, id FROM students
    ''', ())
    return result.fetchmany(2)


    # result = cursor.execute('''
    #         SELECT name, id FROM students
    #     ''', ())
    #     return result.fetchall()

def get_student(conn, student_id):
    cursor = conn.cursor()
    result = cursor.execute('''
        SELECT * FROM students WHERE id = ?
    ''', (student_id,))
    return result.fetchone()

def get_students_by_age(conn, age):
    cursor = conn.cursor()
    result = cursor.execute('''
        SELECT * FROM students WHERE id <= ?
    ''', (age,))
    return result.fetchall()



if __name__ == "__main__":
    connection = sql.connect("database.db")
    create_tables(connection)
    add_student(connection, "Max", 25, "Bishkek")
    add_student(connection, "Arzy", 43, "Almaty")
    all_students = get_all_students(connection)
    for student in all_students:
        print(student)

    print("___________________________")
    print("___________________________")
    print("___________________________")
    print("___________________________")

    student = get_student(connection, 11)
    print(student)

    print("___________________________")
    print("___________________________")
    print("___________________________")

    students_by_age = get_students_by_age(connection, 10)
    print(students_by_age)

    connection.close()

