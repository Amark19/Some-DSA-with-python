class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        ans = []
        def subsequence(ls,index,target):
            if index >= N or target < 0:
                if target == 0:
                    ans.append(ls.copy())
                return
            if target == 0:
                ans.append(ls.copy())
                return
            ls.append(candidates[index])
            subsequence(ls,index + 1,target - candidates[index])
            ls.remove(candidates[index])
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:index+=1
            subsequence(ls,index + 1,target)
        subsequence([],0,target)
        return ans
