import random

random_number = random.randint(3, 20)
print(random_number)
empty_field = []
for i in range(1, 21):
    for j in range(1, 21):
        if random_number % (i + j) == 0 and i < j:
            empty_field.append([i, j])
empty_field.sort()
for i in empty_field:
    for j in i:
        print(j, end='')



