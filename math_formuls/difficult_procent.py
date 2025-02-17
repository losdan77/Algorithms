def compute_difficult_procent(start_sum, year_procent, mounth):
    mounth_procent = year_procent / 12
    result_sum = start_sum * (1 + mounth_procent / 100) ** mounth
    return result_sum


def main():
    print(compute_difficult_procent(10000, 16, 6))


if __name__ == '__main__':
    main()