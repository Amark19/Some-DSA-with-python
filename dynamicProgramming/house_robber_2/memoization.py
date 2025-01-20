class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp1 = [-1 for i in range(n - 1)]
        dp2 = dp1.copy()

        def recur(arr, idx, dp):
            if (idx == 0): return arr[idx]
            if (idx < 0): return 0
            if dp[idx] != -1:
                return dp[idx]
            should_consider = arr[idx] + recur(arr, idx - 2, dp)
            not_consider = 0 + recur(arr, idx - 1, dp)
            dp[idx] = max(should_consider, not_consider)
            return dp[idx]

        return max(recur(nums[1:], n - 2, dp1), recur(nums[:n - 1], n - 2, dp2))
