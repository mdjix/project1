bytes_str = b'r\xc3\xa9sum\xc3\xa9'
print(bytes_str)

first_change = bytes_str.decode('utf-8')
print(first_change)

second_change = first_change.encode('latin-1')
print(second_change)

third_change = second_change.decode('latin-1')
print(third_change)


