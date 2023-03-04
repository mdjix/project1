import json
import csv


def from_jsom_to_csv():
    
    with open('../task_3/file.json') as f:
        my_dict = json.load(f)

    for value in my_dict.values():
        value.append(input('Enter phone number: '))

    with open('file.csv', 'w', newline='') as my_file:
        headers = ['id', 'name', 'age', 'phone']
        writer = csv.writer(my_file, delimiter=',')
        writer.writerow(headers)
        kv_list = [[key, *val] for key, val in my_dict.items()]
        print(kv_list)
        writer.writerows(kv_list)
    return my_file


from_jsom_to_csv()
