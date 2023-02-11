from datetime import datetime
import time

def runtime(func):
    def wrapper(*args):
        start_time = datetime.now()
        value = func(*args)
        execution_time = datetime.now() - start_time
        print(f'Execution time - {execution_time}')
        return value
    return wrapper


@runtime
def func(dict1):
    dict2 = {}
    for k, v in dict1.items():
        dict2[v] = k
        time.sleep(2)
    return dict2


print(func({1: 'a', 2: 'b', 3: 'c'}))


@runtime
def func2(list1):
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] += 1
            time.sleep(1)
        else:
            dict1[i] = 1
            time.sleep(1)
    return dict1


print(func2([1, 2, 3, 4, 5, 4, 4, 3, 2, 2, 2, 1]))
