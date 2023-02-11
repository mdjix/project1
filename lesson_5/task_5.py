import random

number = random.randint(1, 100)

while True:
    user_number = int(input('Угадайте число от 1 до 100: '))

    if user_number <= 0:
        print('Число не из диапазона')
    elif user_number > number:
        print('Число меньше!')
    elif user_number < number:
        print('Число больше!')
    else:
        print(f'Вы угадали! Загаданное число - {number}')
        break
