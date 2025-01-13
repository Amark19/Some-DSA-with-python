class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0  # opening brackets
        for val in s:
            if val == "(":
                left_max += 1
                left_min += 1
            elif val == ")":
                left_max -= 1
                left_min -= 1
            else:
                left_max += 1
                left_min -= 1
            if left_min < 0:
                left_min = 0
            if left_max < 0:
                return False
        return left_min == 0
