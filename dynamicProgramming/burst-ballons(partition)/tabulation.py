class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        can't follow top down approach instead we can use use bottomt up (not dp one but reg this problem)
        In an example of b1 b2 b3 b4 b5
        If b3 was the last best value that gives us the max
        that means b3 was exist in its previous iteration which could
        b1 b3, b2 b3, b3 b4, b3 b5
        that means we can partition an array to left & right that is b1 b2 & b4 b5

        So to select best value we can try out all the indices and make partitions
        """
        n = len(nums)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        """
        In memoization,
        i started from 0 -> n
        j started from n- > 0
        As tabulation is bottom up we will reverse this up
        """
        nums.insert(0, 1)
        nums.append(1)
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                mx = 0
                for k in range(i, j + 1):
                    collection = nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j]
                    mx = max(collection, mx)
                dp[i][j] = mx
        return dp[1][n]