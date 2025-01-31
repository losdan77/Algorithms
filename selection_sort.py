def selection_sort(target):
    print(target)
    for i in range(len(target) - 1):
        min_idx = i
        for j in range(i + 1, len(target)):
            if target[min_idx] > target[j]:
                min_idx = j
        
        if i != min_idx:
            target[i], target[min_idx] = target[min_idx], target[i]
            print(target)
    
    return target


def main():
    example_list = [1, 6, 2, 4, 8, 9 ,10, 3, 5, 7]
    print(selection_sort(example_list))


if __name__ == '__main__':
    main()