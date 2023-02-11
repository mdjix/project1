while True:
    user_name = input('Введите ваше имя: ')
    user_age = int(input('Введите ваш возраст: '))

    if user_age <= 0:
        print('Ошибка, повторите ввод.')
    elif user_age > 0 and user_age < 10:  # 0 < user_age < 10
        print(f'Привет, шкет {user_name}')
    elif user_age >= 10 and user_age <= 18:  # 10 < user_age <= 18
        print(f'Как жизнь, {user_name}?')
    elif user_age > 18 and user_age < 100:  # 18 < user_age < 100
        print(f'Что желаете, {user_name}?')
    else:
        print(f'{user_name}, вы лжете, в наше время столько не живут...')

    exit = input('Завершить работу?\nВведите "yes" для выхода: ')

    if exit == 'yes':
        break
    else:
        continue
