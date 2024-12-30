class Solution:
    def isValid(self, s: str) -> bool:
        open_pare = ["(","{","["]
        close_pare = [")","}","]"]
        st = []
        for i in range(len(s)):
            if s[i] in open_pare:
                st.append(s[i])
            elif len(st)!=0 and s[i] == close_pare[open_pare.index(st[-1])]:
                st.pop()
            else:
                return False
        if len(st) == 0:
            return True