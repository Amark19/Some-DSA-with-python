def FindMaxSum(self, a, n):
    def recur(arr, idx):
        if (idx == 0): return arr[idx]
        if (idx < 0): return 0
        should_consider = arr[idx] + recur(arr, idx - 2)
        not_consider = 0 + recur(arr, idx - 1)
        return max(should_consider, not_consider)

    return recur(a, n - 1)
