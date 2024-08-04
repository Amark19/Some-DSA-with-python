class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices) + 1)]
        for idx in range(len(prices) - 1, -1, -1):
            for buy_state in range(2):
                for cap in range(1, 3):
                    if buy_state:
                        profit = max(dp[idx + 1][0][cap] - prices[idx], dp[idx + 1][1][cap])
                    else:
                        profit = max(dp[idx + 1][1][cap - 1] + prices[idx], dp[idx + 1][0][cap])
                    dp[idx][buy_state][cap] = profit
        return dp[0][1][2]