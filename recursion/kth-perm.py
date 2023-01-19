class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        ans = ""
        numbers = [str(i) for i in range(1,n + 1)]
        fct = math.factorial(n-1)
        while n > 0:
            ans += numbers[((k-1)//fct)]
            k = (k)%fct
            numbers.remove(ans[-1])
            if n > 1:fct = fct//(n - 1)
            n -= 1
        return ans
        '''
        n = 4 k = 17
        basically go on finding ith postion
        so here for 1st
        if n == 4 that 1st series which start with 1 will have 6 perm(1234,1243,1324,1342,1423,1432)
                        same with 2nd,3rd,4th
        that means each series is of (n-1) permutations/factorial(24 is 4! to divide it into 4eqaul ways we have to give 6)
        so for k = 17
        first number will be 3 cause for 1(6seq) + 2(6seq) => 12
        ans = 3___ numbers[(17-1)//6)]

        for 2nd number we know that now for each number we have 2 permutation(cause we have to arrange in 3 numbers)i.e 1,2,4
        now we know that in 3rd series it's 5th number 13,14,15,16,17 & this 5tth sequence is of 4th number
        for 1 ->1,2(two sequence each)
            2 ->3,4
            4 ->5,6
        ans = 34__  numbers[(5-1)//2)]

        for 3rd number we only have 1 permutation for each number i.e
        for 1 only 1,2
            2 only 2,1
        that means we already are at 17th sequence now we can take 1st sequence
        ans = 341_ numbers[(0//2)]
        ans = 3412 numbers[(0//1)]
        '''
