class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        def subsequence(ls,index,target):
            if index >= N or target < 0:
                return
            if target == 0:
                #here as we r using the same array and manipulating it we don't have different arrays/list which can consume different address
                #but here as we r using same address for ls so whenever ls is modifying it's value then ans also modifies it's value
                #so that's why we create copy which create new address/memory from which it will never modify again
                ans.append(ls.copy())
                return
            ls.append(candidates[index])
            subsequence(ls,index,target - candidates[index])
            ls.remove(candidates[index])
            subsequence(ls,index + 1,target)
        subsequence([],0,target)
        return ans
