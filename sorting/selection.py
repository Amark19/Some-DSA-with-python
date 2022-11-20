def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min:  # we find minimum element at each pass and
                min = arr[j]
                arr[i], arr[j] = arr[j], arr[i]  # swap it to ith position
    return arr


arr = [64, 25, 12, 22, 11]
print(selectionSort(arr))
