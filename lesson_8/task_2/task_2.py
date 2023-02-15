def work_with_file(s1, s2, s3, s4):

    list1 = [s1, s2]
    list2 = [s3, s4]

    with open('file.txt', 'w') as my_file:
        for i in list1:
            my_file.write(i + '\n')
    my_file.close()

    with open('file.txt', 'a') as my_file:
        for i in list2:
            my_file.write(i + '\n')
    my_file.close()
    return my_file


str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
str3 = input('Enter third string: ')
str4 = input('Enter fourth string: ')

work_with_file(str1, str2, str3, str4)
