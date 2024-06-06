from functools import reduce


def f1(x, y):
    return x + y


print(f1(5, 5))

f2 = lambda x, y: x + y

print(f2(5, 5))

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)

suma = reduce(lambda x, y: x + y, liczby)
print(suma)

parzysta2 = [x for x in range(10) if x % 2 == 0]
print(parzysta2)