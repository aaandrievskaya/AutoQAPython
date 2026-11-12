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


if __name__ == "__main__":
    #postrochniy_vivod()
    #initciali()
    #windows_os()
    korrectniy_ip_adres()