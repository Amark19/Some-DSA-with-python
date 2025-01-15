class Solution:
    def numTrees(self, n: int) -> int:
        num_trees_dp = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total_trees = 0
            for root in range(1, nodes + 1):  # arrange roots
                left = root - 1
                right = nodes - root
                total_trees += num_trees_dp[left] * num_trees_dp[right]
            num_trees_dp[nodes] = total_trees
        return num_trees_dp[n]
