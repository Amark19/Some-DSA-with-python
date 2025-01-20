def maxCoins(self, nums: List[int]) -> int:
    """
    can't follow top down approach instead we can use use bottomt up (not dp one but reg this problem)
    Why not top down ??
    exmaple 3 1 5 8
    Lets consider best value is 5
    burst out 5 array becomes 3 1 5(canceled) 8
    but can't partiion it to 3 1 & 8 as 1,3 can be dependent on 8
    SO, we can't follow top down approach
    In an example of b1 b2 b3 b4 b5
    If b3 was the last best value that gives us the max
    that means b3 was exist in its previous iteration which could
    b1 b3, b2 b3, b3 b4, b3 b5
    that means we can partition an array to left & right that is b1 b2 & b4 b5

    So to select best value we can try out all the indices and make partitions
    """
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def recur(i, j):
        if i > j: return 0
        if dp[i][j] != -1: return dp[i][j]
        mx = float("-inf")
        for k in range(i, j + 1):
            collection = nums[i - 1] * nums[k] * nums[j + 1] + recur(i, k - 1) + recur(k + 1, j)
            mx = max(collection, mx)
        dp[i][j] = mx
        return mx

    nums.insert(0, 1)
    nums.append(1)
    return recur(1, n)
