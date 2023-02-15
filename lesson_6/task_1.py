def func(dict1):
    print(dict1)
    dict2 = {}
    for k, v in dict1.items():
        dict2[v] = k
    return dict2


print(func({1: 'a', 2: 'b', 3: 'c'}))
