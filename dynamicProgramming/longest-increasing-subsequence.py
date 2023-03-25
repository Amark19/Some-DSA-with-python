class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_arr = [1]*len(nums)
        for i in range(len(nums) - 1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp_arr[i] = max(dp_arr[i],1+dp_arr[j])
        return max(dp_arr)
