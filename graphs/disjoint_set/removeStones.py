class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Initialize variables to track the maximum row and column indices across all stones
        mx_row = 0
        mx_col = 0
        n = len(stones)  # Total number of stones

        # Find the maximum row and column values among all stones to help define the 1D index range
        for i in range(len(stones)):
            mx_row = max(mx_row, stones[i][0])
            mx_col = max(mx_col, stones[i][1])

        # We flatten the 2D grid (row, column) into a 1D array to handle union-find operations.
        # The 1D representation ensures rows and columns are treated as nodes in a common space.
        # We set the 1D array size to mx_row + mx_col + 1 to cover all row and column nodes.
        ds_set = DisjointSet(mx_row + mx_col + 1)

        # Set to keep track of unique stone nodes (both row and column transformed to 1D)
        stone_nodes = set()

        # Flatten the 2D grid:
        # For each stone, consider its row and column positions as separate nodes in the 1D representation.
        for stone in stones:
            stone_row = stone[0]  # row index
            stone_col = stone[1] + 1 + mx_row  # flatten column index to 1D by shifting by max row + 1
            ds_set.union_set(stone_row, stone_col)  # Union row and column to connect them in the same component
            stone_nodes.add(stone_row)  # Add row as a unique node
            stone_nodes.add(stone_col)  # Add flattened column as a unique node

        # Count components: Find the number of unique root nodes to identify independent components
        cnt = 0
        for stone_node in stone_nodes:
            if ds_set.find(stone_node) == stone_node:  # Check if node is a root
                cnt += 1  # Count as a component if it is a unique root

        # Result: The maximum number of stones that can be removed is calculated as:
        # total stones - independent components
        # Each component represents one set of connected stones; we need at least one stone in each component.
        return n - cnt
