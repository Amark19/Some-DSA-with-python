class Solution:
    def countWays(self, n, s):
        dp = [[[-1, -1] for _ in range(n)] for _ in range(n)]

        def recur(i, j, isTrue):
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]

            ways = 0
            for k in range(i + 1, j, 2):
                left_true = recur(i, k - 1, 1)
                left_false = recur(i, k - 1, 0)
                right_true = recur(k + 1, j, 1)
                right_false = recur(k + 1, j, 0)

                if s[k] == "&":
                    if isTrue:
                        ways += left_true * right_true
                    else:
                        ways += left_true * right_false + left_false * right_true + left_false * right_false

                elif s[k] == "|":
                    if isTrue:
                        ways += left_true * right_true + left_true * right_false + left_false * right_true
                    else:
                        ways += left_false * right_false

                elif s[k] == "^":
                    if isTrue:
                        ways += left_true * right_false + left_false * right_true
                    else:
                        ways += left_true * right_true + left_false * right_false

            dp[i][j][isTrue] = ways
            return ways

        return recur(0, n - 1, 1)