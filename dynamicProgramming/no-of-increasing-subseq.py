nums = [1, 3, 5, 4, 7]
dp_arr = [1] * len(nums)
count = dp_arr.copy()
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[i] > nums[j]:
            if dp_arr[i] == dp_arr[j] + 1:
                count[i] += count[j]  # Increment count only when a new LIS of length dp[i] is found
            elif dp_arr[i] < dp_arr[j] + 1:
                dp_arr[i] = dp_arr[j] + 1
                count[i] = count[j]
print(dp_arr)
print(count)
max_dp = max(dp_arr)
cnt = 0
for val in range(len(dp_arr)):
    if max_dp == dp_arr[val]:
        cnt += count[val]

print( cnt)