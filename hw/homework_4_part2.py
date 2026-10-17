class Library:
    def __init__(self, city, books = None):
        self.city = city
        self.books = books

    def __str__(self):
        return f"<Library object, city: {self.city}, books: {len(self.books)}>"

    def __len__(self):
        return len(self.books)

    def __contains__(self, book):
        print(f"Ищем книгу: {book}")
        return book in self.books

    def __bool__(self):
        return True if len(self.books) > 5 else False

lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])

print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)

if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")