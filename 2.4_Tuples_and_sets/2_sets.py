def task_1():
    numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
    print(max(numbers) + min(numbers))

def task_2():
    numbers = {10, 2, -0.5, -7, 82, 12, -4.23}
    print(sum(numbers)/len(numbers))

def task_3():
    numbers = {10, 2.5, 3, 42, 51, 10, -96}
    # sum = 0
    # for x in numbers:
    #     sum += x**2
    print(sum(x**2 for x in numbers))



if __name__ == "__main__":
    task_1()
    task_2()
    task_3()