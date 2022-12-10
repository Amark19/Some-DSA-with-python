class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def subsequence(ls,idx):
            if idx >= len(nums):
                if ls not in ans:
                    ans.append(ls.copy())
                return
            ls.append(nums[idx])
            subsequence(ls,idx + 1)
            ls.remove(nums[idx])
            subsequence(ls,idx + 1)
        subsequence([],0)
        return ans
