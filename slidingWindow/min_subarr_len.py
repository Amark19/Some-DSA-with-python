class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = float("inf")
        # for i in range(len(nums)):
        #     su = 0
        #     for j in range(i,len(nums)):
        #         su += nums[j]
        #         if su >= target:
        #             mn = min(mn,j - i + 1)
        #             break
        # return 0 if mn==float("inf") else mn
        left, right = 0, 0
        su = 0
        while right < len(nums) and left < len(nums):
            su += nums[right]
            if su >= target:
                while su >= target and left < len(nums):
                    mn = min(mn, right - left + 1)
                    su -= nums[left]
                    left += 1
            right += 1
        return 0 if mn == float("inf") else mn
