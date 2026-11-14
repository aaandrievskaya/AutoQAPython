def postrochniy_vivod():
    n = input()
    print(*n.split(), sep='\n')

def initciali():
    n = input()
    a, b, c = n.split()
    print(f'{a[0]}.{b[0]}.{c[0]}.')

def windows_os():
    n = input()
    print(*n.split('\\'), sep='\n')

def korrectniy_ip_adres():
    n = input()
    a, b, c, d = n.split('.')
    if (int(a) >= 0 and int(a) <= 255) and (int(b) >= 0 and int(b) <= 255) and (int(c) >= 0 and int(c) <= 255) and (int(d) >= 0 and int(d) <= 255):
        print('ДА')
    else:
        print('НЕТ')

def dobav_razdelitel():
    n = input()
    delit = input()
    l = []
    l.extend(n)
    # i = 1
    # while i < len(l):
    #     l.insert(i, delit)
    #     i+=2
    print(delit.join(l))

def kolichestvo_sovpadauchih_par():
    n = input()
    l = n.split()
    l_int = [int(x) for x in l]
    l_int_no_duble = [l_int[0]]
    for i in range(1, len(l_int)):
        if l_int[i] not in l_int_no_duble:
            l_int_no_duble.append(l_int[i])
    counts = {} #пришлось использовать словарь
    for num in l_int_no_duble:
        counts[num] = l_int.count(num)
    print(counts)
    
    # C(n, 2) = n * (n - 1) / 2 -- формула сочетаний без повторений для составления групп по 2 элемента из n различных элементов
    C = 0
    for n in counts:
        C += counts[n] * (counts[n] - 1) / 2
    print(C)


if __name__ == "__main__":
    #postrochniy_vivod()
    #initciali()
    #windows_os()
    #korrectniy_ip_adres()
    #dobav_razdelitel()
    kolichestvo_sovpadauchih_par()