tuple1 = (1, 2, 3, 4)
tuple2 = (1, 2, 3, 4)
tuple3 = (1, 2, 3, 4)

print(tuple1 is tuple2)
print(tuple2 is tuple3)

# task 3

list1 = list(tuple1)
list2 = list(tuple3)
list3 = list(tuple3)

print(list1 is not list2)
print(list2 is not list3)
