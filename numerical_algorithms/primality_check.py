from math import sqrt
from random import randint


def probability_primality_check(value, tests):
    for i in range(tests):
        # Получаем случайное а
        a = randint(1, value - 1)
        # Проверка на простоту с помощью возведения в степень по модулю.
        # Аналог выражения, a ** (p - 1) % p, но работает гораздо быстрее.
        if pow(a, value - 1, value) != 1:
            return False
    return True


def true_primality_check(value):
    for i in range(2, int(sqrt(value))):
        if value % i == 0:
            return False
    return True


def main():
    print(true_primality_check(3571))
    print('---')
    tests = 10
    print(probability_primality_check(3571, tests))
    print(probability_primality_check(3539, tests))
    print(probability_primality_check(479001599, tests))
    print(probability_primality_check(2856, tests))
    print(probability_primality_check(3537, tests))
    print(probability_primality_check(321197185, tests))


if __name__ == '__main__':
    main()