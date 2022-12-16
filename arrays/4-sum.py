class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans , su = [] , 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:#just continue with next iteration if prev & next val is same cause will be processing same target1
                continue
            target1 = target - nums[i]
            #find 3 such numbers whos sum is target1
            j = i + 1
            while j < len(nums):
                target2 = target1 - nums[j]#find 2 such numbers whose sum is target2
                l,r = j + 1,len(nums) - 1
                while l < r:
                    su = nums[l] + nums[r]
                    if target2 - su > 0: l += 1
                    elif target2 - su < 0: r -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:l += 1
                j += 1
                while j < len(nums) and nums[j-1] ==  nums[j] : j+=1
            
        return ans
        '''
        for -2 -1 0 0 1 2
        target1 = 0 - (-2) = 2
        target2 = 2 - (-1) = 3
        now we have two find two such number whose sum is 3 which simply means we found one solution 3 - 3 =0
        & some basic steps to avoid adding duplicates
        '''
