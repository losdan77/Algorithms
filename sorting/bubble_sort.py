example_array = [4, 9, 1, 2, 5, 7, 10, 3]


def bubble_sort(array: list):
    print('start sort: ', array)

    n = 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] > array[i+1]:
                is_sorted = False
                array[i], array[i+1] = array[i+1], array[i]
        print(array)
        n += 1

    print('end sort: ', array)
    return array


def main():
    bubble_sort(example_array)


if __name__ == '__main__':
    main()