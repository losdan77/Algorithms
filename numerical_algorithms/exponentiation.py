import time


def exponentiation(value, p):
    result = 1

    factor = value

    while p:
        if p % 2 == 1:
            result *= factor

        factor *= factor
        p //= 2
        print(f'result={result}, factor={factor}, p={p}')

    return result


def main():
    start_time = time.time()    
    print(exponentiation(9, 11))
    end_time = time.time()
    print('time = ', end_time - start_time)

    start_time = time.time()    
    print(9 ** 11)
    end_time = time.time()
    print('time = ', end_time - start_time)
    


if __name__ == '__main__':
    main()