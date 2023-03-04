a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

while True:
    action = input('Выберите действиве (+, -, *, **, //, %). Чтобы выйти введите "end": ')

    if action == '+':
        print(f'Сумма: {a+b}')
    elif action == '-':
        print(f'Разность: {a-b}')
    elif action == '*':
        print(f'Произведение: {a*b}')
    elif action == '**':
        print(f'{a} в степени {b}: {a**b}')
    elif action == '//':
        print(f'Результат целочисленного деления: {a//b}')
    elif action == '%':
        print(f'Результат деления по модулю: {a%b}')
    elif action == 'end':
        break;
    else:
        print('Введен неправильный символ.')
