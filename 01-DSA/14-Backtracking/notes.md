# Backtracking

## Core Idea
- Try all possibilities, backtrack when a choice doesn't lead to solution
- Extension of recursion with pruning

## Template
```
def backtrack(state, choices):
    if is_goal(state):
        add to results
        return
    for choice in choices:
        if is_valid(choice):
            make choice
            backtrack(new_state, remaining_choices)
            undo choice  # backtrack
```

## Classic Problems
- N-Queens
- Sudoku Solver
- Permutations / Combinations
- Subset Sum
- Word Search
- Palindrome Partitioning

## Problems Solved
<!-- Add links to your solved problems here -->
