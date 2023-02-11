user_input = input('Введите строку: ').strip()

even_symbols = user_input[1::2]
odd_symbols = user_input[::2]

print(f'Введена строка "{user_input}".', end='\n\n')
print(even_symbols, odd_symbols, sep='     ', end='\n!!!')
