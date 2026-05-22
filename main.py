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
            add_book(books)
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