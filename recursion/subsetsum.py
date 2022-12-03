class subset:
    def __init__(self):
        self.ans = []

    def subsequence(self, ls, idx):
        if idx >= len(arr):
            self.ans.append(sum(ls))
            return
        ls.append(arr[idx]) # 3
        self.subsequence(ls, idx + 1)  # taking elment
        ls.remove(arr[idx])
        self.subsequence(ls, idx + 1)  # not taking elment 


arr = [ 2,5,8,11,13]
obj = subset()
obj.subsequence([], 0)
print(obj.ans)
