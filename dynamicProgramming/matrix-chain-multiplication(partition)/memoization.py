class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        # why 2 indices ??
        # To indicate block of an array from i -> j
        # that is AB CD
        # that is 40x20 20x30 + 30x10 10x30
        # TO multiply AB we require minimum operations 40x20x30 in matrix
        dp = [[-1 for _ in range(N)] for _ in range(N)]

        def recur(i, j):
            if i == j:
                return 0  # we only have one block so no operations required
            if dp[i][j] != -1: return dp[i][j]
            mn = float("inf")
            # Lets make partitions
            for k in range(i, j):
                # break it from i,k & k+1,j
                # That is for indices (1,4)
                # we could break it to k==1 (1,1) -> (2,4) A (BCD)
                # can break (AB)(CD) & (ABC)(D)

                steps = arr[i - 1] * arr[k] * arr[j] + recur(i, k) + recur(k + 1, j)
                mn = min(mn, steps)
            dp[i][j] = mn
            return mn

        return recur(1, N - 1)


"""
Time Complexity: O(N^3) (N^2 for dp array and N for the loop)
Space Complexity: O(N^2) for dp array
"""