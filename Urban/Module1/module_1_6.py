# Варинат решения с выводом строки с удаленными пробелами

my_string = input("Введите произвольную строку: ")
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])

# Варинат решения с изменением строки путем удаления всех пробелов

my_string = input("Введите произвольную строку: ")
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
my_string = my_string.replace(" ", "")
print(my_string[0])
print(my_string[-1])