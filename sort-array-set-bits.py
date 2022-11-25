
# Using custom comparator lambda function
arr = [31,2,3,5,13]

print(sorted(arr, key = lambda x: (bin(x).count('1'), x)))
