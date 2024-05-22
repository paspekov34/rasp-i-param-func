def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [1, 2, 3]
values_dict = ({'a': 8917, 'b': 8929, 'c': 8905})
values_list_2 = [23, 'string']
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, 2, 3)
print_params(c=[1, 2, 3])
print_params(a=1, b=2, c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)