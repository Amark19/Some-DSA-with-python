nums = [14, 9, 8, 4, 3, 2]
total_su = sum(nums)


def recur(idx, su):
    if idx == 0: return su + nums[0] == total_su - su + nums[0]
    if su == total_su - su: return True
    take = recur(idx - 1, su + nums[idx])
    not_take = recur(idx - 1, su)
    return take or not_take


n = len(nums)
print(recur(n - 1, 0))