class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {} #caching
        def min_dp(i):
            if i == len(days):
                return 0
            if i in dp: #do we have minimum value for value at i ? that we stored in dp
                return dp[i]

            dp[i] =float('inf')

            for d,c in zip([1,7,30],costs): # [1,7,30] is incremental factor
                '''
                dp[i] = min(dp[i],c + min_dp(i+d)])

                we can't do this cause it can go out of index & will not work properyly
                for an eg [1,2,8]
                at index 0 for 7 day pass it will directly jump to 0 + 7th index which does not exists
                so, we should have something to handle out of bound index,values
                '''

                j = i
                while j < len(days) and days[j] < days[i] + d:# handle next upcoming value
                    '''
                    [1,4,6]
                    at j=0 , 1<2 (for d == 1)
                    at j=1,4 < 2 break
                    so next value to pass is 4
                    '''
                    j += 1
                dp[i] = min(dp[i],c + min_dp(j))
            return dp[i]
        return min_dp(0)
