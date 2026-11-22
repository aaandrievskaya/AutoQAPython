# konverter_kilometrov
def convert_to_miles(km):
    return km* 0.6214

# print(convert_to_miles(1))
# print(convert_to_miles(5))
# print(convert_to_miles(10))

# kolichestvo_dney
def get_days(month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif month == 2:
        return 28

# print(get_days(1))
# print(get_days(2))
# print(get_days(9))

# Делители 1
def get_factors(num):
    sp=[i for i in range(1, num+1) if num % i == 0]
    return sp

# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))

# Делители 2
def number_of_factors(num):
    return len(get_factors(num))

# print(number_of_factors(1))
# print(number_of_factors(5))
# print(number_of_factors(10))

# Найти всех
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

# print(find_all('AaAa', 'a'))
# print(find_all('a b c', ' '))
# print(find_all('', 'a'))

# Merge lists 1
def merge(list1, list2):
    list1.extend(list2)
    return sorted(list1)

# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))

# Merge lists 2
def quick_merge():
    n = int(input())
    req = [input() for _ in range(n)]
    
    list1 = [int(i) for i in req[0].split()]
    list2 = [int(i) for i in req[1].split()]

    for item in range(1, len(req)-1): 
        list1 = merge(list1, list2)
        list2 = [int(i) for i in req[item+1].split()]
        
    return merge(list1, list2)

print(*quick_merge())