text1 = "abcde"
text2 = "ace"

prev = [0 for i in range(len(text2) + 1)]
curr = prev.copy()
for i in range(1, len(text1) + 1):
    for j in range(1, len(text2) + 1):
        if text1[i - 1] == text2[j - 1]:
            curr[j] = 1 + prev[j - 1]
        else:
            curr[j] = max(prev[j], curr[j - 1])
    prev = curr.copy()
print(prev[len(text2)])