from datetime import datetime
import time


def sleep_time() -> str:
    time_now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    time.sleep(1)
    return time_now


def range_number(n: int) -> list:
    number = [sleep_time() for _ in range(n)]
    return number


result = int(input('Введите число: '))
print(range_number(result))


# def func(n):
#     list1 = []
#     for i in range(n):
#         list1.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
#         time.sleep(1)
#     return list1
#
#
# result = func(int(input('Введите число: ')))
# print(result)
