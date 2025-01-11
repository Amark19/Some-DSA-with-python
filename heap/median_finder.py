import heapq
class MedianFinder:

    """
    mx    mn
    1 2 | 3 4
    will be wanted max value from left side of arr
    and min value from right side of arr to calculate median
    """

    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to max-heap (left)
        heapq.heappush(self.left, -num)

        # Ensure all elements in `left` are <= all elements in `right`
        if self.left and self.right and (-self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # Balance the sizes of the heaps
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # If one heap has more elements, the median is the root of that heap
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]

        # If both heaps are balanced, the median is the average of their roots
        return (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
