import json


def load_books():
    """Загружает список книг из books.json"""
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    """Сохраняет список книг в books.json"""
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book(books):
    print("\nДобавление новой книги:")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()

    # Валидация оценки
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    date = input("Дата прочтения (например, 2025-03-20): ").strip()

    # Проверка дупликатов (автор + название)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Такая книга уже есть в списке.")
            return

    # Создание новой книги
    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    }

    # Сохранение новой книги в список books и books.json
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' добавлена!")


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
            books = load_books()
            add_book(books)

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