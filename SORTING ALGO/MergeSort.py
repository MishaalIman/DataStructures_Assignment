def merge(lA, rA):
    final = []
    i, j = 0, 0
    while i < len(lA) and j < len(rA):
        if lA[i] < rA[j]:
            final.append(lA[i])
            i += 1
        else:
            final.append(rA[j])
            j += 1
    final.extend(lA[i:])
    final.extend(rA[j:])
    return final

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    lA = merge_sort(arr[:mid])
    rA = merge_sort(arr[mid:])
    return merge(lA, rA)

arr = [10, 3, 5, 6, 7, 2, 4, 11]
print(merge_sort(arr))
