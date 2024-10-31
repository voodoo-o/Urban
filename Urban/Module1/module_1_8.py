# Создание словаря

my_dict = {"Name": "Vlad", "Age": 20}
print("Dict:", my_dict)
print("Existing value:", my_dict["Age"])
print("Not existing value: ", my_dict.get('Work'))
my_dict.update({'is_student': True})
name = my_dict.pop("Name")
print("Deleted value:", name)
print("Modified dictionary:", my_dict)

# Создание множества

my_set = {1, 1, 1, 2, 3, 3, "Hi", 234.123, "Hi"}
print("Set:", my_set)
my_set.add(111)
my_set.add(2.3)
print("Modified set:", my_set)
