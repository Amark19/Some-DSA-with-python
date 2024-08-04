class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]

        def recur(idx, buy_state, cap):
            if cap == 0: return 0
            if idx == len(prices):
                return 0
            if dp[idx][buy_state][cap] != -1: return dp[idx][buy_state][cap]
            if buy_state:
                profit = max(recur(idx + 1, 0, cap) - prices[idx], recur(idx + 1, 1, cap))
            else:
                profit = max(recur(idx + 1, 1, cap - 1) + prices[idx], recur(idx + 1, 0, cap))
            dp[idx][buy_state][cap] = profit
            return dp[idx][buy_state][cap]

        return recur(0, 1, 2)