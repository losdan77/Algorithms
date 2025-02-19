def heapsort(array: list):
    make_heap(array)

    i = 0
    while i < len(array):
        last = (len(array) - 1) - i

        array[0], array[last] = array[last], array[0]

        remake_heap(array=array, latest_index=last)

        i+= 1

    return(f'finish heapsort = {array}')

def make_heap(array: list):
    i = 0

    while i < len(array):
        index = i

        while index != 0:
            parent_index = (index - 1)//2

            if array[index] <= array[parent_index]:
                break

            array[index], array[parent_index] = array[parent_index], array[index]

            index = parent_index
        
        i += 1
        print(array)
    
    print(f'finish make heap={array}')


def remake_heap(array, latest_index):
    index = 0
    while True:
        child1_idx = 2 * index + 1
        child2_idx = 2 * index + 2

        if child1_idx >= latest_index:
            child1_idx = index
        if child2_idx >= latest_index:
            child2_idx = index

        if (array[index] >= array[child1_idx]) and (array[index] >= array[child2_idx]):
            break

        if array[child1_idx] > array[child2_idx]:
            swap_child_idx = child1_idx
        else:
            swap_child_idx = child2_idx

        array[index], array[swap_child_idx] = array[swap_child_idx], array[index]

        index = swap_child_idx
    print(f'finish remake_heap={array}')            


def main():
    example_array = [1, 6, 7, 3, 2, 4, 5, 10, 9, 8]
    print(heapsort(example_array))


if __name__ == '__main__':
    main()