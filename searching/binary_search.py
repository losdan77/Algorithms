def binary_search(array: list, target: int):
    min_idx = 0
    max_idx = len(array) - 1

    while min_idx <= max_idx:
        middle_idx = (min_idx + max_idx) // 2

        if array[middle_idx] < target:
            min_idx = middle_idx + 1
        elif array[middle_idx] > target:
            max_idx = middle_idx - 1
        else:
            return middle_idx
        
    return None


def main():
    example_search = [1, 3, 4, 5, 6, 7, 8, 12, 14, 16, 17, 22, 23, 24, 26]
    print(binary_search(array=example_search, target=8))
    

if __name__ == '__main__':
    main()