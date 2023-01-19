class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def isPallindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        def part(idx):
            if idx >= len(s):
                res.append(path.copy())
            for j in range(idx,len(s)):
                if isPallindrome(s[idx:j+1]):
                    path.append(s[idx:j+1])
                    part(j+1)
                    path.pop()
        part(0)
        return res
        '''
        example string :- aabb
        first target individual characters like
        a,a
        a,a,b
        a,a,b,b
        then it backtracks pop last element from ds i.e b so a,a,b
        then tries out current idx to jth index whther its pallindrome or not
        so for we get a,a,bb
        1.tries out individual then subtrings 
        '''
