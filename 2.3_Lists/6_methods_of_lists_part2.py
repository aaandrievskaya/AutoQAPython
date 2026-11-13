def perestavit_min_i_max():
    a = input()
    l = a.split()
    l_int = [int(x) for x in l]
    l_int_sort = l_int.copy()
    l_int_sort.sort()
    min = l_int_sort[0]
    max = l_int_sort[len(l_int_sort)-1]

    # for i in range(len(l_int)):
    #     if l_int[i] == min:
    #         i_min = i
    #     elif l_int[i] == max:
    #         i_max = i
    i_min = l_int.index(min)
    i_max = l_int.index(max)

    l_int.remove(min)
    l_int.remove(max)
    l_int.insert(i_max, min)
    l_int.insert(i_min, max)

    l_int = [str(x) for x in l_int]
    print(' '.join(l_int))




if __name__ == "__main__":
    perestavit_min_i_max()