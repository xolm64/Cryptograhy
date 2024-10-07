from books import Book
from users import User
from libraries import Library


library1 = Library(name="Library #1")

book1 = Book(title="Harry Potter", author="J.K. Роулинг", year=1997, genre='fantasy')
book2 = Book(title="The Blind Assasin", author="Margaret Atwood", year=2005, genre="blockbuster")
book3 = Book(title="War and Peace", author="Leo Tolstoy", year=1869, genre='novel')
book4 = Book(title="1984", author="George Orwell", year=1949,genre='novel')
book5 = Book(title="One Hundred Years of Solitude", author="Gabriel", year=1967, genre='drama')

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_book(book5)


user1 = User(username="bookworm")
print("Добро пожаловать в библиотеку!")

main_menu = ("\nМеню:\n"
             "1. Доступные книги\n"
             "2. Взять книгу\n"
             "3. Мои книги\n"
             "4. Поиск по жанру\n"
             "q. Выход")


while True:

    print(main_menu)

    user_input = input("Ваш выбор: ")

    if user_input == "1":
        print("Вы выбрали показ доступных книг!")

        available_books = library1.get_available_books()

        for book in available_books:
            print(book)
    elif user_input == "4":
        print("Вы выбрали поиск книг по жанру")
        result_find = input("введите один из жанров: fantasy, blockbuster, novel, drama \n")
        result1 = library1.find_genre(result_find)
        for book in result1:
            print(book)


    elif user_input == 'q':
        break









