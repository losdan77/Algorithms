def mergesort(array, temp_array, start, end):
    
    if start == end:
        return
    
    midpoint = (start + end) // 2

    mergesort(array=array, temp_array=temp_array, start=start, end=midpoint)
    mergesort(array=array, temp_array=temp_array, start=midpoint+1, end=end)

    left_index = start
    right_index = midpoint + 1
    temp_array_index = left_index

    while (left_index <= midpoint) and (right_index <= end):
        if array[left_index] <= array[right_index]:
            temp_array[temp_array_index] = array[left_index]
            left_index += 1
        else:
            temp_array[temp_array_index] = array[right_index]
            right_index += 1
        temp_array_index += 1

    for i in range(left_index, midpoint + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1
    for i in range(right_index, end + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1

    for i in range(start, end + 1):
        array[i] = temp_array[i]


def main():
    example_array = [3, 7, 1, 2, 4, 8, 10, 9, 5, 6]
    temp_array = [None] * len(example_array)

    mergesort(array=example_array, temp_array=temp_array, start=0, end=len(example_array)-1)
    print(temp_array)
    print(example_array)
    

if __name__ == '__main__':
    main()