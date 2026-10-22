import sqlite3

def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books(
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER)
    """)
    connection.commit()

def insert_books(connection, name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute("""
        INSERT INTO books(name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre, number_of_pages, number_of_copies))
    connection.commit()

def get_books_by_author(connection, author):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM books WHERE author = ?
    """, (author,))
    return cursor.fetchall()

def delete_books_by_author(connection, author):
    connection.execute("""
        DELETE FROM books WHERE author = ?
    """, (author,))
    connection.commit()

if __name__ == '__main__':
    connection = sqlite3.connect('database.db')

    create_table(connection)

    insert_books(connection, "Гарри поттер", "Роалинг чето там", 2000, "Фантастика", 500, 1000000)
    insert_books(connection, "Гарри поттер 2", "Роалинг чето там", 2003, "Фантастика", 510, 2000000)
    insert_books(connection, "Гарри поттер 3", "Роалинг чето там", 2005, "Фантастика", 550, 3000000)
    insert_books(connection, "Гарри поттер 4", "Роалинг чето там", 2006, "Фантастика", 700, 1055000)
    insert_books(connection, "Гарри поттер 5", "Роалинг чето там", 2008, "Фантастика", 800, 10052000)
    insert_books(connection, "Гарри поттер 6", "Роалинг чето там", 2010, "Фантастика", 400, 1002400)
    insert_books(connection, "Гарри поттер 7", "Роалинг чето там", 2012, "Фантастика", 550, 4000440)
    insert_books(connection, "Гарри поттер 8", "Роалинг чето там", 2013, "Фантастика", 570, 2000000)
    insert_books(connection, "Гарри поттер 9", "Роалинг 222", 2015, "Фантастика", 390, 88000000)

    books = get_books_by_author(connection, "Роалинг чето там")
    for book in books:
        print(book)

    delete_books_by_author(connection, "Роалинг чето там")

    connection.close()