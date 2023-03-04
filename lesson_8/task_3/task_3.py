import json


def add_dict_to_json():
    new_dict = {}
    for i in range(100001, 100007):
        new_dict[i] = (input('Enter name: '), int(input('Enter age: ')))

    with open('file.json', 'w') as f:
        json.dump(new_dict, f)

    return f


add_dict_to_json()
