class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: continue  # continue to next iteration if prev & next is equal
            l, r = i + 1, len(nums) - 1
            while l < r:  ##finding all nums[i],nums[j] for a
                su = a + nums[l] + nums[r]
                if su > 0:
                    r -= 1
                elif su < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1  # update l or r pointer to avoid infinite loop
                    while nums[l] == nums[
                        l - 1] and l < r: l += 1  # if l & l-1 of nums equal then keep updating l pointer
        return ans
