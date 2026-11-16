def task_1():
    my_dict = {0.5: 'apple', 2: 'banana', -3.57: 'orange'}
    print(min(my_dict) + max(my_dict))

def task_2():
    users = [
{'name': 'Hank', 'phone': '124-3818', 'email': 'hank@gmail.com'},
{'name': 'Petr', 'phone': '555-1618', 'email': 'helga@mail.net'},
{'name': 'Sasha', 'phone': '449-3141', 'email': ''},
{'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
{'name': 'Maria','phone': '12-129-3149','email': 'm.shark@yandex.ru','city': 'Pskov'},
{'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
{'name': 'Tony','phone': '242-449-3878','email': 'tony.ggg@mail.ru','birth_year': 1111},
]
    p=[]
    for user in users: 
        if user['phone'][-1] == '8':
            p.append(user['name'])
    p.sort()
    print(*p)

def task_3():
    users = [
{'name': 'Andrew', 'email': 'and@gmail.com'},
{'name': 'Tim', 'phone': '555-1618', 'email': 'tim-tim@yandex.ru'},
{'name': 'Olivia', 'phone': '449-3141', 'email': ''},
{'name': 'Vika', 'phone': '547-2123', 'email': 'Viko4ka@gmail.com'},
{'name': 'Kate', 'surname': 'Maltseva', 'city': 'Vologda'},
]
    p =[]
    for user in users:
        if user.get('email') in ('', None):
            p.append(user['name'])
    p.sort()
    print(*p)

def strokovoe_predstavlenie():
    nums = {0:'zero', 1: 'one', 2:'two', 3: 'three', 4:'four', 5: 'five', 6:'six', 7: 'seven', 8:'eigh', 9: 'nine'}
    n = input()
    q=[]
    for i in n:
        if int(i) in nums:
            q.append(nums[int(i)])  
    print(*q)

def informaciya_ob_uchebnih_kursah():
    courses = [
    {"course": "CS101", "room": "3004", "teacher": "Хайнс", "time": "8:00"},
    {"course": "CS102", "room": "4501", "teacher": "Альварадо", "time": "9:00"},
    {"course": "CS103", "room": "6755", "teacher": "Рич", "time": "10:00"},
    {"course": "NT110", "room": "1244", "teacher": "Берк", "time": "11:00"},
    {"course": "CM241", "room": "1411", "teacher": "Ли", "time": "13:00"}
]
    c = input()
    for i in range(len(courses)):
        if c == courses[i]['course']:
            print(f'{courses[i]['course']}: {courses[i]['room']}, {courses[i]['teacher']}, {courses[i]['time']}')

def nabor_soobcheniy():
    keypad = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " ",
}
    #Наверное это хуйня, но важно, что хуйня рабочая! Сгенерированная моим собственным интеллектом!
    s = input()
    res = []
    for lit in s: #перебираем буквы в сообщении
        for i in keypad: #перебираем ключи в словаре
            if lit.upper() in keypad[i]: #если буква есть в значении элемента-пары
                for j in range(len(keypad[i])): #перебираем символы в значении элемента-пары
                    if lit.upper() == keypad[i][j]: #если буква в сообщении совпадает с символом в значении элемента-пары
                        res.append(i*(j+1)) #добавляем ключ в список в том количестве, 
                                            #на позиции которой находится буква в значении элемента-пары (начиная с 1)
    print(''.join(res))

    #А вот это уже ИИшная помощь 
def nabor_soobcheniy_with_AI():
    keypad = {
            "1": ".,?!:",
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ",
            "0": " ",
    }
    
    s = input().upper()  # Сразу перевели всю строку в верхний регистр один раз!
    res = []
    
    for lit in s:
        for key, letters in keypad.items(): 
            if lit in letters:
                # find() сразу возвращает индекс от 0. Прибавляем 1 — получаем кол-во нажатий:
                count = letters.index(lit) + 1
                res.append(key * count)
                break  # Нашли букву — нет смысла проверять остальные кнопки!
                
    print(''.join(res))

def kod_morze():
    morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

    s = input().upper()
    res =[]
    for symbol in s:
        for k, v in morse_code.items():
            if symbol == k:
                res.append(v)
    print(' '.join(res))


    

if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    #strokovoe_predstavlenie()
    #informaciya_ob_uchebnih_kursah()
    #nabor_soobcheniy()
    #nabor_soobcheniy_with_AI()
    kod_morze()
