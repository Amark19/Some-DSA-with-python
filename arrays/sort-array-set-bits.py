from operator import itemgetter
arr = [0,1,2,3,4,5,6,7,8]
ls,ans = [],[]
for val in arr:
    ls.append((val,bin(val)[2:].count('1')))
for val in sorted(ls,key=itemgetter(1,0)):
    ans.append(val[0])
print(ans)