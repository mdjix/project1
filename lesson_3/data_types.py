a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
sum = a + b
print(f"Сумма: {sum}")

print(a>b)
float_a = float(a)
print(float_a)

poetry = '   Ночь, улица, фонарь, аптека, бессмысленный и тусклый свет'
print(poetry[:16])
print(poetry.swapcase())  # верхний регистр в нижний, и наоборот
print(poetry.upper())
print(poetry.split(','))
print(poetry.lstrip())  # удаляет пробелы в начале строки
