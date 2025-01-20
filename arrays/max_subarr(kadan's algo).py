class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su = 0
        max_sum = float("-inf")
        for num in nums:
            su += num
            max_sum = max(max_sum, su)
            if su < 0:
                su = 0
        return -1 if max_sum == float("-inf") else max_sum
