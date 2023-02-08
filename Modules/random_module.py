import random

print(dir(random))

print(random.random())

print(random.randint(1, 100))

print(random.randrange(1, 10))

print(random.randrange(1, 10, 2))

print(random.choice('computer'))

print(random.choice([12, 45, 87, 44, 10, 23]))

print(random.choice((56, 77, 32, 99, 82, 18)))

num = [12, 45, 87, 44, 10, 23]
random.shuffle(num)
print(num)
