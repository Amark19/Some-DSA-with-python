def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
    def traverseAndFormString(dp):
        i = len(text1)
        j = len(text2)
        formString = ""
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                formString += text1[i - 1]
                i -= 1
                j -= 1
            elif dp[i][j - 1] > dp[i - 1][j]:
                formString += text2[j - 1]
                j -= 1
            else:
                formString += text1[i - 1]
                i -= 1
        while i > 0:
            formString += text1[i - 1]
            i -= 1
        while j > 0:
            formString += text2[j - 1]
            j -= 1
        return formString[::-1]

    dp_arr = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
            else:
                dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
    return traverseAndFormString(dp_arr)