def binary_search(x,low,high,search):
    mid = (low+high)//2
    if x[mid]==search:
        return mid
    elif search<x[mid]:
        return binary_search(x,low,mid-1,search)
    else:
        return binary_search(x,mid+1,high,search)

x = [10,14,15,18,19,67]
low = 0
high = len(x)-1
search = int(input("Enter the element tha you want to search? "))
print(binary_search(x,low,high,search))
