class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        def subsequence(ls,index,target,ans):
            if index >= N or target < 0:
                return
            if target == 0:
                #here is only one copy of ls flowing through the program.
                #So whenever result changes, it also reflects in ans.
                #That's why copying it breaks the chain and gives you the correct result
                ans.append(ls.copy())
                print(ans)
                return
            ls.append(candidates[index])
            subsequence(ls,index,target - candidates[index],ans)
            ls.remove(candidates[index])
            subsequence(ls,index + 1,target,ans)
        subsequence([],0,target,ans)
        print(ans)
        return ans
