user_input = input('Введите предложение из 2-х слов: ')

s1 = ' '.join(user_input.split(' ')[::-1])

s2 = s1.split()
s2.insert(1, ' ! ')

s3 = ' '.join([str(i) for i in s2])
print(f'!{s3}!')
