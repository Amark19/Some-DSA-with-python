class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums): return -1

        # painter's partition problem
        def findValidPartition(value):
            splits = 1
            total_num = 0
            for num in nums:
                if total_num + num > value:
                    splits += 1
                    total_num = num
                else:
                    total_num += num
            return splits

        low = max(nums)
        high = sum(nums)
        # for val in range(low,high+1):
        #     if findValidPartition(val) == k:
        #         return val
        while low <= high:
            mid = (low + high) // 2
            curr_split = findValidPartition(mid)
            if curr_split > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
