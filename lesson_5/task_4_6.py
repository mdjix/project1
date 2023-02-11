import timeit

n = int(input('Введите число: '))
sum1 = 0
sum2 = 0
i = 1

myfunc1 = '''
def func1(sum1):

    while i <= n:
        sum1 += i ** 3
        print(sum1)
        i += 1
'''

myfunc2 = '''
def func2(sum2):

    for i in range(1, n + 1):
        sum2 += i ** 3
        print(sum2)

'''

print('Время, затраченное на выполнение цикла while - ', timeit.timeit(stmt=myfunc1, number=10000))
print('Время, затраченное на выполнение цикла for - ', timeit.timeit(stmt=myfunc2, number=10000))
