def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < min:
                min = arr[j]
                arr[i],arr[j] = arr[j],arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print(selectionSort(arr))