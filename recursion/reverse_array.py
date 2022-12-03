def reverse(l,r):
    if l >= r:return
    arr[l],arr[r] = arr[r],arr[l]
    reverse(l+1,r-1)
arr = [1,2,3,4,5,6]
reverse(0,len(arr) - 1)
print(arr)