class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(nums):
            stack = []
            mx = float("-inf")
            for i in range(len(nums)):
                start = i
                # While stack is not empty AND top of stack is more than the current element
                while stack and stack[-1][1] > nums[i]:
                    # Pop the top element from the stack
                    index, height = stack.pop()
                    mx = max(mx, (i - index) * height)
                    start = index
                # Push the current element into the stack
                stack.append((start, nums[i]))
            for i, h in stack:
                mx = max(mx, h * (len(nums) - i))  # for all elements are in increasing order
            return mx

        row = len(matrix)
        col = len(matrix[0])
        height = [0] * col
        mx = float("-inf")
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            mx_area = largestRectangleArea(height)
            mx = max(mx_area, mx)
        return mx
