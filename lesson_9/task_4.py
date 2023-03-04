import math


def find_distance(*args):
    length = 0
    for index, point in enumerate(args[:-1]):
        x1, y1 = point
        x2, y2 = args[index+1]
        length += (x2 - x1)**2 + (y2 - y1)**2
    distance = math.sqrt(length)
    return distance


result = find_distance((1, 1), (1, 2), (3, 3))
print(result)
