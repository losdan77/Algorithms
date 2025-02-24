def countingsort(array, max_value):
    counts = [0] * (max_value + 1)

    for values in array:
        counts[values] += 1
    print(counts)

    index = 0
    for i in range(max_value + 1):
        for j in range(counts[i]):
            array[index] = i
            index += 1
    

def main():
    example_array = [1, 2, 2, 1, 0, 2, 2, 1, 0, 2]
    countingsort(array=example_array, max_value=2)
    print(example_array)


if __name__ == "__main__":
    main()