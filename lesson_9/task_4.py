import math


def find_distance(*args):
    d = 0
    for i in args:
        d += (i[1]-i[0])**2
    distance = math.sqrt(d)
    return distance


result = find_distance((1, 1), (1, 2), (3, 3))
print(result)
