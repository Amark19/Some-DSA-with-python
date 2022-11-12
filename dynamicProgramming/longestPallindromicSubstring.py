def longestPalindrome(self, s: str) -> str:
    length,max_rep,idx,string = len(s),0,0,""
    arr = [[0 for k in range(length+1)] for l in range(length+1)]
    for i in range(length + 1):
        for j in range(length + 1):
            if (i == 0 or j == 0):arr[i][j] = 0
            elif s[length - i] == s[j - 1] : arr[i][j] = arr[i-1][j-1] + 1
            else:arr[i][j] = 0
            if max_rep < arr[i][j]: idx = j;max_rep = arr[i][j]
    for i in range(max_rep):
        string += s[idx-i-1]
    print(idx)
    return string