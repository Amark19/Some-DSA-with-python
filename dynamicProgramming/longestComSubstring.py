
def LCSubStr(X, Y, m, n):
	LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
	result = 0
	for i in range(1,m + 1):
		for j in range(1,n + 1):
			if (X[i-1] == Y[j-1]):
				LCSuff[i][j] = LCSuff[i-1][j-1] + 1
				result = max(result, LCSuff[i][j])
			else:
				LCSuff[i][j] = 0
	return result

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
	LCSubStr(X, Y, m, n))
