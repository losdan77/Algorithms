def gen_prime(n):
    '''Решето Эратосфена'''
    result = []
    array = [x if x%2!=0 or x == 2 else -1 for x in range(n + 1)] # сразу убираем четные
    p = 2

    while p <= n:
        
        if array[p] != -1:
            result.append(p)

            factor = 2
            p_mult = p * factor

            while p_mult <= n:
                array[p_mult] = -1
                factor += 1
                p_mult = p * factor

        p += 1

    return result


def main():
    print(gen_prime(200))


if __name__ == '__main__':
    main()