class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:return 0
        max_set,count,maxval = set(nums) , 0 , 0
        for num in max_set:
            if num - 1 not in max_set:
                count = 1
                curr_num = num
                while curr_num + 1 in max_set:
                    curr_num += 1
                    count += 1
                
                maxval = max(maxval,count)
        return maxval
