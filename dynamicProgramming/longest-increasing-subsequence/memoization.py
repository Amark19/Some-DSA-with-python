class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]

        def recur(idx, prev_idx):
            if idx == len(nums): return 0
            if dp[idx][prev_idx + 1] != -1: return dp[idx][prev_idx + 1]
            ln = recur(idx + 1, prev_idx)  # not take current index
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                ln = max(ln, 1 + recur(idx + 1, idx))  # take current index
            dp[idx][prev_idx + 1] = ln
            return ln

        return recur(0, -1)