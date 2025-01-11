import heapq    
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []
        for val in nums1:
            heapq.heappush(heap, (val + nums2[0], 0))
        count = 0
        while count < k and heap:
            su, pos = heapq.heappop(heap)
            num1 = su - nums2[pos]
            ans.append([num1, nums2[pos]])
            count += 1
            if pos + 1 < len(nums2):
                heapq.heappush(heap, (num1 + nums2[pos + 1], pos + 1))
        return ans
