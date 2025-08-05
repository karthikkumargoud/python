def convert_to_single_string(tup):
    return ''.join(tup)
strings = ('Hello', ' ', 'World')
print(convert_to_single_string(strings))
strings = ('Hello', 'World')
print(''.join(strings))
