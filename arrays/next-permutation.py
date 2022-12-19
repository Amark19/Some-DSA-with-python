class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums == sorted(nums)[::-1]:
            nums.reverse()
        elif nums[-1] > nums[-2] :nums[-1],nums[-2] = nums[-2],nums[-1]
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[i-1]:
                    idx = i-1
                    break
            for j in range(idx + 1,len(nums)):
                if nums[j] > nums[idx] :
                    idx1 = j
            # print(idx,idx1)
            nums[idx1],nums[idx] = nums[idx],nums[idx1]
            # print(nums)
            i,j = idx + 1,len(nums) - 1
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1