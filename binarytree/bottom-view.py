from collections import defaultdict
        mapper = defaultdict(list)
        ans = []
        q = [(root,0)]
        mapper[0] = [root.data]
        while q:
            for i in range(len(q)):
                node = q[0][0]
                if node and node.left:
                    q.append((node.left,q[0][1] -1))
                    mapper[q[0][1] - 1].append(node.left.data)
                if node and node.right:
                    q.append((node.right,q[0][1] + 1))
                    mapper[q[0][1] + 1].append(node.right.data)
                del q[0]
        # print(sorted(mapper.items()))
        for k in sorted(mapper.items()):
            ans.append(k[1][-1])
        return ans
