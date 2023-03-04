first_line = frozenset('У лукоморья дуб зеленый')
print(first_line)

second_line = frozenset('Златая цепь на дубе том')

print(first_line.difference(second_line))  # возвращает разницу

print(first_line.intersection(second_line))  # возвращает пересечение (одинаковые эл-ты)

print(first_line.issubset(['a', 'f', 'p']))  # является ли подмножеством

print(first_line.issuperset(['м', 'з', 'ы', 'б', 'ь', 'р', 'о', ' ']))  # является ли надмножеством

print(first_line.symmetric_difference(second_line))  # Возвращает только те элементы, которые есть либо в одном,
                                                     # либо в другом мн-ве

