class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1] * len(arr)
        hsh = [1] * len(arr)
        maxi = 0
        maxIndex = 0
        for i in range(0, len(arr)):
            hsh[i] = i
            for j in range(0, i):
                if arr[i] > arr[j] and 1 + dp[j] > dp[i]:
                    dp[i] = dp[j] + 1
                    hsh[i] = j
            if dp[i] > maxi:
                maxi = dp[i]
                maxIndex = i
        st = []
        st.append(arr[maxIndex])
        # 5 4 11 1 16 8
        while hsh[maxIndex] != maxIndex:
            maxIndex = hsh[maxIndex]
            st.append(arr[maxIndex])
        return st[::-1]