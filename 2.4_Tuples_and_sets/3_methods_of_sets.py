def kolichestvo_slov_v_tekste():
    a = input().replace('.','').replace(',','').replace(';','').replace(':','').replace('-','').replace('?','').replace('!','').lower().split()
    s = set(a)
    print(s)
    print(len(s))

def vstrechalos_li_chislo_ranshe():
    a = input().split()
    a = [int(x) for x in a]
    s = set(a)
    for i in a:
        if i in s:
            print('NO')
            s.discard(i)
        else:
            print('YES')


if __name__ == "__main__":
    #kolichestvo_slov_v_tekste()
    vstrechalos_li_chislo_ranshe()