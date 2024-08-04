def longestPalindrome(self, s: str) -> str:
    # babad
    # for a
    # first check a then bab
    # odd finish,now even
    # ab then baba
    # for b....
    def palindrome(l, r, pall_len, pall):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > pall_len:
                pall_len = r - l + 1
                pall = s[l:r + 1]
            l -= 1
            r += 1
        return pall, pall_len

    pall = ""
    pall_len = 0
    for i in range(len(s)):
        pall, pall_len = palindrome(i, i, pall_len, pall)  # check for odd
        pall, pall_len = palindrome(i, i + 1, pall_len, pall)  # then check for even
    return pall

    ##some optimizations
    def palindrome(l, r, pall_len, pall):
        res_l, res_r = l, r
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > pall_len:
                pall_len = r - l + 1
                res_l, res_r = l, r
            l -= 1
            r += 1
        if (res_r - res_l + 1) >= pall_len and l != res_l and r != res_r:
            pall = s[res_l:res_r + 1]
        return pall, pall_len

    pall, pall_len = "", 0
    for i in range(len(s)):
        pall, pall_len = palindrome(i, i, pall_len, pall)  # check for odd
        pall, pall_len = palindrome(i, i + 1, pall_len, pall)  # then check for even
    return pall