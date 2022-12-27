class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def pe(ls,ans,arr):
            if len(ls) == len(nums):
                ans.append(ls.copy())
                return
            for i in range(0,len(nums)):
                if not arr[i]:
                    ls.append(nums[i])
                    arr[i] = 1
                    print(ls,arr)
                    pe(ls,ans,arr)
                    ls.remove(nums[i])
                    arr[i] = 0
        ans = []
        pe([],ans,[0 for i in range(len(nums))])
        return ans
