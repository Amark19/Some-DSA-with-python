class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:  # should not be connected component
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mailMapping = {}
        n = len(accounts)
        ds_set = DisjointSet(n)
        for i in range(n):
            m = len(accounts[i])
            for j in range(1, m):
                mail = accounts[i][j]
                if mail not in mailMapping:
                    mailMapping[mail] = i
                else:
                    ds_set.union_set(mailMapping[mail], i)

        '''
        We have something like this 
        johnsmith@mail.com = 0
        john_newyork@mail.com = 0
        we found same mail as johnsmith@mail.com which is from node 1
        lets merge node 2 to 1 (where we already have same mail)
        1 -> 2
        from this now john00@mail.com will also have its root from 1 which will be merged
        '''

        mail_list = {}
        for mail, index in mailMapping.items():
            parent = ds_set.find(index)
            if parent not in mail_list:
                mail_list[parent] = []
                mail_list[parent].append(mail)
            else:
                mail_list[parent].append(mail)
        ans = []
        for index, mails in mail_list.items():
            temp = []
            temp.append(accounts[index][0])
            mails.sort()
            for mail in mails:
                temp.append(mail)
            ans.append(temp)
        return ans
