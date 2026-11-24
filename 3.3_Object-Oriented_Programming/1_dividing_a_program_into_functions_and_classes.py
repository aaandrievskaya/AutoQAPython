# 1. Прямоугольник 📐
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

# square = Rectangle(5, 5)

# print(square.area())
# print(square.perimeter())

# 2. Счётчик 🔢
class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value

# first = Counter(10)
# second = Counter()

# first.increment()

# print(first.get_value())
# print(second.get_value())

# 3. Банковский счёт 🏦
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

# account = BankAccount('Анна')

# account.deposit(1000)
# print(account.withdraw(300))
# print(account.get_balance())

# print(account.withdraw(800))
# print(account.get_balance())

# 4. Список задач ✅
class TodoList:
    def __init__(self):
        self.list_tasks = []

    def add_task(self, text):
        self.list_tasks.append(text)

    def remove_task(self, text):
        if text in self.list_tasks:
            self.list_tasks.remove(text) 
            return True
        else:
            return False

    def get_tasks(self):
        return self.list_tasks.copy()

# todo = TodoList()
# todo.add_task('Прочитать урок')

# tasks = todo.get_tasks()
# tasks.append('Посторонняя задача')

# print(todo.get_tasks())

# 5. Библиотека 📚
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f'{self.title} — {self.author}'

class Library:
    def __init__(self):
        self.list_of_books = []

    def add_book(self, book: Book):
        self.list_of_books.append(book)

    def find_by_author(self, author: Book):
        return [b.title for b in self.list_of_books if b.author.capitalize() == author.capitalize()]

# book = Book('Капитанская дочка', 'Александр Пушкин')
# print(book.get_info())

# library = Library()
# library.add_book(book)
# library.add_book(Book('Дубровский', 'Александр Пушкин'))
# library.add_book(Book('Мцыри', 'Михаил Лермонтов'))

# print(library.find_by_author('АЛЕКСАНДР ПУШКИН'))
# print(library.find_by_author('Николай Гоголь'))

# 6. Магазин: разделяем обязанности 🛒🌶️
class Product:
    def __init__(self, name, price: int):
            self.name = name
            self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.lines_check = []

    def add_product(self, product: Product, quantity=1):
        self.cart.append({product: quantity})

    def total(self):
        tot_price = 0
        for pr in self.cart:
            for k, v in pr.items():
                    tot_price += k.price * v
        return tot_price

    def get_lines(self):
        for pr in self.cart:
            for k, v in pr.items():
                self.lines_check.append(f'{k.name}: {k.price}  x {v} = {k.price * v}')
        
        return self.lines_check

def print_receipt(cart: ShoppingCart):
    lines = cart.get_lines()
    for line in lines:
        print(line)
    print(f'Итого: {cart.total()}')

bread = Product('Хлеб', 40)
milk = Product('Молоко', 80)

cart = ShoppingCart()
cart.add_product(bread, 2)
cart.add_product(milk)

print_receipt(cart)