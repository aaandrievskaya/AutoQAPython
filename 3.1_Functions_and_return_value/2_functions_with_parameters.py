#FIO
def print_fio(name, surname, patronymic):
    print(surname[0].capitalize()+name[0].capitalize()+patronymic[0].capitalize())

#print_fio('семён','иванов', 'петрович')

#summa_cifr
def print_digit_sum(num): 
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)

num = 127
#print_digit_sum(num)

#zvezdni_treugolnik
def draw_triangle(fill, base): 
    q = base
    for i in range(base):
        if i < q:
            print(fill * (i+1))
            q -= 1
        else:
            q -= 1
            print(fill * (q+1))

#draw_triangle('*', 7)

#v_kakoe_vremya_sozvon
def print_perm_time_call(msc_time): 
    h_m_msk = msc_time.split(':')
    h_prm = int(h_m_msk[0]) + 2
    print(f'Созвон будет в {h_prm}:{h_m_msk[1]}.')

# print_perm_time_call('09:12')

# Замена омоглифов
def replace_homoglyphs(text):
    homoglyphs = {
    'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а',
    'ʍ': 'м', 'ʙ': 'в', 'Φ': 'Ф', 'k': 'к', 'x': 'х',
    'c': 'с', 'E': 'Е', 'T': 'Т', 'ȹ': 'ф', 'Ͷ': 'И',
    'ʜ': 'н', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н',
    'K': 'К', 'Ƅ': 'ь', 'ͷ': 'и', 'ɯ': 'ш', 'X': 'Х',
    'C': 'С', 'B': 'В', 'M': 'М', 'π': 'п', '3': 'З',
    'Γ': 'Г', 'ʮ': 'ч'}
    new_text = []
    for i in text:
        if i in homoglyphs.keys():
            new_text.append(homoglyphs[i])
        else:
            new_text.append(i)
    print(''.join(new_text))

# replace_homoglyphs('πͷрамͷдkа №3') # Требуется только реализовать функцию. Но я проверила

# Индексы символов
def transform(text):
    slov = {}
    for i in range(len(text)):
        slov.setdefault(text[i], set()).add(i)
    print(slov)

# transform('banana') # Требуется только реализовать функцию. Но я проверила

# Проверка доступа
def is_access_allowed(ip_address, mode, ip_access_lists):
    if mode == 1:
        if ip_address not in ip_access_lists['black list']:
            print('ДА')
        else:
            print('НЕТ')
    if mode == 2:
        if ip_address not in ip_access_lists['white list']:
            print('НЕТ')
        else:
            print('ДА')

# is_access_allowed("192.0.2.1", 1, {
#     'black list': ['192.0.2.1'],
#     'white list': []
# })
# is_access_allowed('192.0.2.2', 1, {
#     'black list': ['192.0.2.1'],
#     'white list': []
# })
# is_access_allowed("192.0.2.1", 2, {
#     'black list': ['192.0.2.1'],
#     'white list': ['192.0.2.1']
# })
# is_access_allowed("192.0.2.2", 2, {
#     'black list': [],
#     'white list': ['192.0.2.1']
# })

# Строка запроса
def add_query_string(url, query):
    print(f'{url}?' + '&'.join(f'{k}={v}' for k,v in query.items()))

# add_query_string("https://example.com", {'page': 1, 'per': 5, 'sort': True})

# Список продуктов 
def print_product_list(product_list):
    dict_emoji = {'яблоко': '🍎','хлеб': '🍞','конфеты': '🍬','лимон': '🍋','морковь': '🥕','огурец': '🥒','помидор': '🍅','яйцо': '🥚',
    'чеснок': '🧄','авокадо': '🥑','спички': '🥢','соль': '🧂','филе говядины': '🥩','киви': '🥝','лук': '🧅','сыр': '🧀',}
    to_shop = {}
    for item in product_list:
        if item in dict_emoji:
            to_shop.setdefault(dict_emoji[item], +1)
        else:
            to_shop.setdefault(item, +1)
    print(to_shop)

# print_product_list(['яблоко', 'хлеб', 'яблоко', 'молоко', 'хлеб'])

# Собери слово
def scrabble(letters, word):
    chars = list(letters.lower())
    res = True
    for i in range(len(word)):
        if word[i].lower() in chars:
            chars.remove(word[i].lower())
        else:
            res = False
            print(res)
            break
    if res != False:
        print(res)

# scrabble('мамкот', 'мма')

# Банк
clients = {}
def bank(operation, id, amount):
    clients.setdefault(id, 0)
    if operation == 'top up':
        clients[id] += amount
    elif operation == 'withdraw':
        clients[id] -= amount
    elif operation == 'pay':       
        clients[id] -= amount
    elif operation == 'show balance': 
        print(clients[id])

bank('top up', 'anna', 500)
bank('top up', 'boris', 200)
bank('pay', 'anna', 150)
bank('show balance', 'boris', None)
bank('show balance', 'anna', None)

