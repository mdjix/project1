numbers = [1, 2, 3, 4]
print(type(numbers))
print(numbers[1])

numbers.append(5)
print(numbers)

letters = ['a', 'b', 'c', 'd', 'e']
new_item = input('Enter a letter: ')
letters.insert(3, new_item)
numbers.extend(letters)
print(numbers)

numbers.insert(5, '!')  # insert '!' at position 5
numbers.insert(6, 'c')
print(numbers)

numbers.remove('c')  # remove the first item whose equal to x
print(numbers)

deleted_item = numbers.pop(4)  # remove and return the item from the position x
print(numbers)
print(deleted_item)
deleted_item2 = numbers.pop()  # remove and return the last item in the list
print(numbers)
print(deleted_item2)

item_index = numbers.index('b')
print(item_index)

print(numbers.count('b'))  # return the number of times x appears in the list

# sort() changes the list directly and doesn't return any value
new_number_list = [4, 2, 9, 0, 1, 7, 3]
new_number_list.sort()  # sort the items of the list in ascending order
print(new_number_list)
new_number_list.sort(reverse=True)  # sort the items of the list in descending order
print(new_number_list)

new_letter_list = ['j', 'bye', 'morning', 'hi', 'night', 'a']
new_letter_list.sort(key=len)  # the list is sorted by the length of each element
print(new_letter_list)

copy_list = new_number_list.copy()
print(id(new_number_list))
print(id(copy_list))  # different id

numbers.clear()
print(numbers)

c = [c * 3 for c in 'python']  # generate new list
print(c)
