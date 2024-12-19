class Solution:
    def trap(self, height: List[int]) -> int:
        len_height = len(height)
        left_most_filled_arr = [0 for _ in range(len_height)]
        right_most_filled_arr = [0 for _ in range(len_height)]
        left_max, right_max, i, j = 0, 0, 0, len_height - 1
        for val in height:
            left_max = max(left_max, val)
            left_most_filled_arr[i] = left_max
            i += 1
        for val in height[::-1]:
            right_max = max(right_max, val)
            right_most_filled_arr[j] = right_max
            j -= 1
        stored_water = [0 for _ in range(len_height)]
        for i in range(len_height):
            stored_water[i] = min(left_most_filled_arr[i], right_most_filled_arr[i]) - height[i]
        return sum(stored_water)
