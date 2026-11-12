
def alfavit():
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alf = [alfabet[i] * (i + 1) for i in range(len(alfabet))]
    # alf = []
    # for i in range(len(alfabet)):
    #     alf.append(alfabet[i]*(i+1))
    print(alf)

def vse_srazu_1():
    numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 
               0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
    print(len(numbers)) #Вывел длину списка;
    print(numbers[-1]) #Вывел последний элемент списка;
    print(numbers[::-1]) #Вывел список в обратном порядке (вспоминаем срезы);

    num5 = numbers.count(5)
    num17 = numbers.count(17)
    if num5 > 0 and num17 > 0:   #Вывел «YES» (без кавычек), если список содержит числа 5 и 17, или «NO» (без кавычек) в противном случае;
        print('YES')
    else:
        print('NO') 

    numbers.pop(0)
    numbers.pop()
    print(numbers)  #Вывел список с удалёнными первым и последним элементами.

def spisok_deliteley():
    n = int(input())
    delit = [i for i in range(1, n+1) if n % i == 0]
    # delit = []
    # for i in range(1, n+1):
    #     if n % i == 0:
    #         delit.append(i)
    print(delit)



if __name__ == "__main__":
    #alfavit()
    #vse_srazu_1()
    spisok_deliteley()