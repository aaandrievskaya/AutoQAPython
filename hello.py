import random

k = int(input())
for i in range(k):
    print("Python is ready, baby")
    print("WOW, i'm using Git... ")
a = random.randint(0,10)
b = random.randint(0,10)
sum = a+b
print (f'{a}+{b}=...?')
sum1 = int(input())
if sum1==sum:
    print('Great!')
else:
    print('Loser!')