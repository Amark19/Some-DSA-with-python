class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1] * (n + 1)  # Memoization array

        def recursion(number):
            if number == 0:
                return False  # the current player loses because no valid move is possible.

            if dp[number] != -1:
                return dp[number]  # Return memoized result

            i = 1
            while i * i <= number:
                # If the opponent loses after removing `i * i` stones, current player wins
                if not recursion(number - i * i):
                    dp[number] = True
                    return True
                i += 1

            dp[number] = False  # Otherwise, current player loses
            return False

        return recursion(n)
