class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m + n - 2  # m - 1 + n - 1
        '''
        if we observe the pattern then we came to know that we will always required m - 1 + n - 1 steps to reach to End.
        example: m = 3, n = 2
        1. r -> d -> d
        2. d -> d -> r
        3. d -> r -> d
        
        if m = 3,n = 5
        then d -> r -> r -> d -> d
        etc.. 

        so we just have to use combinations over here that mean we have to arrange the total steps such as m or n of them
        would d or r else r or d.
        rdd -> possible combinations 3C1 or 3C2
        '''
        count = 1
        for i in range(m - 1):
            count *= (total_steps - i) / (i + 1)
        print(count)
        return round(count)
