class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        next_warmer_temperatures = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                next_warmer_temperatures[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return next_warmer_temperatures
