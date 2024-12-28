from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = len(t)
        t_counter = Counter(t)
        left = 0
        count = 0
        min_len = float("inf")
        s_index = -1

        for right in range(len(s)):
            char = s[right]

            if char in t_counter:
                if t_counter[char] > 0:
                    count += 1
                t_counter[char] -= 1

            # When we have a valid window
            while count == t_count:
                # Update minimum window size
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    s_index = left

                # Shrink the window from the left
                left_char = s[left]
                if left_char in t_counter:
                    t_counter[left_char] += 1
                    if t_counter[left_char] > 0:
                        count -= 1
                left += 1

        return "" if s_index == -1 else s[s_index:s_index + min_len]
