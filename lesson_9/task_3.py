def letter_counter(file):
    file_to_read = open(file, 'r')
    text = file_to_read.read().lower()
    letter = input('Enter a letter: ')
    num_of_letters = text.count(letter.lower())
    return print(f'Letter {letter} appears {num_of_letters} times in the file.')


letter_counter('story.txt')
