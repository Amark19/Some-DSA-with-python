# 1 2 3 -4 5 6
# 1 -> 1,1
# 2 -> 2,2
# 3 ->3,6
# -4 ->
nums = [1, 2, 3, -4, 5, 6]
res = max(nums)
cur_min, cur_max = 1, 1

for n in nums:
    if n == 0:
        cur_min, cur_max = 1, 1
        continue
    tmp = n * cur_max  # necessary because in cur_min cur_max value is changing
    cur_max = max(n * cur_max, n * cur_min, n)
    cur_min = min(tmp, n * cur_min,
                  n)  # we should also have extreme negative value cause if we have nxt value as -ve then extreme_negative * curr can make max_positive value
    res = max(res, cur_max)
print(res)