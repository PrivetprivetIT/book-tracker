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


def delete_book(books):
    if not books:
        print("\nНет книг для удаления.")
        return
    print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} — {book['title']}")
    try:
        idx = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= idx < len(books):
            removed = books.pop(idx)
            save_books(books)
            print(f"Книга '{removed['title']}' удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")


def main():
    books = load_books()
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
            delete_book(books)
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()