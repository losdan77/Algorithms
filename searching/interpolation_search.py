def interpolation_search(array: list, target: int):
    min_idx = 0
    max_idx = len(array) - 1
    num_iter = 0

    while min_idx < max_idx:
        num_iter += 1

        middle_idx = min_idx + (max_idx - min_idx) * (target - array[min_idx]) // (array[max_idx] - array[min_idx])

        print(min_idx, middle_idx, max_idx)

        if (middle_idx < min_idx) or (middle_idx > max_idx):
            return None
        
        if array[middle_idx] > target:
            max_idx = middle_idx - 1
        elif array[middle_idx] < target:
            min_idx = middle_idx + 1
        else:
            return middle_idx, num_iter
        
    return None


def main():
    sorted_array = [2, 4, 7, 11, 12, 17, 23, 24, 26, 27, 29, 31, 33, 40, 43, 45, 46]
    print(interpolation_search(sorted_array, 22))


if __name__ == '__main__':
    main()