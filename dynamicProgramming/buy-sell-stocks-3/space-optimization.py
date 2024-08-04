class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nex = [[0 for _ in range(3)] for _ in range(2)]
        curr = nex.copy()
        for idx in range(len(prices) - 1, -1, -1):
            for buy_state in range(2):
                for cap in range(1, 3):
                    if buy_state:
                        profit = max(nex[0][cap] - prices[idx], nex[1][cap])
                    else:
                        profit = max(nex[1][cap - 1] + prices[idx], nex[0][cap])
                    curr[buy_state][cap] = profit
            prev = curr
        return prev[1][2]