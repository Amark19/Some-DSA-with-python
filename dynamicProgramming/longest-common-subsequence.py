class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_arr = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp_arr[i][j] = dp_arr[i-1][j-1] + 1
                else:
                    dp_arr[i][j] = max(dp_arr[i][j-1],dp_arr[i-1][j])
        print(dp_arr)      
        return dp_arr[len(text1)][len(text2)]
