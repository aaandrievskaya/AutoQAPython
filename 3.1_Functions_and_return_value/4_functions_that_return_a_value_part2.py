# Is_the_Triangle_Valid
def is_valid_triangle(side1, side2, side3):
    max_side = max(side1, side2, side3)
    dif_sides = [side1, side2, side3]
    dif_sides.remove(max_side)
    small_1, small_2 = dif_sides
    return small_1 + small_2 > max_side

# print(is_valid_triangle(2, 2, 2))
# print(is_valid_triangle(2, 3, 10))
# print(is_valid_triangle(3, 4, 5))    

# Палиндром
def is_palindrome(text):
    symbols = []
    for i in text:
        if i.isalpha():
            symbols.append(i.lower())
    return symbols == symbols[::-1]

# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))

# Ровно в одном
def is_one_away(word1, word2):
    q = 0
    pairs = []
    if len(word1) == len(word2):
        pairs = list(zip(word1, word2))
    for item in pairs:
        if item[0] != item[1]:
            q += 1
    return q == 1
    
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))

# Змеиный регистр
def convert_to_python_case(text: str):
    res = []
    res.append(text[0].lower())
    for i in range(1, len(text)):
        if text[i].isupper():
            res.append('_')
            res.append(text[i].lower())
        else:
            res.append(text[i])
    res = ''.join(res)
    return res

# print(convert_to_python_case('HelloWorld'))
# print(convert_to_python_case('Python'))
# print(convert_to_python_case('MyFirstFunction'))

# Is the Number Prime?
def is_prime(num: int):
    delit = [i for i in range(1, num+1) if num % i == 0] 
    return len(delit) == 2

# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(17))

# Next Prime
def get_next_prime(num):
    flag = 0
    i = 1
    while flag == 0:
        if is_prime(num + i):
            flag = 1
        else:
            i += 1
    return num + i

# print(get_next_prime(1))
# print(get_next_prime(2))
# print(get_next_prime(3))
# print(get_next_prime(24))

# Good password
def is_password_good(password: str):
    r1, r2, r3, r4 = 0, 0, 0, 0
    if len(password) >= 8:
        r1 = 1
        for i in password:
            if i.isupper():
                r2 = 1
            elif i.islower():
                r3 = 1
            elif i.isdigit():
                r4 = 1
    return (r1, r2, r3, r4) == (1, 1, 1, 1)

print(is_password_good('Abcdefg1'))
print(is_password_good('Abcdef1'))
print(is_password_good('abcdefg1'))
print(is_password_good('ABCDEFG1'))
print(is_password_good('Abcdefgh'))