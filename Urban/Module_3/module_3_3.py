def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(4, 'строка2')
print_params(10)
print_params()
print_params(b = 25)
print_params(c=[1, 2, 3])

values_list = [25, 'Hello', True]
values_dict = {'a': 123, 'b': 'Abra', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [2, 'Kadabra']
print_params(*values_list2, 42)