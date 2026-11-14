def summa_elementov_matrici():
    matrix = [[3, 7, 2],
              [8, 1, 5],
              [4, 9, 6]]
    cols = len(matrix)   #так как матрица квадратная

    sum_all = 0
    for r in range(len(matrix)):
        for c in range(cols):      
            sum_all += matrix[r][c]
    print(f'Сумма всех элементов: {sum_all}')

    r1, r2, r3 = matrix
    sum_r1 = 0
    sum_r2 = 0
    sum_r3 = 0
    for x in r1:
        sum_r1 += x
    for x in r2:
        sum_r2 += x
    for x in r3:
        sum_r3 += x
    sum_str = [sum_r1, sum_r2, sum_r3]
    print(f'Суммы строк: {sum_str}')

    max = 0
    for r in range(len(matrix)):
        for c in range(cols): 
            if max < matrix[r][c]:
                max = matrix[r][c]
    print(f'Максимальный элемент: {max}')

def rabota_s_diagonalyami():
    matrix = [[5, 2, 8, 1],
              [4, 9, 3, 7],
              [6, 1, 2, 5],
              [8, 4, 7, 3]]
    
    cols = len(matrix)   #так как матрица квадратная
    sum_main = 0
    sum_secondary = 0
    for i in range(len(matrix)):
        for j in range(cols):
            if i == j:
                sum_main += matrix[i][j]
            elif j == len(matrix) - i - 1: #взяла формулу из учебника
                sum_secondary += matrix[i][j]
    print(f'Сумма главной диагонали: {sum_main}')
    print(f'Сумма побочной диагонали: {sum_secondary}')

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 0
    print('Изменённая матрица:')
    for i in range(len(matrix)):
        print(matrix[i])

def povorot_matrici_na_90():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    new_matrix = [['_'] * len(matrix) for i in range(len(matrix))]

    q_j = 3
    for i in range(len(new_matrix)): #
        for j in range(len(new_matrix)): #
            new_matrix[i][j] = matrix[q_j][i]
            q_j -= 1
            if q_j < 0:
                q_j = 3     
    for i in range(len(new_matrix)):
            print(new_matrix[i])



if __name__ == "__main__":
    #summa_elementov_matrici()
    #rabota_s_diagonalyami()
    povorot_matrici_na_90()