import csv
import time


def bubble_sort(array):
    n = len(array)
    comparisons, permutations = 0, 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                permutations += 1
    return array, comparisons, permutations

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    comparisons, permutations = 0, 0
    if low < high:
        pi, c, p = partition(array, low, high)
        comparisons += c
        permutations += p
        array, c1, p1 = quick_sort(array, low, pi - 1)
        comparisons += c1
        permutations += p1
        array, c2, p2 = quick_sort(array, pi + 1, high)
        comparisons += c2
        permutations += p2
    return array, comparisons, permutations

def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    comparisons, permutations = 0, 0
    for j in range(low, high):
        comparisons += 1
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            permutations += 1
    array[i + 1], array[high] = array[high], array[i + 1]
    permutations += 1
    return i + 1, comparisons, permutations

def merge_sort(array):
    comparisons, permutations = 0, 0
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        left_half, c1, p1 = merge_sort(left_half)
        right_half, c2, p2 = merge_sort(right_half)
        comparisons += c1 + c2
        permutations += p1 + p2

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
            permutations += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            permutations += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            permutations += 1

    return array, comparisons, permutations


if __name__ == "__main__":
    table_source = list(csv.reader(open('src/students.csv', "r"), delimiter=","))
    column_name = input(f"Enter the column to sort ({', '.join(table_source[0])}): ")
    if type(column_name) != str or column_name not in table_source[0] or column_name.isdigit():
        print("Invalid column.")
        exit()
    column_index = table_source[0].index(column_name)

    if not table_source[1][column_index].isdigit():
        print("This column is not a number. Cannot sort it.")
        exit()
    
    column_to_list = [ row[column_index] for row in table_source[1:] ]

    start = time.time()
    sorted_array, comparisons, permutations = bubble_sort(column_to_list.copy())
    end = time.time()
    print(f"Bubble sort: {end - start} seconds, {comparisons} comparisons, {permutations} permutations\
          \nComplexity: O(n^2).\n")

    start = time.time()
    sorted_array, comparisons, permutations = quick_sort(column_to_list.copy())
    end = time.time()
    print(f"Quick sort: {end - start} seconds, {comparisons} comparisons, {permutations} permutations.\
          \nComplexity: O(n log n) on average, but O(n^2) in the worst case.\n")

    start = time.time()
    sorted_array, comparisons, permutations = merge_sort(column_to_list.copy())
    end = time.time()
    print(f"Merge sort: {end - start} seconds, {comparisons} comparisons, {permutations} permutations\
          \nComplexity: O(n log n) in all cases.\
          \nThis is because the list is being split in log(n) calls and the merging process takes linear time in each call.\n")