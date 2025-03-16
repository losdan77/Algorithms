def greatest_common_divisor(num_a, num_b):
    '''итерационный подход'''
    a_mod_b = 0
    while num_b:
        a_mod_b = num_a % num_b
        num_a = num_b
        num_b = a_mod_b
        # print(num_a, num_b)
    return num_a


def gcd_recursiv(num_a, num_b):
    if num_b:
        return gcd_recursiv(num_a=num_b, num_b=num_a % num_b)
    return num_a


def main():
    num_a = 4851
    num_b = 3003
    print(greatest_common_divisor(num_a=num_a, num_b=num_b))
    print(gcd_recursiv(num_a=num_a, num_b=num_b))


if __name__ == '__main__':
    main()