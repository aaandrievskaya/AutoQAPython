#функция с match-case
def get_day_name(day: int) -> str:
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Неверный день недели"

#список и цикл
numbers = list(range(1, 10))    # девять чисел: 1…9
max_value = numbers[0]

for n in numbers:
    if n > max_value:
        max_value = n
print(f"Максимум: {max_value}")    # 9
# max(), sorted() и сортировка «чтобы взять последний» здесь не используются

#цикл с break
for n in list(range(1, 8)):
    print(n)
    if n == 5:
        break

#List comprehension
words = [f"str{i}" for i in range(10)]
print(words)                         # ['str0', 'str1', ..., 'str9']

long_words = [word for word in words if len(word) > 5]
print(long_words)

######################################################################
import random
import time

def simulate_load():
    STEPS_COUNT = 10 
    UP_INT_LIMIT = 100 
    LOW_INT_LIMIT = 0 
    LOAD_THRESHOLD = 85 #порог нагрузки
    PAUSE_SECONDS = 0.2
    for i in range(STEPS_COUNT):
        load_value = random.randint(LOW_INT_LIMIT, UP_INT_LIMIT)
        if load_value > LOAD_THRESHOLD:
            print(f"Предупреждение: нагрузка {load_value} превышает порог!")
        else:
            print(f"Нагрузка {load_value}, все ОК.")
        time.sleep(PAUSE_SECONDS)

simulate_load()



