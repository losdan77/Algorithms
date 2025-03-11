def linear_search(value, target):
    i = 0
    while i < len(target):
        if target[i] == value:
            return True
        i += 1
    return False


def linear_search_with_sort(value, target):
    i = 0
    target.sort()
    while i < len(target):
        if target[i] == value:
            return True
        if target[i] > value:
            return False
        i += 1
    return False


def linear_search_idx_with_for(target, value):
    for idx, v in enumerate(target):
        if v == value:
            return idx
    return -1


def linear_search_with_eq_item(target, value):
    i = 0
    result_list = []
    while i < len(target):
        if target[i] == value:
            result_list.append(i)
        i += 1
    
    if result_list:
        return result_list
    return -1 


def main():
    example_list = [1, 4, 6, 2, 9, 10, 5, 3, 7]
    example_list_2 = [1, 2, 3, 4]
    example_list_3 = [2, 4, 5, 4, 7, 8, 3, 4]

    print(linear_search(9, example_list))
    print(linear_search_with_sort(3, example_list))
    print(linear_search_idx_with_for(example_list_2, 3))
    print(linear_search_with_eq_item(example_list_3, 4))

if __name__ == '__main__':
    main()