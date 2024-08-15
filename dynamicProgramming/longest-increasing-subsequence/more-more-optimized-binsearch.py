class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        random_shit = []
        random_shit.append(nums[0])

        def binary_search_lower_bound(low, high, arr, ele):
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < ele:
                    low = mid + 1
                else:
                    high = mid
            return low

        random_shit_len = 0
        for val in range(1, len(nums)):
            if nums[val] > random_shit[-1]:
                random_shit.append(nums[val])
                random_shit_len += 1
            else:
                given_index = binary_search_lower_bound(0, random_shit_len, random_shit, nums[val])
                random_shit[given_index] = nums[val]
        return len(random_shit)