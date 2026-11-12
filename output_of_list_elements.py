def without_name():
    numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
    sol = 0
    for num in numbers:
        sol += num**2
    print(sol)

def negatives_zeros_and_positives():
    n = int(input())
    spis = [int(input()) for _ in range(n)]
    # spis = []
    # for _ in range(n):
    #     spis.append(int(input()))
    negatives = [num for num in spis if num < 0]
    zeros = [num for num in spis if num == 0]
    positives = [num for num in spis if num > 0]
    res = []
    res.extend(negatives)
    res.extend(zeros)
    res.extend(positives)
    print(*res, sep='\n')

def bez_dublicatov():
    n = int(input())
    spis = [str(input()) for _ in range(n)]

    res = [spis[0]]
    for i in range(1, len(spis)):
        if spis[i] not in res:
            res.append(spis[i])
    print()        
    print(*res, sep='\n')



if __name__ == "__main__":
    #without_name()
    #negatives_zeros_and_positives()
    bez_dublicatov()