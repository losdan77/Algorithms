def quicksort(array, start, end):
    if start >= end:
        return
    
    divider = array[start]

    before, after = [], []

    i = start + 1
    while i <= end:
        if array[i] < divider:
            before.append(array[i])
        if array[i] > divider:
            after.append(array[i])
        i += 1

    index = start
    while len(before) > 0:
        array[index] = before.pop()
        index += 1

    array[index] = divider

    midpoint = index

    index += 1
    while len(after) > 0:
        array[index] = after.pop()
        index += 1

    quicksort(array=array, start=start, end=midpoint - 1)
    quicksort(array=array, start=midpoint + 1, end=end)


def main():
    example_arrray = [7, 8, 9, 4, 6, 5, 10, 3, 2, 1]
    quicksort(example_arrray, 0, len(example_arrray)-1)
    print(example_arrray)


if __name__ == '__main__':
    main()