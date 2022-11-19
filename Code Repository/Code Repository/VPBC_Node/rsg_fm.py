import random


def random_by_number(number, min_random, max_random, spaces=1, precision=2):
    if spaces <= 0:
        return number

    random_numbers = [random.uniform(min_random, max_random) for i in range(0, spaces)]
    increment_number = (number - sum(random_numbers)) / spaces

    return [round(n + increment_number, precision) for n in random_numbers]


number = int(input ("Enter the secret amount:"))
spaces = int(input ("Enter the number of shares:"))
max_random = number / spaces
min_random = max_random * 0.6
random_numbers = random_by_number(number, min_random, max_random, spaces=spaces, precision=2)

print(random_numbers)
print(len(random_numbers))
print(sum(random_numbers))
