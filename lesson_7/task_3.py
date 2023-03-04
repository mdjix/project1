words = ('tenet', 'war', 'civic', 'mom', 'game', 'level', 'phone', 'laptop', 'radar', 'moon',
         'racecar', 'lyrics', 'avalanche', 'madam', 'save', 'olive')

palindrome = filter(lambda x: x == x[::-1], words)
print(list(palindrome))


# def func(i):
#     if i == i[::-1]:
#         return i
#
#
# palindrome = filter(func, words)
# print(list(palindrome))
