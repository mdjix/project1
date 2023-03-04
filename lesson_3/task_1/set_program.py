set1 = set('programming')  # set1 = set() - create empty set
print(set1)

set2 = {'a', 'b', 'c'}  # set2 = {} - dict. Can't create empty set using {}
print(set2)

set3 = {i ** 2 for i in range(10)}  # set generator
print(set3)

fruits = ['apple', 'banana', 'orange', 'lemon', 'banana']
print(set(fruits))

x = input('Enter fruit: ')
print(x in fruits)

list1 = [1, 6, 3]
print(set2.isdisjoint(list1))  # Проверяет отсутствие общих элементов множества
                               # и последовательности (кортеж, символ или подстрока)

print(set2.union(set3))  # объединение нескольких множеств

set1.add('j')
print(set1)

set1.remove('j')  # удаляет эл-т из множества, если такого нет - KeyError
print(set1)

set1.discard('a')  # удаляет элемент, если он находится в множестве
print(set1)

print(set1.pop())  # удаляет первый эл-т множества (нельзя сказать какой конкретно эл-та будет удален)

