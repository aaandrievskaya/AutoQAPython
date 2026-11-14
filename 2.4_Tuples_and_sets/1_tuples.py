def task_2():
    countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')
    print(countries[-1])

def task_3():
    primes = (31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    print(primes[0:5])

def task_4():
    countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
    print(countries[2:])

def task_5():
    countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
    print(countries[0:-3])

def task_6():
    countries = ('Australia', 'Russia', 'Nigeria', 'Chad', 'Canada', 'USA', 'Germany', 'Netherlands')
    print(countries[3:-2])

def task_7():
    countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
    print(len(countries))    

def task_8():
    numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
    print(max(numbers) + min(numbers))  

def task_9():
    countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
    print(countries.index('Slovenia'))

if __name__ == "__main__":
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()