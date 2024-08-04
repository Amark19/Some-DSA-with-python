class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = [False for _ in range(len(p) + 1)]
        curr = prev.copy()
        prev[0] = True
        for j in range(1, len(p) + 1):
            ok = True
            for k in range(1, j + 1):
                if p[k - 1] != "*":
                    ok = False
                    break
            prev[j] = ok
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    curr[j] = prev[j - 1]
                elif p[j - 1] == "*":
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False
            prev = curr.copy()
        return prev[len(p)]