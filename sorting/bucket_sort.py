import math


def bucketsort(array):
    count_element_in_bucket = 3
    num_bucket = math.ceil(len(array)/count_element_in_bucket)

    buckets = []
    for i in range(num_bucket):
        buckets.append([None]*count_element_in_bucket)

    for value in array:
        bucket_num = int(value / count_element_in_bucket)

        current = buckets[bucket_num]
        for i in range(len(current)):
            if current[i] is None:
                current[i] = value
                break

    print(buckets)      

    index = 0
    for idx in range(num_bucket):
        
        for i in range(len(buckets[idx])):
            if buckets[idx][i] is None:
                del buckets[idx][i]
        
        buckets[idx].sort()
        
        for value in buckets[idx]:
            array[index] = value
            index += 1

    print(buckets)


def main():
    example_array = [3, 4, 5, 1, 7, 2, 10, 9, 8, 6]
    bucketsort(example_array)
    print(example_array)


if __name__ == '__main__':
    main()