class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            nn = abs(n)
        else:
            nn = n
        while nn > 0:
            if nn % 2 != 0:
                ans = ans * x
                nn -= 1
            else:
                x *= x
                nn /= 2
        if n < 0:
            return 1 / (ans)
        else:
            return ans

"""
2^10 = (2x2)^5
4^5 = 4x4^4
4^4 = 16x16
16^2 = 256
multiply 4 to 256 = 1024
"""