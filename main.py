import json


def load_books():
    """Загружает список книг из books.json"""
    pass


def save_books(books):
    """Сохраняет список книг в books.json"""
    pass


def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("Добавление книги (заглушка)")
        elif choice == "2":
            print("Список книг (заглушка)")
        elif choice == "3":
            print("Средняя оценка (заглушка)")
        elif choice == "4":
            print("Статистика по авторам (заглушка)")
        elif choice == "5":
            print("Удаление книги (заглушка)")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()