class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n,count = len(matrix),len(matrix[0]),0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1]) + 1
        for i in range(m):
            for j in range(n):
                count += matrix[i][j]
        return count

'''
explaination :- Dp approach

let example we have the input matrix as this : 
0 1 1 1 
1 1 1 1
0 1 1 1

focus on sq 1's matrices can be formed which has value of curre_index value

first row
0 1 1 1
let's start with 
0 -> 0
1 -> 1
1 -> 1
1-> 1

for 1st column as well the number of matrices stays same as the value of element

so we can traverse from row -> 1 and column -> 1(i.e 2nd column)
1 1 1
for 2nd 1(we have 1 itself & no other matrix) -> 1
0 1
1 [1]
3rd 1 -> 1 iteself & one 2x2 matrix that means(basically we r checking 3 elements upward,left-one,diagonally left one & checking minmum between that & then add one) -> 2
0 [1 1]
1 [1 [1]]
another possible combination is 2x3 but that is not square submatrix 0 1 1
                                                                     1 1 1
for 4th one (-> 1 itself and one square matrix) -> 2 
    1 [1 1]
    1 [1 [1]]                                                                    

3rd columns
1 1 1
for 1st one -> one itself -> 1
for 2nd one -> one itself + one sq -> 2
for 3rd one -> one itslef + one 2x2 sq + one 3x3 sq -> 3


equivalent matrix becomes 
0 1 1 1
1 1 2 2
0 1 2 3

return sum(matrix)
'''