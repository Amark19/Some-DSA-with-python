class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1, -1] for _ in range(len(prices))]

        def recur(idx, buy_state):
            if idx == len(prices):
                return 0
            if dp[idx][buy_state] != -1: return dp[idx][buy_state]
            if buy_state:
                profit = max(recur(idx + 1, 0) - prices[idx], 0 + recur(idx + 1, 1))
            else:
                profit = max(prices[idx] + recur(idx + 1, 1), 0 + recur(idx + 1, 0))
            dp[idx][buy_state] = profit
            return profit

        return recur(0, 1)