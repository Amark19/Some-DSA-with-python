class Solution:
    def shortest_distance(self, matrix):
        # Code here
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1e8

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1e8:
                    matrix[i][j] = -1