def func(x: str) -> str:
    if x.isdigit():
        return f'Вы ввели целое число {x}'
    else:
        try:
            float(x)
            if float(x).is_integer():
                return f'Вы ввели отрицательное число {x}'
            if float(x) < 0:
                return f'Вы ввели отрицательное дробное число {x}'
            else:
                return f'Вы ввели дробное число {x}'
        except ValueError:
            return f'Вы ввели некорректное значение: {x}'


user_input = input('Enter number: ')
print(func(user_input))
