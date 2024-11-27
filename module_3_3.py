def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [1, 'Big', False]
values_dict = {'a': 3, 'b': 'Small', 'c': 2}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)