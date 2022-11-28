class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till_now = -2134567
        max_end = 0
        for i in range(len(nums)):
            max_end+=nums[i]
            if max_till_now < max_end:
                max_till_now = max_end
            if max_end < 0:
                max_end = 0
        return max_till_now
