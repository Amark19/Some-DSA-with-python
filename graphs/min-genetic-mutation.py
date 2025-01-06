class Solution:
    def buildAdjancencyList(self, bank, startGene):
        adj = defaultdict(list)
        for i in range(len(bank)):
            key1 = bank[i]
            for j in range(len(bank)):
                key2 = bank[j]
                count = 0
                for k in range(len(key2)):
                    if key1[k] != key2[k]:
                        count += 1
                if count == 1:
                    adj[key1].append(key2)
        for j in range(len(bank)):
            key2 = bank[j]
            count = 0
            for k in range(len(key2)):
                if startGene[k] != key2[k]:
                    count += 1
            if count == 1:
                adj[startGene].append(key2)
        return adj

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        adj = self.buildAdjancencyList(bank, startGene)
        que = [(startGene, 0)]
        vis = set()
        while que:
            node, layer = que[0]
            vis.add(node)
            del que[0]
            for val in adj[node]:
                if val not in vis:
                    if val == endGene:
                        return layer + 1
                    que.append((val, layer + 1))
        return -1
        # ofcourse this can be optimized by assigning A C G T a number
