# Disjoint set
A Disjoint Set data structure, also known as Union-Find, is used to manage a collection of non-overlapping subsets. It’s efficient for keeping track of connected components, often in applications like graph algorithms, network connectivity, and image processing.

## Key Operations

- `Find`: Determines which subset a particular element belongs to. This operation is important for checking if two elements are in the same subset.
- `Union`: Joins two subsets into a single subset, merging their memberships.

## Implementation
Disjoint sets are typically implemented with two techniques for optimization:

- `Path Compression`: When finding the root of a subset, make nodes in the path point directly to the root, reducing the depth of the tree.
- `Union by Rank`: Always attach the smaller tree under the root of the larger tree, keeping the structure balanced and reducing search time.

## why do we find root while merging two nodes in disjoint set ?

If we didn’t find the root and merged nodes directly, two nodes that seem distinct might actually be part of the same connected component. 

Basically in a example of (1,2) , (2,3) , (4,5) our graph will look like 1-2-3 & 4-5
Now, if we want to merge (3,5) that will actually messed up merger & will make 1-2-3-4-5 which is wrong.