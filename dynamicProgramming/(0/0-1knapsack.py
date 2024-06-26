class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        def rec(idx,W,wt,val,dp):
            # base condition
            if idx == 0:
                if wt[0] <= W: # go from n to 0 & check whther I can add last element to bag or not
                    return val[0]
                return 0
            
            if dp[idx+1][W] != -1:return dp[idx+1][W]
            #take the value or not take the value
            not_tak = 0 + rec(idx - 1,W,wt,val,dp)
            tak = float('-inf')
            
            if wt[idx] <= W:
                tak = val[idx] + rec(idx -1,W - wt[idx],wt,val,dp)
            dp[idx+1][W]=max(not_tak,tak)
            return max(not_tak,tak)
        dp = [[-1 for _  in range(W+1)] for _ in range(n+1)]
        return rec(n-1,W,wt,val,dp)
