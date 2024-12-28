class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (if valid)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse left column (if valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
