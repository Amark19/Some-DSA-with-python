class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * len(s)
        wordDict_set = set(wordDict)

        def recursion(index):
            if index >= len(s):
                return True
            if dp[index] != -1:
                return dp[index]
            tmp_string = ""
            for i in range(index, len(s)):
                tmp_string += s[i]
                len_tmp = len(tmp_string)
                if tmp_string in wordDict_set and recursion(i + 1):
                    dp[index] = True
                    return True
            dp[index] = False
            return False

        return recursion(0)
