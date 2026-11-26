# 1. Защищаем баланс 🔒
class Wallet:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def spend(self, amount):
        if amount > 0 and self._balance - amount >= 0:
            self._balance -= amount
            return True
        else:
            return False

# wallet = Wallet()

# try:
#     wallet.balance = 100
# except AttributeError:
#     print('Баланс нельзя присвоить напрямую')

# 2. Сотрудник и менеджер 👩‍💼
class Employee:
    def __init__(self, name, sallary):
        self.name = name
        self.sallary = sallary

    def get_payment(self):
        return self.sallary

class Manager(Employee):
    def __init__(self, name, sallary, bonus):
        super().__init__(name,sallary)
        self.bonus = bonus

    def get_payment(self):
        return self.sallary + self.bonus

# manager = Manager('Борис', 60000, 0)

# print(manager.get_payment())
# print(isinstance(manager, Employee))

# 3. Голоса животных 🐈🐕
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'Неизвестный звук'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f'Мяу'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f'Гав'

def collect_voices(animals):  
    return [f'{item.name}: {item.speak()}' for item in animals]

# animals = [
#     Cat('Мурка'),
#     Dog('Шарик'),
#     Animal('Неизвестный')
# ]

# print(collect_voices(animals))

# 4. Площади фигур 📐
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def total_area(shapes):
    l_areas = [item.area() for item in shapes]
    return sum(l_areas)

# try:
#     shape = Shape()
# except TypeError:
#     print('Нельзя создать абстрактную фигуру')

# 5. Общий интерфейс без наследования 🔔

class EmailNotifier:
    def send(self, message):
        return f'Email: {message}'

class SmsNotifier:
    def send(self, message):
        return f'SMS: {message}'

def notify_all(notifiers, message):
    return [item.send(message) for item in notifiers]

# notifiers = [EmailNotifier(), SmsNotifier()]

# print(notify_all(notifiers, 'Заказ готов'))

# 6. Заказ и доставка 🚚🌶️
class Pickup:
    def calculate(self, subtotal):
        return 0

class CourierDelivery:
    def calculate(self, subtotal):
        if subtotal >= 1000:
            return 0
        elif 1000 > subtotal > 0:
            return 200

class Order:
    def __init__(self, delivery):
        self.delivery = delivery
        self.l_prices = []

    def add_item(self, price):
        self.l_prices.append(price)

    def subtotal(self):
        return sum(self.l_prices)

    def total(self):
        if self.subtotal() > 0:
            return self.delivery.calculate(self.subtotal()) + self.subtotal()
        else:
            return 0

    def set_delivery(self, delivery):
        self.delivery = delivery

# order = Order(CourierDelivery())
# order.add_item(1000)

# print(order.total())

# 7. Добавляем новый способ доставки 🧩
class FixedDelivery:
    def __init__(self, fee):
        self.fee = fee

    def calculate(self, subtotal):
        return self.fee

order = Order(FixedDelivery(350))

print(order.total())

order.add_item(1000)
print(order.total())
