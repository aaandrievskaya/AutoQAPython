# Количество аргументов
def count_args(*args):
    return len(args)

# print(count_args([1, 2, 3]))
# print(count_args([1, 2], 'текст', None, True))

# Сумма квадратов
def sq_sum(*args: int):
    sqs = [i**2 for i in args]
    return sum(sqs)

# print(sq_sum(1.5, 2))
# print(sq_sum(0, 0))
# print(sq_sum())

# Среднее арифметическое
def mean(*args):
    ints = [i for i in args if type(i) == int or type(i) == float]
    if len(ints) > 0:
        return sum(ints)/len(ints)
    else:
        return 0

# print(mean('10', [1, 2], None))
# print(mean())

# Приветствие
def greet(*args: str):
    return 'Hello, ' + ' and '.join(i for i in args) + '!'

# print(greet('Тимур'))
# print(greet('Тимур', 'Анна'))
# print(greet('Alice', 'Bob', 'Charlie'))

# Список продуктов
def print_products(*args):
    products = [arg for arg in args if type(arg) == str and arg.isalnum() == True]
    num = 1
    if len(products) == 0:
        print('Нет продуктов')
    else:
        for item in products:
            print(f'{num}) {item}')
            num += 1

# print_products('хлеб', 'хлеб', '0')

# Именованные аргументы
def info_kwargs(**kwargs):
    sorted_k = sorted(kwargs)
    for k in sorted_k:
        print(f'{k}: {kwargs[k]}')

info_kwargs(items=[1, 2], active=True, note=None)
info_kwargs()