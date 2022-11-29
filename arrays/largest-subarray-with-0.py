class Solution:
    def maxLen(self, n, arr):
        #approach is simple just go on adding numbers in su variable and add sum as key with index as it's value in dictionary.
        #if that su is present that means there is subarray with 0 (15,2,-2) => 15.so we can take maximum between already max_value and
        #current_index - dictinary[su] so we will get length of subarray 
        #15 8 -2 2
        #15 + 8 => 23
        #23 -2 + 2 => 23
        #so here 23 previously occured in index 1 and current is 4,so length becomes 2
        su,dic,maxval = 0,{},0
        for i in range(len(arr)):
            su += arr[i]
            if su in dic:
                maxval = max(maxval,i - dic[su])
            elif su == 0:
                maxval = max(maxval,i+1)
            else:
                dic[su] = i
        return maxval
