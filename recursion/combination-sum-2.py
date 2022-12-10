class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        def subsequence(ls,index,target,ans):
            if index >= N or target < 0:
                return
            if target == 0:
                ans.append(ls.copy())
                return
            ls.append(candidates[index])
            subsequence(ls,index,target - candidates[index],ans)
            ls.remove(candidates[index])
            subsequence(ls,index + 1,target,ans)
        subsequence([],0,target,ans)
        print(ans)
        return ans
