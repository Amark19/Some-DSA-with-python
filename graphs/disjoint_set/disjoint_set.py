class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

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
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def print_structure(self):
        # Display the current structure of the sets
        structure = {}
        for i in range(1, len(self.parent)):
            root = self.find(i)
            if root in structure:
                structure[root].append(i)
            else:
                structure[root] = [i]

        # Print the set structure in a tree-like format
        for root, nodes in structure.items():
            print(f"{root}: " + " -> ".join(map(str, nodes)))


# Initialize disjoint set with 5 elements (1 to 5)
ds = DisjointSet(5)

# Step 1: Union(1, 2)
ds.union_set(1, 2)
print("After Union(1, 2):")
ds.print_structure()

# Step 2: Union(3, 4)
ds.union_set(3, 4)
print("\nAfter Union(3, 4):")
ds.print_structure()

# Step 3: Union(2, 3)
ds.union_set(2, 3)
print("\nAfter Union(2, 3):")

ds.print_structure()

# Step 4: Union(4, 5)
ds.union_set(4, 5)
print("\nAfter Union(4, 5):")
ds.print_structure()
