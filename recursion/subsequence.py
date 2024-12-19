def subsequence(ls, idx):
    if idx >= len(arr):
        print(ls)
        return
    ls.append(arr[idx])  # 3
    subsequence(ls, idx + 1)  # taking elment
    ls.remove(arr[idx])
    subsequence(ls, idx + 1)  # not taking elment 


arr = [2, 5, 8, 11, 13]
subsequence([], 0)
