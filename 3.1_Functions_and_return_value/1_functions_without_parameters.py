def drow_box(): #task_1
    for i in range(14):
        if i == 0 or i == 13:
            print('*'*10)
        else:
            print('*'+ ' '*8 + '*')
drow_box()


def draw_triangle(): #task_2
    for i in range(10):
        print('*'*i)
draw_triangle()
