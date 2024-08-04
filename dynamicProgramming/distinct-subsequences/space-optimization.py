class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev = [0 for _ in range(len(t) + 1)]
        prev[0] = 1
        curr = prev.copy()
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr.copy()
        return prev[j]