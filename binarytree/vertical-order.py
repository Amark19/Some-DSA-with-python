# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        mapper = defaultdict(list)
        ans, ans1 = [], []
        q = [(root, 0)]
        mapper[0] = [[root.val, 0]]
        level = 1
        while q:
            for i in range(len(q)):
                node, ver = q[0][0], q[0][1]
                if node and node.left:
                    q.append((node.left, ver - 1, level))
                    mapper[ver - 1].append([node.left.val, level])
                    mapper[ver - 1].sort(key=lambda x: (x[1], x[0]))
                if node and node.right:
                    q.append((node.right, ver + 1, level))
                    mapper[ver + 1].append([node.right.val, level])
                    mapper[ver + 1].sort(key=lambda x: (x[1], x[0]))
                del q[0]
            level += 1
        # print(sorted(mapper.items()))
        for k in sorted(mapper.items()):
            ans.append(k[1])
        for i in range(len(ans)):
            tmp = []
            for j in range(len(ans[i])):
                tmp.append(ans[i][j][0])
            ans1.append(tmp)
        return ans1
