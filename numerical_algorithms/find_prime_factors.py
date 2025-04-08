def find_factors(number):
    factors = []

    # проверяем делимость на 2
    while number % 2 == 0:
        factors.append(2)
        number = number // 2
    
    i = 3
    max_factor = number ** 0.5
    while i < max_factor:
        # Проверяем делимость на i.
        # Используем while, так как number 
        # может иметь несколько одинаковых простых делителей, 
        print(f"out: i = {i}, max_factor = {max_factor}")
        while number % i == 0:
            
            factors.append(i)
            number = number // i
            max_factor = number ** 0.5
            print(f"in: i = {i}, max_factor = {max_factor}, number = {number}")
        # Увеличиваем на 2, так как рассматриваем только нечетные числа
        i += 2

    if number > 1:
        factors.append(number)

    return factors


def main():
    # Простые числа.
    print(23 * 17, find_factors(23 * 17))
    print(137 * 239, find_factors(137 * 239))
    print(1046527 * 16127, find_factors(1046527 * 16127))
    print(16769023 * 1073676287, find_factors(16769023 * 1073676287))

    # Составное число.
    print(545632, find_factors(545632))


if __name__ == "__main__":
    main()