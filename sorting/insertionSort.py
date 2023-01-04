def insertionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1,0,-1):#sorting left side of array at each iteration
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
        print(arr)



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(arr)
