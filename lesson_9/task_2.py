def merge_dicts(dict1, dict2):
    merged_dict = {}
    dict_list = [dict1, dict2]
    dict_keys = dict1.keys() | dict2.keys()
    for k in dict_keys:
        merged_dict[k] = [v.get(k) for v in dict_list]
    return print(merged_dict)


first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}

merge_dicts(first_dict, second_dict)
