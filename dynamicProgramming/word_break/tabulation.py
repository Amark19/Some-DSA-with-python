class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        wordDict_set = set(wordDict)
        dp[-1] = True
        for index in range(len(s) - 1, -1, -1):
            tmp_string = ""
            for i in range(index, len(s)):
                tmp_string += s[i]
                len_tmp = len(tmp_string)
                if tmp_string in wordDict_set and dp[i + 1]:
                    dp[index] = True
                    break
        return dp[0]
