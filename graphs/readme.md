# Tips and Tricks

## Unconnected Components

### Matrix

- For matrix run a loop for each cell and if cell is 1 then run a DFS/BFS to find all connected cells and mark them as visited.(O(V^2))
- Count the number of DFS/BFS calls.
    
### Graph (adjacency list)

- Run a DFS/BFS for each node and mark all connected nodes as visited.(O(V+E))