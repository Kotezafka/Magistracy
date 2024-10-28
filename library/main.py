from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, NoReturn, Dict, List, Any
from datetime import datetime


def log_operation(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - функция {func.__name__} начала выполнение")
        result = func(*args, **kwargs)
        print(f"{timestamp} - функция {func.__name__} завершила выполнение")
        return result

    return wrapper


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool = True
    categories: List[str] = Field(
        default_factory=list,
        description="Категории книги",
        min_items=1,
        max_items=5,
        example=["Fiction", "Fantasy"],
    )

    def __hash__(self):
        return hash(self.title)

    def is_book_borrow(self) -> bool:
        if not self.available:
            raise BookNotAvailable(f"Книга {self.title} занята\n")
        return False


class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, values: EmailStr):
        if values and "@gmail.com" not in values:
            raise ValueError(f"Некорректная почта {values}\n")
        return values


class BookNotAvailable(Exception):
    """Исключение, которое возникает, когда книга недоступна"""

    pass


class Library(BaseModel):
    books: List[Book] = []
    users: List[User] = []
    borrows: Dict[Any, User] = {}

    def __str__(self):
        return f"Зарегистрированные пользователи в библиотеке: {', '.join([u.name for u in self.users])}\nКниги в библиотеке: {', '.join([b.title for b in self.books])}"

    def add_book(self, book: Book) -> NoReturn:
        self.books.append(book)

    def find_book(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title == title:
                return book

    @log_operation
    def take_book(self, book: Book, user: User) -> NoReturn:
        if book.is_book_borrow():
            raise BookNotAvailable(f"Книга {book.title} занята")

        self.borrows[book] = user
        book.available = False
        print(f"Пользователь {user.name} из библиотеки взял книгу: {book.title}\n")

    def return_book(self, book: Book) -> NoReturn:
        user = self.borrows.pop(book)
        book.available = True
        print(f"Пользователь {user.name} в библиотеку вернул книгу: {book.title}\n")

    def total_books(self) -> int:
        return len(self.books)


def main():
    library = Library()

    book1 = Book(
        title="Война и мир",
        author="Лев Николаевич Толстой",
        year=1869,
        categories=["Fiction", "Historical Fiction"],
    )
    book2 = Book(
        title="Преступление и наказание",
        author="Фёдор Михайлович Достоевский",
        year=1866,
        categories=["Fiction", "Detective"],
    )

    library.add_book(book1)
    library.add_book(book2)

    try:
        user1 = User(
            name="Petrova Aleksandra Nikolaevna",
            email="alex_nikolaeva@gmail.com",
            membership_id="1",
        )
        user2 = User(
            name="Sinitsyn Anton Pavlovich",
            email="ant_pavlovich@tttgmail.com",
            membership_id="2",
        )
    except ValueError as e:
        print(e)

    library.users.append(user1)

    print(f"{library}\n")

    if library.find_book(title=book1.title) is None:
        print(f'Книга "{book1.title}" не найдена\n')
    else:
        print(f'Книга "{book1.title}" есть в библиотеке\n')

    try:
        book1.is_book_borrow()
    except Exception as e:
        print(e)

    print(f"Книги в библиотеке: {library.total_books()}\n")

    library.take_book(book=book1, user=user1)

    library.return_book(book=book1)

    print(f"{library}\n")

    print(f"Книги в библиотеке: {library.total_books()}\n")


if __name__ == "__main__":
    main()
