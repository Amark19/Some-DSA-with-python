class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        def subsequence(ls,idx,ans):
            if idx >= len(nums):
                ans.append(ls.copy())
                # print(ls , ans)
                return
            ls.append(nums[idx])
            subsequence(ls,idx + 1,ans)
            ls.remove(nums[idx])
            subsequence(ls,idx + 1,ans)
        subsequence([],0,ans)
        return ans
