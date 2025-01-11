class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1)
        left, right = 0, n1
        left_half = (n1 + n2 + 1) // 2
        full_size = n1 + n2
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = left_half - mid1
            l1, l2 = float("-inf"), float("-inf")
            r1, r2 = float("inf"), float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0: l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0: l2 = nums2[mid2 - 1]
            if l1 <= r2 and l2 <= r1:
                if full_size % 2:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1
        return 0


# refer striver video for O(min(log(m), log(n))) solution