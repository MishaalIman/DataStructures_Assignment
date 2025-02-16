def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert

arr = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(arr)
print(arr)
