dict1 = {}
dict1['Book'] = 'Harry Potter and and the Philosopher\'s Stone'
dict1['Author'] = 'J. K. Rowling'
print(dict1)

dict2 = dict(film='Gladiator', director='Ridley Scott', year=2000)
print(dict2)

dict3 = dict([(1, 'a'), (2, 'b')])
print(dict3)

dict4 = dict.fromkeys([1, 2, 3, 4, 5], 'hi')
print(dict4)

dict5 = {a: a+1 for a in range(5)}
print(dict5)
dict5.clear()
print(dict5)

dict_copy = dict3.copy()
dict_copy[3] = 'c'
print(dict3)
print(dict_copy)

print(dict4.get(5))  # return key value, return None if key doesn't exist
dict4.setdefault(6, 'hello')  # return key value, create key with default value if key doesn't exist
print(dict4)

print(dict3.items())  # return a view object that display a list of dictionary's (key, value) tuple pairs

deleted_key = dict4.pop(6)  # delete key and return value
print(deleted_key)

deleted_item = dict4.popitem()  # delete and return key:value
print(deleted_item)

dict1.update(dict2)
print(dict1)
