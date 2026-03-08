# Time & Space Complexity Cheatsheet

## Big O at a Glance
```
O(1)        - Constant      - Hash map lookup, array access
O(log n)    - Logarithmic   - Binary search
O(n)        - Linear        - Single loop, linear search
O(n log n)  - Linearithmic  - Merge sort, heap sort
O(n^2)      - Quadratic     - Nested loops, bubble sort
O(2^n)      - Exponential   - Recursion without memoization
O(n!)       - Factorial     - Permutations
```

## Data Structure Operations
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Map | - | O(1) | O(1) | O(1) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | - | O(n) | O(log n) | O(log n) |

## Sorting Algorithms
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble | O(n) | O(n^2) | O(n^2) | O(1) |
| Selection | O(n^2) | O(n^2) | O(n^2) | O(1) |
| Insertion | O(n) | O(n^2) | O(n^2) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick | O(n log n) | O(n log n) | O(n^2) | O(log n) |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) |

## Pattern Recognition
| If you see... | Think... |
|---------------|----------|
| Sorted array | Binary search, two pointer |
| Subarray/substring | Sliding window |
| Find pair/triplet | Two pointer, hash map |
| Top K / Kth | Heap |
| Tree traversal | DFS/BFS |
| Graph connectivity | BFS/DFS, Union-Find |
| Overlapping subproblems | DP |
| All possibilities | Backtracking |
| Optimize min/max | Greedy or DP |
