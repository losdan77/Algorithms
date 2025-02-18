example_array = [1, 4, 3, 5, 2, 9, 7, 10, 11, 8]

def insertion_sort(array: list):
    for i in range(1, len(array)):
        print(array)
        j = i
        while array[j] < array[j - 1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

def main():
    print(f'finish={insertion_sort(example_array)}')

if __name__ == "__main__":
    main()