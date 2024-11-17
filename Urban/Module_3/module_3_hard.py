def calculate_structure_sum(data_struct):
    summ = 0
    for i in data_struct:
        if isinstance(i, str):
            summ += len(i)
        elif isinstance(i, (int, float)):
            summ += i
        elif isinstance(i, (list, tuple, set)):
            summ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            summ += calculate_structure_sum(i.keys())
            summ += calculate_structure_sum(i.values())
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


