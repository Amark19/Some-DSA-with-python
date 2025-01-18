class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Store indices along with values to keep track of original positions
        nums_with_indices = [(num, idx) for idx, num in enumerate(nums)]
        # Result array to store the count of smaller elements
        result = [0] * len(nums)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    # Element from left is added; update result
                    result[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    # Element from right is smaller; increase right_count
                    right_count += 1
                    merged.append(right[j])
                    j += 1

            # Add remaining elements from left
            while i < len(left):
                result[left[i][1]] += right_count
                merged.append(left[i])
                i += 1

            # Add remaining elements from right
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        # Perform modified merge sort
        merge_sort(nums_with_indices)

        return result
