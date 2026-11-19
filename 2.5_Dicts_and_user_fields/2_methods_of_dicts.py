def task_1():
    d = {}
    for i in range(1, 15 + 1):
        d[i] = i**2
    print(d)    

def task_2():
    dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
    dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
    for k in dict2:
        var = dict1.setdefault(k) # либо значение None, либо значение существующей пары
        if var == None:
            dict1[k] = dict2[k]
        else:
            dict1[k] = dict1[k] + dict2[k]
    print(dict1)

def task_3():
    text = 'Для торжества зла достаточно лишь бездействия хороших людей.'
    symbols = set(text)
    d ={}
    dic = d.fromkeys(symbols, 0)
    for t in text:
        dic[t] += 1
        
    print(dic)


def task_4():
    text = 'coat pencil guy tree tree pause power sand apple song taxi tree coat coat pause pause'
    words = set(text.split())
    d ={}
    dic = d.fromkeys(words, 0)
    for w in text.split():
        dic[w]+= 1
    q=0
    l=[]
    for k,v in dic.items():
        if v > q:
            q = v
            l.clear()
            l.append(k)
        elif v == q:
            l.append(k)
    l.sort()
    print(*l)

def task_5():
    pets = [
#(кличка питомца, имя владельца, фамилия владельца, возраст владельца).
('Барсик', 'Маша', 'Петрова', 17),
('Джек', 'Галина', 'Лагунова', 45),
('Муся', 'Александр', 'Каракулов', 28),
('Буся', 'Маша', 'Петрова', 17),
('Кира', 'Вова', 'Пухарев', 54),
]
#     pets = [
# ('Freddie', 'Jessica', 'Brown', 38),
# ('Freya', 'Jessica', 'Brown', 38),
# ('Chernysh', 'Harry', 'Wonn', 20),
# ('Kesha', 'Harry', 'Wonn', 20),
# ('Patrick', 'Hermann', 'Schulz', 72),
# ('Foxya', 'Julia', 'Alikina', 47),
# ('Thomas', 'Julia', 'Alikina', 47),
# ('Mia', 'Nikolai', 'Lagunov', 39),
# ('Rufus', 'Harry', 'Wonn', 20),
# ]
    dic = {}
    for item in pets:
        key = (item[1:])
        if key not in dic:
            dic[key] = [item[0]]          
        else:
            dic[key].append(item[0])
    print(dic)


def slovar_programmista():
    n = int(input())
    slovar = [input() for _ in range(n)]

    dic ={}
    for item in slovar:
        k, v = item.split(': ', 1)
        dic[k.lower()] = v

    m = int(input())
    termins = [input().lower() for _ in range(m)]

    for ter in termins:
        if ter in dic:
            print(dic[ter])
        else:
            print('Не найдено')



def anagrami_slova():
    a = input()
    b = input()
    a_d= {}
    b_d = {}
    for i in set(a):
        a_d[i] = a.count(i)
    for i in set(b):
        b_d[i] = b.count(i)

    if (a_d) == (b_d):
            print('YES')
    else:
            print('NO')


def anagrami_predlozheniya():
    a = input()
    b = input()
    a = list(a)
    b = list(b)

    a_res = []
    for i in a:
        if i.isalpha() == True:
            a_res.append(i.lower())
    b_res = []
    for i in b:
        if i.isalpha() == True:
            b_res.append(i.lower())

    a_dict = {}
    b_dict = {}
    for s in set(a_res):
        a_dict[s] = a_res.count(s)
    for s in set(b_res):
            b_dict[s] = b_res.count(s)

    if (a_dict) == (b_dict):
        print('YES')
    else:
        print('NO')

def slovar_sinonimov():
    n = int(input())
    slovar = [input() for _ in range(n)]
    isk = input()
    dict_slovar = {}
    for item in slovar:
        k, v = item.split()
        dict_slovar[k] = v

    if isk in dict_slovar.keys():
        print(dict_slovar[isk])
    elif isk in dict_slovar.values():
        for k, v in dict_slovar.items():
            if v == isk:
                print(k)

def strani_i_goroda():
    n = int(input())
    sprav = [input() for _ in range(n)]
    m = int(input())
    request = [input() for _ in range(m)]

    slovar = {}
    for item in sprav:
        k, v = item.split(' ', 1)
        v = v.split()
        slovar[k] = v


    for i in request:
        for k, v in slovar.items():
            for gorod in v:
                if gorod == i:
                    print(k)
                


def telefonnaya_kniga():
    n = int(input())
    phones = [input() for _ in range(n)]
    m = int(input())
    requests = [input() for _ in range(m)]

    book = {}
    for item in phones:
        v, k = item.split()
        k = k.capitalize()
        if k not in book:
            book[k] = [v]
        else:
            book[k].append(v)

    for item in requests:
        if item.capitalize() in book.keys():
            print(*book[item.capitalize()])
        else:
            print('абонент не найден')
          


def secretnoe_slovo():
    sec = input()
    n = int(input())
    slovar = [input() for _ in range(n)]

    dic_transcrib = {}
    for item in slovar:
        k, v = item.split(': ')
        dic_transcrib[k] = int(v)

    symbols_sec = set(list(sec))
    dic_chipher = {}
    for sym in symbols_sec:
        dic_chipher[sym] = list(sec).count(sym)

    dic_res = {}
    for k1,v1 in dic_chipher.items():
        for k2,v2 in dic_transcrib.items():
            if v1 == v2:
                dic_res[k1] = k2
    res = []
    for i in list(sec):
        res.append(dic_res[i])

    print(''.join(res))





if __name__ == "__main__":
    #task_1()
    #task_2()
    #task_3()
    #task_4()
    #task_5()
    #slovar_programmista()
    #anagrami_slova()
    #anagrami_predlozheniya()
    #slovar_sinonimov()
    #strani_i_goroda()
    telefonnaya_kniga()
    #secretnoe_slovo()
