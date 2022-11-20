def bubbleSort(arr):
    for i in range(len(arr)):
        # as in each iteration we r sorting array from right hand side so we don't have to traverse whole array instead we can traverse till n-i-1
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 25, 12, 22, 11]
print(bubbleSort(arr))
