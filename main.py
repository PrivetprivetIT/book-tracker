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


def show_books(books):
    """Показывает список всех книг"""
    if not books:
        print("\nСписок книг пуст.")
        return
    print("\nСписок прочитанных книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} — {book['title']} (оценка: {book['rating']}, дата: {book['date']})")


def average_rating(books):
    """Показывает среднюю оценку всех книг"""
    if not books:
        print("\nНет книг для расчёта средней оценки.")
        return
    total = sum(book['rating'] for book in books)
    avg = total / len(books)
    print(f"\nСредняя оценка всех книг: {avg:.2f}")


def author_stats(books):
    """Показывает количество книг каждого автора"""
    if not books:
        print("\nНет книг для статистики по авторам.")
        return
    stats = {}
    for book in books:
        author = book['author']
        stats[author] = stats.get(author, 0) + 1
    print("\nСтатистика по авторам:")
    for author, count in stats.items():
        print(f"{author}: {count} книг(а)")


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
            show_books(books)
        elif choice == "3":
            average_rating(books)
        elif choice == "4":
            author_stats(books)
        elif choice == "5":
            print("Удаление книги (заглушка)")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()