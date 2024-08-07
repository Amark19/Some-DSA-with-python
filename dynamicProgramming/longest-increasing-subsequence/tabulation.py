class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]
        for idx in range(len(nums) - 1, -1, -1):
            for prev_idx in range(idx - 1, -2, -1):
                ln = dp[idx + 1][prev_idx + 1]  # not take current index
                if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                    ln = max(ln, 1 + dp[idx + 1][idx + 1])  # take current index
                dp[idx][prev_idx + 1] = ln
        return dp[0][0]