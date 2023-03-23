class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # storing states i.e any node value which repeating no need to call recursion call direct take values from it

        def recur(index,val):
            if index == len(nums):
                return 1 if target == val else 0
            if (index,val) in dp:
                return dp[(index,val)]
            '''
            aggegating result i.e no of possible values from left & right
            '''
            dp[(index,val)] = recur(index + 1 , val + nums[index]) + recur(index + 1,val - nums[index])

            return dp[(index,val)]
        
        return recur(0,0)
