list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 is not list2)

# task 3

tuple1 = tuple(list1)
tuple2 = tuple(list2)

tuple1 = tuple2
print(tuple1 is tuple2)
