# Bit Manipulation

## Basic Operations
| Operation | Syntax | Example |
|-----------|--------|---------|
| AND | a & b | Check if bit is set |
| OR | a \| b | Set a bit |
| XOR | a ^ b | Toggle / find unique |
| NOT | ~a | Flip all bits |
| Left Shift | a << n | Multiply by 2^n |
| Right Shift | a >> n | Divide by 2^n |

## Common Tricks
- `n & (n-1)` -> remove last set bit
- `n & (-n)` -> isolate last set bit
- `a ^ a = 0` -> find single number in array
- `n & 1` -> check odd/even

## Classic Problems
- Single Number (XOR all)
- Count set bits
- Power of 2 check
- Subsets using bitmask

## Problems Solved
<!-- Add links to your solved problems here -->
