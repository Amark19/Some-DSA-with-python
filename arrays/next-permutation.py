class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums == sorted(nums)[::-1]:
            nums.reverse()
        elif nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[i - 1]:
                    idx = i - 1
                    break
            for j in range(idx + 1, len(nums)):
                if nums[j] > nums[idx]:
                    idx1 = j
            # print(idx,idx1)
            nums[idx1], nums[idx] = nums[idx], nums[idx1]
            # print(nums)
            i, j = idx + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


'''
intuition is so easy
let's take an example of
1 3 5 4 2
if we see from backwards 5 4 2  is something reversly sorted that means it have reached to its max value so no further permutation is possible for this 3
(as next permutation for 3 2 1 is not possible because it' alreadt the last one)
(traverse from back find an element which is greater than its previous)
now we know that max after 3 is reached so we have to find the upcoming greater element than 3 which is 4
& let's swap that which would become 1 4 5 3 2
but again it maximum after 4 (5 3 2) & we want to find very first permutation for 1->4 then can we reverse this after 4?5 3 2 => 2 3 5
ans would become 1 4 2 3 5
'''
