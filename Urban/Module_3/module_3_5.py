def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0]
    if len(str_number) == 1:
        return int(first)
    else:
        return int(first) * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)

