import sys

tuple1 = (1,)
print(type(tuple1))

a = ()
print(sys.getsizeof(a))  # empty tuple - 40, each new element +8


list1 = ['a', 'b', 'c', 'd', 'e']
tuple2 = tuple(list1)  # it can be any iterable object
print(tuple2)
print(len(tuple2))

list2 = []
tuple3 = ()
list_size = list2.__sizeof__()
tuple_size = tuple3.__sizeof__()
print(list_size > tuple_size)

fruits = ('apple', 'banana', 'cantaloupe', 'durian')
a, b, c, d = fruits  # use '_' instead of unnecessary variables (_, b, _, c)
print(c)
print(fruits[1])
print(fruits[-1])

tuple4 = (1, 2, 3, ('one', 'two', 'three'))
print(tuple4[-1])
print(tuple4[-1][1])

tuple_a = (1, 2, 3, 3)
tuple_b = (1, 2, 3, 4)
print(tuple_a > tuple_b)  # числа сравниваются по значению
tuple_c = ('a',)
tuple_d = ('j',)
print(tuple_c > tuple_d)  # строки стравниваются в алфавитном порядке

del tuple_a
# print(tuple_a)   NameError: name 'tuple_a' is not defined

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[0::2])  # print all elements with step 2 (equivalent to [::2])
print(numbers[::-1])  # print all elements in descending order
print(numbers.index(4))
print(numbers.count(1))

word1 = ('Good', )
word2 = ('morning', )
phrase = word1 + word2
print(type(phrase))

idiom = ('A', ' ', 'blessing', ' ', 'in', ' ', 'disguise')
idiom = ''.join(idiom)  # convert tuple to str
print(idiom)

numbers_list = list(numbers)  # convert to list
print(type(numbers_list))
