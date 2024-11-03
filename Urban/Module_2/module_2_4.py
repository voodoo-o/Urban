numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Простые числа
not_primes = []  # Не простые числа
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    if numbers[i] == 2:
        primes.append(numbers[i])
        continue
    is_prime = True
    for j in range(2, int(numbers[i] ** 0.5) + 1):
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
print(primes)
print(not_primes)
