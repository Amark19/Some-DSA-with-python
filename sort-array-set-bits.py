
# Using custom comparator lambda function
arr = [31,2,3,5,13]
 
 
# form a tuple with val, index
n = len(arr)
arr = [(arr[i], i) for i in range(n)]
 
 
def countSetBits(val):
    cnt = 0
    while val:
        cnt += val % 2
        val = val//2
    return cnt
 
 
# first criteria to sort is number of set bits,
# then the index
sorted_arr = sorted(arr, key=lambda val: (
    countSetBits(val[0]), n-val[1]), reverse=True)
sorted_arr = [val[0] for val in sorted_arr]
print(sorted_arr[::-1])
