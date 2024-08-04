class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        for idx in range(len(prices) - 1, -1, -1):
            for buy_state in range(2):
                if buy_state:
                    profit = max(dp[idx + 1][0] - prices[idx], 0 + dp[idx + 1][1])
                else:
                    profit = max(prices[idx] + dp[idx + 1][1], 0 + dp[idx + 1][0])
                dp[idx][buy_state] = profit
        return dp[idx][buy_state]