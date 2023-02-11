def func(list1):
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


print(func([1, 2, 3, 4, 5, 4, 4, 3, 2, 2, 2, 1]))
