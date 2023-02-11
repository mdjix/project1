num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if num1 > 10 and num2 > 10:
    print('Оба числа больше 10.')
elif num1 > 10 or num2 > 10:
    print('Одно из чисел больше 10.')
else:
    if not bool(num1):
        print('Условие с помощью преобразования типов.')
    else:
        print('Блок else.')