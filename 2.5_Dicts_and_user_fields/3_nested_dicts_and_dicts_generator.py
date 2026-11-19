def task_1():
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    result = {v:k for k, v in months.items()}
    print(result)


def task_2():
    numbers = [-3, 6, 4, 76, 2, -1, 2]
    res = {k: numbers[k]**2 for k in range(len(numbers))}
    print(res)


def task_3():
    colors = {'b8': 'Grey', 'b9': None, 'a2': 'Green', 'a1': 'Black', 'c10': None, 'a6': 'Pink'}
    res = {k: v for k,v in colors.items() if v != None}
    print(res)


def task_4():
    favorite_numbers = {'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4,'manny': 4, 'ken': 8423, 'borya': 12}
    res = {k: v for k, v in favorite_numbers.items() if 10 < v <= 99 }
    print(res)


def task_5_i_am_stupid():
    s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'
    s_n = s.split()
    s_nn = []
    for i in s_n:
        k,v = i.split(':')
        s_nn.append(int(k))
        s_nn.append(v)
    res = {s_nn[i]: s_nn[i+1] for i in range(0, len(s_nn), 2)}

    print(res)

def task_5_i_am_smart():
    s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'
    res  = {int((i.split(':'))[0]): i.split(':')[1] for i in s.split()}
    print(res)

def task_6_i_am_stupid():
    numbers = [24, 5, 17, 9, 28, 84, 62]
    num_n_delit = []
    for item in numbers:
        delit = []
        for i in range(1, item+1):
            if item % i == 0:
                delit.append(i)
        it = [item, delit]
        num_n_delit.append(it)
    #res = {num_n_delit[i][0]: num_n_delit[i][1] for i in range(len(num_n_delit))} моё решение
    res = {i[0]: i[1] for i in num_n_delit} #ИИшкино решение №1
    #res = {k: v for k, v in num_n_delit} ИИшкино решение №охуеть, и так можно было!?))
    print(res)        

def task_6_i_am_smart():
    numbers = [24, 5, 17, 9, 28, 84, 62]
    res = {item: [i for i in range(1, item+1) if item % i == 0] for item in numbers}
    print(res)  

def task_7_i_am_stupid():
    words = ['кошка', 'собака', 'мышь']
    wordsASCII = []
    for word in words:
        v = [ord(i) for i in word]
        it = [word, v]
        wordsASCII.append(it)
    res = {k:v for k, v in wordsASCII}
    print(res)

def task_7_resolved_by_AI():
    words = ['кошка', 'собака', 'мышь']
    # на этой задаче я решила свериться с ИИ и мне пришло озарение что выше все решено не так
    result = {word: [ord(i) for i in word] for word in words}
    print(result)


def task_8():
    letters = {4: 'К', 65: 'Щ', 12: 'П', 41: 'М', 36: 'У'}
    remove_keys = [12, 65, 14, 37]

    res = {k: v for k, v in letters.items() if k not in remove_keys}
    print(res)


def task_9():
    students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}

    res = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
    print(res)


def task_10():
    tuples = [(41, 52, 14), (12, 3, 4), (2, 77, 14), (-2, 4, -9)]

    res = {i[0]: (i[1:3]) for i in tuples}
    print(res)


def task_11():
    student_ids = ['X142', 'B065', 'X144']
    student_grades = [88, 85, 62]
    student_names = ['Nikita Karpov', 'Anna Chernova', 'Ruslan Magarov']

    d = [{i: {name: grade}} for i, name, grade in zip(student_ids, student_names, student_grades)]
    print(d)

if __name__ == "__main__":
    #task_1()
    #task_2()
    #task_3()
    #task_4()
    #task_5_i_am_stupid()
    #task_5_i_am_smart()
    #task_6_i_am_stupid()
    #task_6_i_am_smart()
    #task_7_i_am_stupid()
    #task_7_resolved_by_AI()
    #task_8()
    #task_9()
    task_10()
    #task_11()

