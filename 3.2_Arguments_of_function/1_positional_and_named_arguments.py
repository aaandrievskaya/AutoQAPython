# Создание матрицы
def matrix(n=1, m=None, value=0):
    if m == None:
        m = n
    mat = []
    for i in range(n):
        string = []
        for j in range(m):
            string.append(value)
        mat.append(string)
    return mat

print(matrix())
print(matrix(3))
print(matrix(3, 2))
print(matrix(3, 2, 7))