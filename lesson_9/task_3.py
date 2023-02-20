def letter_counter(file):
    num_of_letters = 0
    letter = input('Enter a letter: ')
    with open(file, 'r') as file:
        for line in file:
            num_of_letters += line.count(letter.lower())
    file.close()
    return print(f'Letter {letter} appears {num_of_letters} times in the file.')


letter_counter('story.txt')
