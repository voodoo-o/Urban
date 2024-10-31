immutable_var = tuple(["Hello", 111, True, 23.2])
print("Immutable tuple: ", immutable_var)

# Поптыка изменения элемента в кортеже

# immutable_var[0] = "hellp"
# print(immutable_var)

# Изменять значения элементов в кортеже нельзя, потому что кортежи являются неизменяемыми типами последеовательности

mutable_list = [1, True, 'a']
mutable_list[0] = 10
mutable_list[1] = False
mutable_list[2] = 'b'
print("Mutable list: ", mutable_list)
