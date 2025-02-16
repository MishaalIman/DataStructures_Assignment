def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

arr = [6, 5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)
