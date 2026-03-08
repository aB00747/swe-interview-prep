# Ultimate_60_Day_DSA_Roadmap_Notion

# 🎯 THE 1% DSA MASTERY ROADMAP

## 60-Day Intensive Program to Crack FAANG & Top Product Companies

---

## 🧠 YOUR SITUATION ANALYSIS

### Current Status

- [x]  3+ years Full Stack Developer experience
- [x]  Strong debugging & problem-solving skills
- [x]  Jobless = Full-time focus available
- [ ]  Interview-ready DSA knowledge
- [ ]  Pattern recognition muscle
- [ ]  30-45 min problem-solving speed

### Your Advantage

You already know **how to code**. You just need to train **pattern recognition** for interviews.

---

## 📅 DAILY SCHEDULE (Jobless = Aggressive Mode)

```
09:00 - 10:30 → Session 1: Learn New Pattern (90 min)
10:30 - 10:45 → Break (15 min)
10:45 - 13:00 → Session 2: Solve Problems 2-3 (135 min)
13:00 - 14:00 → Lunch Break (60 min)
14:00 - 15:30 → Session 3: Review & Deep Dive (90 min)
15:30 - 15:45 → Break (15 min)
15:45 - 17:00 → Session 4: Previous Day Revision (75 min)
17:00 - 18:00 → Optional: Mock Interview / Contest (60 min)

Evening:
18:00 - 19:00 → Dinner & Rest
19:00 - 20:00 → System Design (starts Week 5)
20:00 - 21:00 → Free Time / Relaxation
```

**Total Study Time:** 5-6 hours focused work
**Weekly Off:** Sunday (complete rest or light revision)

---

## 🎯 SUCCESS METRICS TO TRACK

### Weekly Goals

- [ ]  Week 1: 25+ problems solved, 6 patterns mastered
- [ ]  Week 2: 50+ total problems, 12 patterns mastered
- [ ]  Week 3: 75+ total problems, confidence in Linked Lists
- [ ]  Week 4: 100+ total problems, Trees & basic Graphs
- [ ]  Week 5: 130+ total problems, Advanced patterns
- [ ]  Week 6: 160+ total problems, DP fundamentals
- [ ]  Week 7: 190+ total problems, Backtracking mastery
- [ ]  Week 8: 220+ total problems, Mock interview ready

### Daily Tracking (Mark After Each Day)

Rate yourself 1-5 for each:
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐

---

# 📘 PHASE 1: FOUNDATIONS & FUNDAMENTALS (Days 1-14)

## 🏁 WEEK 1: Core Array Patterns (Days 1-7)

---

### DAY 1: Time & Space Complexity ⏱️

**🎯 Goal:** Understand Big O notation - foundation of all interviews

**📚 Learn (90 min):**

- [ ]  Watch: Abdul Bari’s Asymptotic Notations (30 min)
- [ ]  Read: Big-O Cheat Sheet website (20 min)
- [ ]  Study: Common complexities O(1), O(log n), O(n), O(n log n), O(n²)
- [ ]  Practice: Analyze complexity of your Laravel code examples

**💡 Why This Matters:**
Every single interview starts with “What’s the time/space complexity?”
If you can’t answer this, you fail immediately.

**🧠 Key Concepts:**

- [x]  Big O = Worst case (upper bound)
- [ ]  Big Ω = Best case (lower bound)
- [ ]  Big Θ = Average case (tight bound)
- [ ]  Space complexity = Extra memory used (excluding input)

**📝 Practice (2 hours):**

- [x]  Write complexities for: for loop, nested loop, recursion, binary search
- [x]  Analyze 5 code snippets and determine their Big O

**✅ Achievement Unlocked:**
Can analyze any code’s time/space complexity in 30 seconds

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐

---

### DAY 2: Arrays + Two Pointers Pattern 🎯

**🎯 Goal:** Master the Two Pointer technique - 25% of interviews use this

**📚 Learn (90 min):**

- [ ]  Watch: NeetCode’s Two Pointers explanation
- [ ]  Read: Pattern recognition guide
- [ ]  Understand: When to use left-right vs fast-slow pointers

**🔑 Pattern Template:**

```
Two Pointers Pattern:
├─ Use when: Array is SORTED or you need pairs/triplets
├─ Approach: Left pointer (0), Right pointer (n-1)
└─ Move: Based on condition (sum too small? move left++, too big? move right--)

Time: O(n) | Space: O(1)
```

**💡 When to Use:**
- ✅ Sorted array problems
- ✅ Finding pairs/triplets with specific sum
- ✅ Reversing/rearranging elements
- ✅ Removing duplicates in-place

**📝 Problems (3 hours):**

### Easy Problems (Warmup)

- [x]  **LC 26** - Remove Duplicates from Sorted Array
    - Pattern: Two pointers (slow-fast)
    - Learning: In-place modification
    - Time: 15 min target
- [x]  **LC 283** - Move Zeroes
    - Pattern: Two pointers
    - Learning: Partitioning array
    - Time: 15 min target

### Medium Problems (Core Practice)

- [x]  **LC 167** - Two Sum II (Input Array Is Sorted) ⭐
    - Pattern: Two pointers (left-right)
    - Learning: Binary search alternative
    - Time: 20 min target
    - **WHY IMPORTANT:** Foundation for 3Sum, 4Sum
- [ ]  **LC 15** - 3Sum ⭐⭐⭐
    - Pattern: Two pointers + fixing one element
    - Learning: Avoiding duplicates
    - Time: 30 min target
    - **WHY IMPORTANT:** Most asked Amazon problem

**🔄 Revision (90 min):**
- [ ] Re-solve all 4 problems WITHOUT looking at solutions
- [ ] Write down the pattern template in your own words
- [ ] Explain approach to rubber duck/mirror before coding

**✅ Achievement Unlocked:**
Recognize Two Pointer pattern instantly in any problem

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 3: Hashing (HashMap/HashSet) 🗂️

**🎯 Goal:** Master HashMap - 30% of Easy-Medium problems need this

**📚 Learn (90 min):**
- [ ] Watch: HashMap internal working video
- [ ] Understand: Hash function, collision handling (chaining/open addressing)
- [ ] Learn: When to use HashMap vs HashSet vs Array

**🔑 Pattern Template:**

```
HashMap Pattern:
├─ Use when: Need O(1) lookup, counting frequency, tracking "seen before"
├─ Typical structure: Map<value, index> or Map<value, frequency>
└─ Common operations: containsKey(), get(), put()

Time: O(n) | Space: O(n)
```

**💡 When to Use:**
- ✅ “Find pair with sum X” → Store complements
- ✅ Count frequencies → Map<element, count>
- ✅ Check if element seen before → HashSet
- ✅ Group by property → Map<property, List>

**📝 Problems (3 hours):**

### The Most Asked Problem Ever

- [ ]  **LC 1** - Two Sum ⭐⭐⭐
    - Pattern: HashMap to store complements
    - Learning: One-pass solution
    - Time: 15 min target
    - **WHY CRITICAL:** Asked in 80% of first-round interviews
    - **Optimization:** Brute force O(n²) → HashMap O(n)

### Easy Problems

- [ ]  **LC 217** - Contains Duplicate
    - Pattern: HashSet for tracking
    - Learning: Set vs Map usage
    - Time: 10 min target
- [ ]  **LC 383** - Ransom Note
    - Pattern: Frequency map
    - Learning: Character counting
    - Time: 15 min target

### Medium Problems (Google/Facebook Favorites)

- [ ]  **LC 49** - Group Anagrams ⭐⭐
    - Pattern: HashMap with sorted string as key
    - Learning: Grouping by property
    - Time: 25 min target
    - **WHY IMPORTANT:** Tests string + hashing together
- [ ]  **LC 128** - Longest Consecutive Sequence ⭐⭐
    - Pattern: HashSet for O(1) lookup
    - Learning: Smart sequence building
    - Time: 30 min target
    - **WHY IMPORTANT:** Shows optimization thinking

**🔄 Revision (90 min):**
- [ ] Re-solve LC 1 in 5 minutes (must be automatic)
- [ ] Re-solve LC 49 and LC 128 without hints
- [ ] Write down when to use HashMap vs HashSet vs Array

**✅ Achievement Unlocked:**
Never write nested loops when HashMap solves it in O(n)

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 4: Prefix Sum Pattern 📊

**🎯 Goal:** Convert O(n²) range queries to O(n) using preprocessing

**📚 Learn (90 min):**
- [ ] Watch: Prefix sum explanation with examples
- [ ] Understand: Cumulative sum concept
- [ ] Learn: How prefix sum eliminates nested loops

**🔑 Pattern Template:**

```
Prefix Sum Pattern:
├─ Preprocessing: prefixSum[i] = sum of elements [0...i]
├─ Range sum [L, R] = prefixSum[R] - prefixSum[L-1]
├─ Use when: Multiple subarray sum queries
└─ Variation: Use HashMap to store prefix sums

Time: O(n) preprocessing + O(1) per query | Space: O(n)
```

**💡 When to Use:**
- ✅ Subarray sum problems
- ✅ Range sum queries
- ✅ Finding pivot index
- ✅ Product except self (prefix + suffix)

**📝 Problems (3 hours):**

### Easy (Build Foundation)

- [ ]  **LC 303** - Range Sum Query - Immutable
    - Pattern: Basic prefix sum array
    - Learning: Preprocessing concept
    - Time: 15 min target
- [ ]  **LC 724** - Find Pivot Index
    - Pattern: Prefix sum from left and right
    - Learning: Two-pass technique
    - Time: 20 min target

### Medium (Interview Standard)

- [ ]  **LC 560** - Subarray Sum Equals K ⭐⭐⭐
    - Pattern: Prefix sum + HashMap
    - Learning: Continuous subarray problems
    - Time: 30 min target
    - **WHY CRITICAL:** Combines two patterns (prefix + hash)
- [ ]  **LC 523** - Continuous Subarray Sum ⭐
    - Pattern: Prefix sum + modulo + HashMap
    - Learning: Mathematical optimization
    - Time: 35 min target
- [ ]  **LC 238** - Product of Array Except Self ⭐⭐
    - Pattern: Prefix + Suffix product
    - Learning: Space optimization
    - Time: 25 min target
    - **WHY IMPORTANT:** No division constraint

**🔄 Revision (90 min):**
- [ ] Draw prefix sum array for [1,2,3,4,5] and calculate range sums
- [ ] Re-solve LC 560 (critical for interviews)
- [ ] Explain why HashMap needed in subarray sum problems

**✅ Achievement Unlocked:**
Convert O(n²) brute force to O(n) using prefix sum

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 5: Sliding Window - Fixed Size 🪟

**🎯 Goal:** Master fixed-size window optimization

**📚 Learn (90 min):**
- [ ] Watch: Sliding window visualization
- [ ] Understand: Add right, remove left technique
- [ ] Learn: Why it’s O(n) not O(n*k)

**🔑 Pattern Template:**

```
Fixed Sliding Window:
├─ Window size = K (constant)
├─ Step 1: Calculate first window sum/condition
├─ Step 2: Slide → add arr[right], remove arr[left]
├─ Step 3: Update max/min as you slide
└─ Move both pointers together

Time: O(n) | Space: O(1)
```

**💡 When to Use:**
- ✅ “Maximum/minimum in subarray of size K”
- ✅ “Average/sum of K consecutive elements”
- ✅ Fixed-size substring problems

**📝 Problems (3 hours):**

### Easy (Pattern Recognition)

- [ ]  **LC 643** - Maximum Average Subarray I
    - Pattern: Fixed window, track sum
    - Learning: Basic sliding
    - Time: 15 min target
- [ ]  **LC 1343** - Number of Sub-arrays of Size K and Average ≥ Threshold
    - Pattern: Fixed window + condition
    - Learning: Counting technique
    - Time: 20 min target

### Medium (Build Mastery)

- [ ]  **LC 1004** - Max Consecutive Ones III ⭐
    - Pattern: Fixed window with flip count
    - Learning: Constraint handling
    - Time: 25 min target
- [ ]  **LC 567** - Permutation in String ⭐⭐
    - Pattern: Fixed window + frequency match
    - Learning: Anagram detection in window
    - Time: 30 min target
    - **WHY IMPORTANT:** Combines window + hashing

**🔄 Revision (90 min):**
- [ ] Re-solve LC 567 (critical pattern)
- [ ] Practice: Given array, find max sum of K consecutive elements
- [ ] Write template code for fixed sliding window

**✅ Achievement Unlocked:**
Can solve any fixed-window problem in 10 minutes

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 6: Sliding Window - Variable Size 🎢

**🎯 Goal:** Master dynamic window expansion/shrinking - Google/Microsoft favorite

**📚 Learn (90 min):**
- [ ] Watch: Variable window pattern explanation
- [ ] Understand: When to expand vs shrink
- [ ] Learn: Template for “longest/shortest” problems

**🔑 Pattern Template:**

```
Variable Sliding Window:
├─ Expand: Move right pointer, add to window
├─ Shrink: While condition violated, move left pointer
├─ Track: Max/min length during valid windows
└─ Two nested loops BUT still O(n) total

Pattern:
while right < n:
    add arr[right] to window
    while window invalid:
        remove arr[left] from window
        left++
    update result if window valid
    right++

Time: O(n) | Space: O(1) or O(k) for tracking
```

**💡 When to Use:**
- ✅ “Longest substring with condition”
- ✅ “Minimum window containing X”
- ✅ “Max length subarray with constraint”

**📝 Problems (3 hours):**

### Medium (Foundation)

- [ ]  **LC 3** - Longest Substring Without Repeating Characters ⭐⭐⭐
    - Pattern: Variable window + HashSet
    - Learning: Shrinking when duplicate found
    - Time: 25 min target
    - **WHY CRITICAL:** #1 Most asked medium problem
- [ ]  **LC 209** - Minimum Size Subarray Sum ⭐
    - Pattern: Variable window + sum tracking
    - Learning: Minimize window size
    - Time: 20 min target

### Medium-Hard (Master Level)

- [ ]  **LC 424** - Longest Repeating Character Replacement ⭐⭐
    - Pattern: Variable window + frequency
    - Learning: K replacements constraint
    - Time: 30 min target
    - **WHY IMPORTANT:** Complex condition handling
- [ ]  **LC 76** - Minimum Window Substring ⭐⭐⭐
    - Pattern: Variable window + frequency matching
    - Learning: Two HashMaps technique
    - Time: 40 min target
    - **WHY CRITICAL:** Google’s favorite hard problem

**🔄 Revision (90 min):**
- [ ] Re-solve LC 3 in 15 minutes (must be automatic)
- [ ] Re-solve LC 76 (hardest sliding window problem)
- [ ] Compare fixed vs variable window - when to use which?

**✅ Achievement Unlocked:**
Master the expand-shrink logic for any window problem

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 7: WEEK 1 REVISION + MINI CONTEST 🏆

**🎯 Goal:** Solidify Week 1 learning, identify weak areas

**📚 Morning Session (3 hours): Targeted Revision**

### Phase 1: Re-solve Without Hints

- [ ]  LC 1 - Two Sum (Target: 5 min)
- [ ]  LC 15 - 3Sum (Target: 15 min)
- [ ]  LC 3 - Longest Substring Without Repeating (Target: 15 min)
- [ ]  LC 560 - Subarray Sum Equals K (Target: 20 min)
- [ ]  LC 76 - Minimum Window Substring (Target: 25 min)

### Phase 2: Pattern Template Creation

- [ ]  Write Two Pointers template with examples
- [ ]  Write HashMap pattern with use cases
- [ ]  Write Prefix Sum template
- [ ]  Write Fixed Sliding Window template
- [ ]  Write Variable Sliding Window template

**📝 Afternoon Session (2 hours): Simulated Contest**

**Mini Contest Rules:**
- Set timer for 90 minutes
- Solve 3 problems in order (Easy → Medium → Medium)
- No looking at solutions until timer ends
- Treat like real interview

### Contest Problems:

- [ ]  **Problem 1 (Easy):** LC 121 - Best Time to Buy and Sell Stock
    - Expected time: 15 min
    - Pattern: Single pass with tracking min
- [ ]  **Problem 2 (Medium):** LC 11 - Container With Most Water
    - Expected time: 20 min
    - Pattern: Two pointers
- [ ]  **Problem 3 (Medium):** LC 438 - Find All Anagrams in a String
    - Expected time: 30 min
    - Pattern: Fixed sliding window + frequency

**Contest Debrief:**
- [ ] How many solved: ____/3
- [ ] Time taken: ____ minutes
- [ ] Which patterns felt natural?
- [ ] Which patterns need more practice?

**🧠 Evening Session (90 min): Deep Analysis**

### Self-Reflection Questions:

- [ ]  Which pattern do I understand best?
- [ ]  Which pattern takes me longest to code?
- [ ]  Can I explain each pattern to someone else?
- [ ]  Am I still looking at solutions too quickly?

### Week 1 Metrics:

- [ ]  Total problems solved: ____/~25
- [ ]  Problems solved without hints: ____
- [ ]  Average time per Easy problem: ____ min (Target: 15 min)
- [ ]  Average time per Medium problem: ____ min (Target: 30 min)
- [ ]  Patterns where I’m confident (list):
- [ ]  Patterns needing more work (list):

**✅ Week 1 Achievement Unlocked:**
- ✅ 6 core patterns mastered
- ✅ 25+ problems solved
- ✅ Foundation for all future learning

**📊 Week 1 Confidence Level:**
- Two Pointers: ⭐⭐⭐⭐⭐
- Hashing: ⭐⭐⭐⭐⭐
- Prefix Sum: ⭐⭐⭐⭐⭐
- Fixed Sliding Window: ⭐⭐⭐⭐⭐
- Variable Sliding Window: ⭐⭐⭐⭐⭐
- Overall Week 1: ⭐⭐⭐⭐⭐ (Target: 7/10)

---

## 🏁 WEEK 2: Sorting, Intervals & Advanced Pointers (Days 8-14)

---

### DAY 8: Sorting Algorithms 🔢

**🎯 Goal:** Understand sorting fundamentals - asked in Amazon/Microsoft

**📚 Learn (2 hours):**
- [ ] Watch: Merge Sort visualization and implementation
- [ ] Watch: Quick Sort explanation (partition logic)
- [ ] Study: Time/space complexity of all major sorts
- [ ] Understand: Stable vs unstable sorting

**🔑 Must-Know Sorting Algorithms:**

### Merge Sort

```
Merge Sort:
├─ Divide: Split array into halves recursively
├─ Conquer: Sort each half
└─ Merge: Combine sorted halves

Time: O(n log n) - ALL cases
Space: O(n)
Stable: YES
Use when: Need guaranteed O(n log n), sorting linked lists
```

### Quick Sort

```
Quick Sort:
├─ Partition: Choose pivot, rearrange (smaller left, larger right)
├─ Recurse: Sort left and right partitions
└─ Base case: Single element

Time: O(n log n) average, O(n²) worst
Space: O(log n) recursive stack
Stable: NO
Use when: In-place sorting needed, practical performance
```

### Counting Sort

```
Counting Sort:
├─ Count: Frequency of each element (limited range)
├─ Position: Calculate positions
└─ Place: Put elements in sorted order

Time: O(n + k) where k = range
Space: O(k)
Use when: Small range of integers (0 to k)
```

**💡 Sorting Pattern Recognition:**
- ✅ Problem says “sorted” → Often O(n) solution exists
- ✅ Need to sort → Consider which algorithm fits
- ✅ Dutch National Flag → 3-way partitioning

**📝 Problems (3 hours):**

### Implementation Practice

- [ ]  **Implement Merge Sort from scratch**
    - Code without looking at reference
    - Test on [4,2,7,1,9,3]
    - Time: 30 min target
- [ ]  **Implement Quick Sort from scratch**
    - Focus on partition logic
    - Handle duplicates correctly
    - Time: 30 min target

### LeetCode Problems

- [ ]  **LC 912** - Sort an Array
    - Pattern: Implement quick sort
    - Learning: Randomized pivot
    - Time: 20 min target
- [ ]  **LC 75** - Sort Colors (Dutch National Flag) ⭐⭐
    - Pattern: 3-way partitioning in one pass
    - Learning: O(n) time, O(1) space sorting
    - Time: 25 min target
    - **WHY IMPORTANT:** Classic partition problem
- [ ]  **LC 148** - Sort List ⭐⭐
    - Pattern: Merge sort for linked list
    - Learning: Finding middle, merging lists
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Re-implement merge sort without reference
- [ ] Re-solve LC 75 (understand 3-pointer approach)
- [ ] Create comparison table: Which sort when?

**✅ Achievement Unlocked:**
Can implement merge sort in 15 minutes from memory

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 9: Intervals Pattern 📅

**🎯 Goal:** Master interval problems - Google/Microsoft’s scheduling favorites

**📚 Learn (90 min):**
- [ ] Watch: Interval merging visualization
- [ ] Understand: Why sorting by start time is key
- [ ] Learn: Greedy approach for non-overlapping intervals

**🔑 Pattern Template:**

```
Intervals Pattern:
├─ Step 1: ALWAYS sort by start time (or end time for some problems)
├─ Step 2: Iterate and check overlap
├─ Overlap check: intervals[i][1] >= intervals[i+1][0]
└─ Merge: [min(start1, start2), max(end1, end2)]

Common operations:
- Merge: Combine overlapping intervals
- Insert: Add interval and merge
- Count: How many overlap/non-overlap
- Schedule: Meeting rooms, min rooms needed

Time: O(n log n) for sorting + O(n) for iteration
```

**💡 When to Use:**
- ✅ Meeting rooms / scheduling problems
- ✅ Calendar booking systems
- ✅ Range merging/overlapping
- ✅ Activity selection problems

**📝 Problems (3 hours):**

### Foundation Problems

- [ ]  **LC 56** - Merge Intervals ⭐⭐⭐
    - Pattern: Sort + merge overlapping
    - Learning: Basic interval merging
    - Time: 20 min target
    - **WHY CRITICAL:** Foundation for all interval problems
- [ ]  **LC 57** - Insert Interval ⭐⭐
    - Pattern: Insert + merge in sorted list
    - Learning: Three phases (before, overlap, after)
    - Time: 25 min target

### Counting & Scheduling

- [ ]  **LC 252** - Meeting Rooms (Easy)
    - Pattern: Check if any overlap exists
    - Learning: Simple overlap detection
    - Time: 15 min target
- [ ]  **LC 253** - Meeting Rooms II ⭐⭐
    - Pattern: Count max overlapping intervals
    - Learning: Min heap or sorting endpoints
    - Time: 30 min target
    - **WHY IMPORTANT:** Tests optimal resource allocation
- [ ]  **LC 435** - Non-overlapping Intervals ⭐
    - Pattern: Greedy - sort by end time
    - Learning: Activity selection
    - Time: 25 min target

**🔄 Revision (90 min):**
- [ ] Re-solve LC 56 (must be automatic)
- [ ] Re-solve LC 253 using both approaches (heap vs sorting)
- [ ] Practice: Draw timeline for interval examples

**✅ Achievement Unlocked:**
Can handle any calendar/scheduling problem

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 10: Cyclic Sort Pattern 🔄

**🎯 Goal:** Master in-place sorting when array values = 1 to n

**📚 Learn (90 min):**
- [ ] Watch: Cyclic sort explanation
- [ ] Understand: Using index as hash (value-1 = index)
- [ ] Learn: Why this gives O(n) time, O(1) space

**🔑 Pattern Template:**

```
Cyclic Sort Pattern:
├─ Use when: Array contains integers from 1 to n (or 0 to n-1)
├─ Key insight: Place number X at index X-1
├─ Algorithm:
    for i in range(n):
        while arr[i] != i+1 and arr[i] within range:
            swap arr[i] with arr[arr[i]-1]
└─ After: Each number at correct position (or missing/duplicate found)

Time: O(n) - each element placed once
Space: O(1)
```

**💡 When to Use:**
- ✅ “Find missing number in array 1 to n”
- ✅ “Find duplicate in array 1 to n”
- ✅ “First missing positive integer”
- ✅ Array contains range [1, n] or [0, n-1]

**📝 Problems (3 hours):**

### Easy (Pattern Recognition)

- [ ]  **LC 268** - Missing Number
    - Pattern: Cyclic sort or XOR trick
    - Learning: Multiple approaches to same problem
    - Time: 15 min target
- [ ]  **LC 448** - Find All Numbers Disappeared ⭐
    - Pattern: Cyclic sort identifies missing
    - Learning: In-place marking technique
    - Time: 20 min target

### Medium (Core Applications)

- [ ]  **LC 442** - Find All Duplicates in an Array ⭐
    - Pattern: Cyclic sort with duplicate detection
    - Learning: Marking seen elements
    - Time: 25 min target
- [ ]  **LC 287** - Find the Duplicate Number ⭐⭐⭐
    - Pattern: Cyclic sort OR Floyd’s cycle detection
    - Learning: Two solutions to same problem
    - Time: 30 min target
    - **WHY IMPORTANT:** Combines multiple patterns

### Hard (Master Level)

- [ ]  **LC 41** - First Missing Positive ⭐⭐⭐
    - Pattern: Cyclic sort with ignore negatives
    - Learning: Handling invalid elements
    - Time: 35 min target
    - **WHY CRITICAL:** Hard problem with elegant solution

**🔄 Revision (90 min):**
- [ ] Implement cyclic sort on [3,1,5,4,2]
- [ ] Re-solve LC 41 (hard but important)
- [ ] Compare: When to use cyclic sort vs hashing?

**✅ Achievement Unlocked:**
Never use extra space for “1 to n” range problems

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 11: Fast & Slow Pointers (Floyd’s Algorithm) 🐢🐇

**🎯 Goal:** Master cycle detection - critical for linked list problems

**📚 Learn (90 min):**
- [ ] Watch: Floyd’s Cycle Detection explanation
- [ ] Understand: Why slow/fast eventually meet in cycle
- [ ] Study: Math proof of cycle detection
- [ ] Learn: Finding cycle start formula

**🔑 Pattern Template:**

```
Fast & Slow Pointers (Floyd's):
├─ Initialize: slow = head, fast = head
├─ Move: slow moves 1 step, fast moves 2 steps
├─ Cycle detection: If fast meets slow, cycle exists
├─ Cycle start: Reset slow to head, move both 1 step until they meet
└─ Applications: Cycle detection, finding middle, palindrome check

Time: O(n)
Space: O(1)
```

**💡 When to Use:**
- ✅ Detect cycle in linked list
- ✅ Find middle of linked list
- ✅ Check if linked list is palindrome
- ✅ Happy number problem
- ✅ Start of cycle in linked list

**📝 Problems (3 hours):**

### Easy (Foundation)

- [ ]  **LC 141** - Linked List Cycle
    - Pattern: Basic Floyd’s algorithm
    - Learning: Cycle detection
    - Time: 15 min target
- [ ]  **LC 876** - Middle of the Linked List
    - Pattern: Fast-slow pointers
    - Learning: Finding middle in one pass
    - Time: 10 min target
- [ ]  **LC 202** - Happy Number
    - Pattern: Cycle detection in number sequence
    - Learning: Non-linked-list application
    - Time: 20 min target

### Medium (Mastery)

- [ ]  **LC 142** - Linked List Cycle II ⭐⭐⭐
    - Pattern: Floyd’s algorithm + math
    - Learning: Finding cycle start node
    - Time: 25 min target
    - **WHY CRITICAL:** Tests understanding of algorithm proof
- [ ]  **LC 287** - Find the Duplicate Number (Alternative) ⭐⭐
    - Pattern: Array as linked list + Floyd’s
    - Learning: Creative pattern application
    - Time: 30 min target
    - **WHY IMPORTANT:** Shows pattern versatility

**🔄 Revision (90 min):**
- [ ] Draw diagram of cycle detection step-by-step
- [ ] Re-solve LC 142 and explain the math
- [ ] Practice: Implement finding middle without fast-slow

**✅ Achievement Unlocked:**
Can detect cycles in any structure (list, graph, sequence)

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 12: Strings - Core Patterns 🔤

**🎯 Goal:** Master string manipulation - foundation for many problems

**📚 Learn (90 min):**
- [ ] Review: String operations in your language (immutable/mutable)
- [ ] Learn: Two pointers on strings
- [ ] Study: Palindrome patterns
- [ ] Understand: Anagram detection techniques

**🔑 Common String Patterns:**

```
String Patterns:
1. Palindrome Check: Two pointers from ends
2. Anagram: Sort or frequency map
3. Substring: Sliding window
4. Pattern Matching: KMP (advanced)
5. String Building: StringBuilder/array for efficiency
```

**💡 String Tips:**
- ✅ Strings are immutable in many languages (use array/StringBuilder)
- ✅ Two pointers work great on strings
- ✅ Anagrams → same frequency map
- ✅ Palindrome → compare from both ends

**📝 Problems (3 hours):**

### Easy (Warmup)

- [ ]  **LC 125** - Valid Palindrome
    - Pattern: Two pointers + character filtering
    - Learning: Handling non-alphanumeric
    - Time: 15 min target
- [ ]  **LC 344** - Reverse String
    - Pattern: Two pointers swap
    - Learning: In-place string modification
    - Time: 10 min target
- [ ]  **LC 242** - Valid Anagram
    - Pattern: Frequency map comparison
    - Learning: Character counting
    - Time: 15 min target
- [ ]  **LC 14** - Longest Common Prefix
    - Pattern: Vertical scanning or divide-conquer
    - Learning: String comparison techniques
    - Time: 20 min target

### Medium (Core Practice)

- [ ]  **LC 5** - Longest Palindromic Substring ⭐⭐⭐
    - Pattern: Expand around center
    - Learning: O(n²) palindrome detection
    - Time: 30 min target
    - **WHY IMPORTANT:** Classic DP/two-pointer hybrid
- [ ]  **LC 647** - Palindromic Substrings ⭐
    - Pattern: Similar to LC 5, count instead of track
    - Learning: Counting technique
    - Time: 25 min target

**🔄 Revision (90 min):**
- [ ] Re-solve LC 5 (important for DP later)
- [ ] Practice: Reverse words in a string in-place
- [ ] Write string manipulation cheat sheet

**✅ Achievement Unlocked:**
String problems feel natural and intuitive

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/6

---

### DAY 13: Mathematics & Bit Manipulation 🔢

**🎯 Goal:** Learn optimization tricks using math and bits

**📚 Learn (90 min):**
- [ ] Watch: Bit manipulation basics (AND, OR, XOR, shifts)
- [ ] Study: XOR properties and applications
- [ ] Learn: GCD/LCM algorithms
- [ ] Understand: Prime number optimizations

**🔑 Key Concepts:**

### Bit Manipulation Tricks

```
XOR Properties:
├─ a ^ a = 0 (cancel out)
├─ a ^ 0 = a (identity)
├─ XOR is commutative and associative
└─ Use case: Find single number among duplicates

Common Bit Operations:
├─ Check if bit set: (n & (1 << i)) != 0
├─ Set bit: n | (1 << i)
├─ Clear bit: n & ~(1 << i)
├─ Toggle bit: n ^ (1 << i)
└─ Count bits: Brian Kernighan's algorithm
```

### Math Algorithms

```
GCD (Euclidean):
gcd(a, b) = gcd(b, a % b) until b = 0

Prime Check:
Check divisibility up to √n only

Fast Power:
Use binary exponentiation: O(log n)
```

**💡 When to Use:**
- ✅ Finding single/duplicate among pairs → XOR
- ✅ Checking parity (odd/even) → & 1
- ✅ Multiplying/dividing by 2 → shift operators
- ✅ Counting set bits → n & (n-1) trick

**📝 Problems (3 hours):**

### Bit Manipulation

- [ ]  **LC 136** - Single Number ⭐⭐
    - Pattern: XOR cancellation
    - Learning: XOR properties
    - Time: 10 min target
    - **WHY IMPORTANT:** Classic XOR application
- [ ]  **LC 191** - Number of 1 Bits
    - Pattern: Brian Kernighan’s algorithm
    - Learning: Bit counting optimization
    - Time: 15 min target
- [ ]  **LC 338** - Counting Bits ⭐
    - Pattern: DP + bit manipulation
    - Learning: Pattern in bit counts
    - Time: 20 min target
- [ ]  **LC 371** - Sum of Two Integers
    - Pattern: Addition using XOR and AND
    - Learning: Binary arithmetic
    - Time: 25 min target

### Mathematics

- [ ]  **LC 50** - Pow(x, n) ⭐
    - Pattern: Binary exponentiation
    - Learning: O(log n) power calculation
    - Time: 25 min target
- [ ]  **LC 204** - Count Primes
    - Pattern: Sieve of Eratosthenes
    - Learning: Prime generation
    - Time: 20 min target

**🔄 Revision (90 min):**
- [ ] Practice XOR on paper for [4,1,2,1,2]
- [ ] Implement GCD and LCM functions
- [ ] Create bit manipulation cheat sheet

**✅ Achievement Unlocked:**
Know when to use bit tricks for optimization

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/6

---

### DAY 14: WEEK 2 REVISION + ASSESSMENT 🏆

**🎯 Goal:** Consolidate Week 2 learning, prepare for data structures

**📚 Morning Session (3 hours): Comprehensive Revision**

### Phase 1: Re-solve Key Problems (No hints!)

- [ ]  LC 75 - Sort Colors (Target: 10 min)
- [ ]  LC 56 - Merge Intervals (Target: 15 min)
- [ ]  LC 41 - First Missing Positive (Target: 20 min)
- [ ]  LC 142 - Linked List Cycle II (Target: 15 min)
- [ ]  LC 5 - Longest Palindromic Substring (Target: 20 min)
- [ ]  LC 136 - Single Number (Target: 5 min)

### Phase 2: Pattern Consolidation

- [ ]  Create sorting decision tree (when to use which sort?)
- [ ]  Draw interval merging process step-by-step
- [ ]  Implement cyclic sort template from memory
- [ ]  Explain Floyd’s algorithm math proof
- [ ]  Write XOR properties with examples

**📝 Afternoon Session (2 hours): Timed Assessment**

**Full Mock Interview (90 minutes):**

Set timer, no solutions allowed, simulate real interview conditions.

- [ ]  **Problem 1 (Easy):** LC 350 - Intersection of Two Arrays II
    - Expected: 15 min
    - Pattern: Hashing or two pointers
- [ ]  **Problem 2 (Medium):** LC 986 - Interval List Intersections
    - Expected: 25 min
    - Pattern: Two pointers on intervals
- [ ]  **Problem 3 (Medium):** LC 394 - Decode String
    - Expected: 30 min
    - Pattern: Stack (preview for next week)

**Assessment Debrief:**
- [ ] Problems solved: ____/3
- [ ] Time management: Good / Needs work
- [ ] Approach explanation: Clear / Unclear
- [ ] Code quality: Clean / Messy

**🧠 Evening Session (90 min): Week 2 Analysis**

### Pattern Mastery Check:

Rate each pattern 1-10:
- Sorting (Merge/Quick): ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Intervals: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Cyclic Sort: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Fast-Slow Pointers: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Strings: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Bit Manipulation: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

### Week 2 Metrics:

- [ ]  Total problems solved (cumulative): ____/~50
- [ ]  Problems solved without hints this week: ____
- [ ]  Average time per Medium: ____ min (Target: 25-30 min)
- [ ]  Patterns I’m confident in: ________________
- [ ]  Patterns needing more work: ________________

### Preparation for Week 3:

- [ ]  Read about Linked List basics
- [ ]  Watch one video on Stack applications
- [ ]  Review recursion fundamentals

**✅ Week 2 Achievement Unlocked:**
- ✅ 12 total patterns mastered (Week 1 + Week 2)
- ✅ 50+ problems solved
- ✅ Ready for data structures (Linked Lists, Stacks, Queues)

**📊 Overall Confidence After 2 Weeks:**
- Technical Understanding: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (Target: 7/10)
- Problem-Solving Speed: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (Target: 6/10)
- Interview Readiness: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (Target: 5/10 - still early)

**🎯 Week 2 Complete! Moving to Phase 2: Data Structures**

---

# 📗 PHASE 2: DATA STRUCTURES MASTERY (Days 15-30)

## 🔗 WEEK 3: Linked Lists & Stacks (Days 15-21)

---

### DAY 15: Linked List - Basics & Reversal 🔗

**🎯 Goal:** Master pointer manipulation - foundation for all LL problems

**📚 Learn (90 min):**
- [ ] Watch: Linked list visualization
- [ ] Study: Singly vs doubly linked lists
- [ ] Understand: Pointer manipulation
- [ ] Learn: Dummy node technique

**🔑 Pattern Template:**

```
Linked List Key Concepts:
├─ Dummy Node: Simplifies edge cases (head manipulation)
├─ Two Pointers: Fast-slow, prev-curr
├─ Reversal: Iterative (3 pointers) or Recursive
└─ Common operations: Insert, delete, reverse, merge

Reversal Template (Iterative):
prev = None
curr = head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
return prev

Time: O(n) | Space: O(1)
```

**💡 Common LL Patterns:**
- ✅ Reversal: Use 3 pointers (prev, curr, next)
- ✅ Dummy node: When head might change
- ✅ Fast-slow: Finding middle or cycle
- ✅ Runner technique: Reaching nth node from end

**📝 Problems (3 hours):**

### Foundation

- [ ]  **LC 206** - Reverse Linked List ⭐⭐⭐
    - Pattern: Iterative and recursive reversal
    - Learning: Pointer manipulation
    - Time: 20 min target (both approaches)
    - **WHY CRITICAL:** Most fundamental LL problem
- [ ]  **LC 234** - Palindrome Linked List ⭐
    - Pattern: Find middle + reverse + compare
    - Learning: Combining multiple techniques
    - Time: 25 min target

### Merging & Manipulation

- [ ]  **LC 21** - Merge Two Sorted Lists ⭐⭐
    - Pattern: Two pointers + dummy node
    - Learning: Sorted merge technique
    - Time: 20 min target
- [ ]  **LC 19** - Remove Nth Node From End ⭐⭐
    - Pattern: Two pointers with gap
    - Learning: One-pass solution
    - Time: 20 min target
- [ ]  **LC 2** - Add Two Numbers ⭐
    - Pattern: Carry handling in LL
    - Learning: Digit-by-digit addition
    - Time: 25 min target

**🔄 Revision (90 min):**
- [ ] Implement reversal both iteratively and recursively
- [ ] Draw pointer movements on paper
- [ ] Re-solve LC 206 in 10 minutes

**✅ Achievement Unlocked:**
Can manipulate pointers confidently in any LL problem

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 16: Linked List - Advanced Patterns 🔗

**🎯 Goal:** Handle complex LL manipulations

**📚 Learn (90 min):**
- [ ] Study: In-place LL operations
- [ ] Learn: Partition and rearrangement
- [ ] Understand: Floyd’s cycle (review from Day 11)

**📝 Problems (3 hours):**

### Rearrangement

- [ ]  **LC 143** - Reorder List ⭐⭐
    - Pattern: Find middle + reverse + merge
    - Learning: Multi-step LL transformation
    - Time: 30 min target
    - **WHY IMPORTANT:** Combines 3 patterns
- [ ]  **LC 328** - Odd Even Linked List ⭐
    - Pattern: Two pointers for grouping
    - Learning: In-place rearrangement
    - Time: 25 min target

### Advanced Manipulation

- [ ]  **LC 92** - Reverse Linked List II ⭐⭐
    - Pattern: Partial reversal
    - Learning: Careful pointer tracking
    - Time: 30 min target
- [ ]  **LC 25** - Reverse Nodes in k-Group ⭐⭐⭐
    - Pattern: Group reversal
    - Learning: Complex pointer management
    - Time: 40 min target
    - **WHY CRITICAL:** Hard but tests mastery

**🔄 Revision (90 min):**
- [ ] Re-solve LC 143 (important pattern combo)
- [ ] Practice: Reverse every k nodes
- [ ] Draw diagrams for LC 25

**✅ Achievement Unlocked:**
Can handle any complex LL manipulation

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 17: Stack - Basics & Applications 📚

**🎯 Goal:** Master LIFO operations and stack patterns

**📚 Learn (90 min):**
- [ ] Watch: Stack implementation and applications
- [ ] Study: When to use stack (LIFO problems)
- [ ] Learn: Stack with arrays vs linked lists
- [ ] Understand: Monotonic stack (preview)

**🔑 Pattern Template:**

```
Stack Patterns:
├─ Parentheses/Brackets: Match pairs
├─ Next Greater/Smaller: Monotonic stack
├─ Evaluation: Postfix, infix expressions
├─ DFS: Iterative using stack
└─ Function calls: Call stack simulation

Common operations:
- push(): Add to top - O(1)
- pop(): Remove from top - O(1)
- peek(): View top - O(1)
```

**💡 When to Use Stack:**
- ✅ Matching pairs (parentheses, brackets)
- ✅ Backtracking (DFS, undo operations)
- ✅ Next greater/smaller element
- ✅ Expression evaluation
- ✅ Function call simulation

**📝 Problems (3 hours):**

### Foundation

- [ ]  **LC 20** - Valid Parentheses ⭐⭐⭐
    - Pattern: Stack for matching pairs
    - Learning: HashMap for bracket pairs
    - Time: 15 min target
    - **WHY CRITICAL:** Most asked stack problem
- [ ]  **LC 155** - Min Stack ⭐⭐
    - Pattern: Auxiliary stack for min tracking
    - Learning: Design problem
    - Time: 25 min target

### Expression Evaluation

- [ ]  **LC 150** - Evaluate Reverse Polish Notation ⭐
    - Pattern: Stack for postfix evaluation
    - Learning: Operator application
    - Time: 20 min target
- [ ]  **LC 227** - Basic Calculator II ⭐⭐
    - Pattern: Stack + operator precedence
    - Learning: Expression parsing
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Implement stack using arrays and LL
- [ ] Re-solve LC 20 in 10 minutes
- [ ] Practice: Implement min stack without extra space

**✅ Achievement Unlocked:**
Understand when and how to apply stack

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 18: Stack - Monotonic Stack Pattern 📈

**🎯 Goal:** Master monotonic stack - powerful optimization pattern

**📚 Learn (90 min):**
- [ ] Watch: Monotonic stack explanation
- [ ] Study: Increasing vs decreasing stack
- [ ] Understand: Next greater/smaller element
- [ ] Learn: When monotonic stack is optimal

**🔑 Pattern Template:**

```
Monotonic Stack:
├─ Monotonic Increasing: Elements in increasing order
├─ Monotonic Decreasing: Elements in decreasing order
├─ Use for: Next greater/smaller element in O(n)
└─ Key: Pop elements that violate monotonic property

Next Greater Element (Decreasing Stack):
stack = []
result = [-1] * n
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

Time: O(n) - each element pushed/popped once
```

**💡 When to Use:**
- ✅ “Next greater element”
- ✅ “Next smaller element”
- ✅ “Previous greater/smaller”
- ✅ Histogram/bar chart problems
- ✅ Trapping rain water type problems

**📝 Problems (3 hours):**

### Foundation

- [ ]  **LC 496** - Next Greater Element I
    - Pattern: Basic monotonic stack
    - Learning: Stack + hashmap
    - Time: 20 min target
- [ ]  **LC 503** - Next Greater Element II (Circular)
    - Pattern: Circular array handling
    - Learning: Modulo trick
    - Time: 25 min target

### Advanced Applications

- [ ]  **LC 739** - Daily Temperatures ⭐⭐⭐
    - Pattern: Monotonic decreasing stack
    - Learning: Storing indices
    - Time: 25 min target
    - **WHY IMPORTANT:** Classic monotonic stack
- [ ]  **LC 84** - Largest Rectangle in Histogram ⭐⭐⭐
    - Pattern: Monotonic increasing stack
    - Learning: Area calculation with stack
    - Time: 40 min target
    - **WHY CRITICAL:** Hard but important pattern
- [ ]  **LC 42** - Trapping Rain Water ⭐⭐⭐
    - Pattern: Monotonic stack (alternative to DP)
    - Learning: Water trapping logic
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Draw stack states for LC 739
- [ ] Re-solve LC 84 (important for DP later)
- [ ] Understand both increasing and decreasing stacks

**✅ Achievement Unlocked:**
Can use monotonic stack for O(n) optimization

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 19: Queue & Deque 📋

**🎯 Goal:** Master FIFO operations and deque applications

**📚 Learn (90 min):**
- [ ] Watch: Queue and deque explanation
- [ ] Study: Queue implementation (array vs LL)
- [ ] Learn: Deque (double-ended queue)
- [ ] Understand: When to use queue vs deque

**🔑 Pattern Template:**

```
Queue (FIFO):
├─ enqueue(): Add to rear - O(1)
├─ dequeue(): Remove from front - O(1)
├─ peek(): View front - O(1)
└─ Use for: BFS, level order, scheduling

Deque (Double-ended):
├─ Can add/remove from both ends
├─ addFirst(), addLast(), removeFirst(), removeLast()
├─ Use for: Sliding window maximum, palindrome
└─ More flexible than queue
```

**💡 When to Use:**
- ✅ BFS traversal → Queue
- ✅ Sliding window problems → Deque
- ✅ Level order traversal → Queue
- ✅ Task scheduling → Queue

**📝 Problems (3 hours):**

### Queue Basics

- [ ]  **LC 622** - Design Circular Queue ⭐
    - Pattern: Array-based circular queue
    - Learning: Modulo arithmetic for circular
    - Time: 30 min target
- [ ]  **LC 346** - Moving Average from Data Stream
    - Pattern: Queue for sliding window
    - Learning: Average calculation
    - Time: 20 min target

### Deque Applications

- [ ]  **LC 239** - Sliding Window Maximum ⭐⭐⭐
    - Pattern: Monotonic deque
    - Learning: Maintaining max in window
    - Time: 40 min target
    - **WHY CRITICAL:** Most important deque problem
- [ ]  **LC 862** - Shortest Subarray with Sum At Least K ⭐⭐⭐
    - Pattern: Deque + prefix sum
    - Learning: Complex optimization
    - Time: 45 min target
    - **WHY IMPORTANT:** Combines multiple patterns

**🔄 Revision (90 min):**
- [ ] Implement circular queue from scratch
- [ ] Re-solve LC 239 (critical pattern)
- [ ] Compare: When to use queue vs deque vs stack?

**✅ Achievement Unlocked:**
Master queue and deque for optimization problems

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 20: Design Data Structures 🏗️

**🎯 Goal:** Learn to design custom data structures - asked in top companies

**📚 Learn (90 min):**
- [ ] Watch: LRU Cache explanation
- [ ] Study: HashMap + Doubly Linked List combination
- [ ] Understand: O(1) operations design
- [ ] Learn: Common design patterns

**🔑 Design Patterns:**

```
LRU Cache Design:
├─ HashMap: For O(1) get
├─ Doubly LL: For O(1) LRU updates
├─ Operations:
    - get(key): Move to front if exists
    - put(key, value): Add to front, evict LRU if full
└─ Both operations: O(1) time

Common design questions:
- LRU Cache (most asked)
- LFU Cache (harder)
- Min Stack
- Max Stack
- Time-based Key-Value Store
```

**💡 Design Tips:**
- ✅ Start with examples and edge cases
- ✅ Think about time complexity requirements
- ✅ Combine data structures for optimization
- ✅ Explain trade-offs clearly

**📝 Problems (3 hours):**

### Must-Know Designs

- [ ]  **LC 146** - LRU Cache ⭐⭐⭐
    - Pattern: HashMap + Doubly LL
    - Learning: Most asked design problem
    - Time: 45 min target
    - **WHY CRITICAL:** Asked in 50% of FAANG interviews
- [ ]  **LC 460** - LFU Cache ⭐⭐⭐
    - Pattern: Multiple HashMaps + Doubly LL
    - Learning: Complex frequency tracking
    - Time: 60 min target
    - **WHY IMPORTANT:** Harder variant of LRU

### Other Important Designs

- [ ]  **LC 155** - Min Stack (Review from Day 17)
    - Pattern: Auxiliary stack
    - Learning: O(1) min retrieval
    - Time: 15 min target
- [ ]  **LC 380** - Insert Delete GetRandom O(1) ⭐⭐
    - Pattern: HashMap + ArrayList
    - Learning: Random access with deletions
    - Time: 30 min target

**🔄 Revision (90 min):**
- [ ] Draw diagram of LRU Cache operations
- [ ] Implement LRU from memory
- [ ] Practice explaining design decisions out loud

**✅ Achievement Unlocked:**
Can design efficient data structures on the spot

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 21: WEEK 3 REVISION + MINI CONTEST 🏆

**🎯 Goal:** Solidify linked list, stack, queue mastery

**📚 Morning Session (3 hours): Targeted Revision**

### Phase 1: Re-solve Without Hints

- [ ]  LC 206 - Reverse Linked List (Target: 10 min)
- [ ]  LC 143 - Reorder List (Target: 20 min)
- [ ]  LC 20 - Valid Parentheses (Target: 10 min)
- [ ]  LC 84 - Largest Rectangle in Histogram (Target: 25 min)
- [ ]  LC 239 - Sliding Window Maximum (Target: 25 min)
- [ ]  LC 146 - LRU Cache (Target: 30 min)

### Phase 2: Pattern Templates

- [ ]  Write LL reversal template (iterative + recursive)
- [ ]  Write stack template with all operations
- [ ]  Write monotonic stack template
- [ ]  Write deque template for sliding window
- [ ]  Draw LRU Cache structure

**📝 Afternoon Session (2 hours): Simulated Contest**

**Mock Interview (90 minutes):**

- [ ]  **Problem 1 (Easy):** LC 232 - Implement Queue using Stacks
    - Expected: 20 min
    - Pattern: Stack operations
- [ ]  **Problem 2 (Medium):** LC 138 - Copy List with Random Pointer
    - Expected: 30 min
    - Pattern: Linked list + HashMap
- [ ]  **Problem 3 (Medium):** LC 402 - Remove K Digits
    - Expected: 30 min
    - Pattern: Monotonic stack

**Contest Debrief:**
- [ ] Problems solved: ____/3
- [ ] Which data structure felt most natural?
- [ ] Which needs more practice?

**🧠 Evening Session (90 min): Week 3 Analysis**

### Pattern Mastery:

- Linked List: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Stack: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Monotonic Stack: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Queue/Deque: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Design: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

### Week 3 Metrics:

- [ ]  Total problems (cumulative): ____/~75
- [ ]  Data structures confidence: __/10
- [ ]  Average Medium problem time: ____ min

**✅ Week 3 Achievement Unlocked:**
- ✅ Mastered all linear data structures
- ✅ Can design efficient data structures
- ✅ Ready for trees and graphs

**📊 Overall Progress After 3 Weeks:**
- Patterns Mastered: 17 total
- Problems Solved: 75+
- Confidence: 7-8/10
- Ready for: Trees & Graphs

---

## 🌳 WEEK 4: Trees (Days 22-28)

---

### DAY 22: Binary Trees - Traversal & Basics 🌲

**🎯 Goal:** Master tree traversals - foundation for all tree problems

**📚 Learn (2 hours):**
- [ ] Watch: Binary tree traversal animations
- [ ] Study: Pre-order, In-order, Post-order, Level-order
- [ ] Understand: Recursive vs iterative traversals
- [ ] Learn: When to use which traversal

**🔑 Pattern Template:**

```
Binary Tree Traversals:

Pre-order (Root → Left → Right):
Use for: Creating copy, prefix expressions
def preorder(root):
    if not root: return
    process(root)
    preorder(root.left)
    preorder(root.right)

In-order (Left → Root → Right):
Use for: BST sorted order, infix expressions
def inorder(root):
    if not root: return
    inorder(root.left)
    process(root)
    inorder(root.right)

Post-order (Left → Right → Root):
Use for: Deleting tree, postfix expressions
def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    process(root)

Level-order (BFS):
Use for: Level-by-level processing, shortest path in tree
Use queue for iterative approach

Time: O(n) for all | Space: O(h) recursive stack
```

**💡 Tree Basics:**
- ✅ Height of tree: Longest path from root to leaf
- ✅ Depth of node: Path length from root
- ✅ Balanced tree: |left_height - right_height| ≤ 1
- ✅ Complete tree: All levels filled except possibly last

**📝 Problems (3 hours):**

### Traversal Basics

- [ ]  **LC 144** - Binary Tree Preorder Traversal
    - Pattern: Recursive and iterative
    - Learning: Stack for iterative
    - Time: 20 min target
- [ ]  **LC 94** - Binary Tree Inorder Traversal ⭐
    - Pattern: Recursive and iterative
    - Learning: BST sorted order
    - Time: 20 min target
- [ ]  **LC 145** - Binary Tree Postorder Traversal
    - Pattern: Recursive and iterative
    - Learning: Two-stack approach
    - Time: 25 min target

### Level Order (BFS)

- [ ]  **LC 102** - Binary Tree Level Order Traversal ⭐⭐⭐
    - Pattern: Queue for BFS
    - Learning: Level-by-level processing
    - Time: 25 min target
    - **WHY CRITICAL:** Most common tree interview question
- [ ]  **LC 107** - Binary Tree Level Order Traversal II
    - Pattern: Level order + reverse
    - Learning: Bottom-up processing
    - Time: 20 min target

**🔄 Revision (90 min):**
- [ ] Implement all 4 traversals from memory
- [ ] Draw tree and manually trace each traversal
- [ ] Re-solve LC 102 (extremely important)

**✅ Achievement Unlocked:**
Can implement any tree traversal instantly

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 23: Binary Trees - Depth & Height Problems 📏

**🎯 Goal:** Master depth/height based tree problems

**📚 Learn (90 min):**
- [ ] Study: Height vs depth difference
- [ ] Understand: Diameter calculation
- [ ] Learn: Path sum problems
- [ ] Review: Recursion for trees

**🔑 Key Concepts:**

```
Height of Tree:
def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

Diameter Pattern:
At each node, diameter = left_height + right_height
Track global maximum

Path Sum Pattern:
Subtract value at each node
Check if leaf and sum == 0
```

**📝 Problems (3 hours):**

### Depth/Height

- [ ]  **LC 104** - Maximum Depth of Binary Tree ⭐⭐
    - Pattern: Simple recursion
    - Learning: Tree height
    - Time: 10 min target
- [ ]  **LC 111** - Minimum Depth of Binary Tree
    - Pattern: BFS or recursion
    - Learning: Careful with one child
    - Time: 15 min target
- [ ]  **LC 110** - Balanced Binary Tree ⭐
    - Pattern: Height + balance check
    - Learning: Bottom-up recursion
    - Time: 20 min target

### Diameter & Paths

- [ ]  **LC 543** - Diameter of Binary Tree ⭐⭐⭐
    - Pattern: Height at each node
    - Learning: Global max tracking
    - Time: 25 min target
    - **WHY IMPORTANT:** Tests recursion understanding
- [ ]  **LC 112** - Path Sum
    - Pattern: Recursion with subtraction
    - Learning: Leaf node checking
    - Time: 15 min target
- [ ]  **LC 113** - Path Sum II ⭐
    - Pattern: Path sum + backtracking
    - Learning: Collecting all paths
    - Time: 25 min target

**🔄 Revision (90 min):**
- [ ] Draw tree and calculate diameter manually
- [ ] Re-solve LC 543 (important for DFS)
- [ ] Practice explaining recursion out loud

**✅ Achievement Unlocked:**
Comfortable with tree recursion patterns

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/6

---

### DAY 24: Binary Trees - Construction & Modification 🔨

**🎯 Goal:** Build and modify trees programmatically

**📚 Learn (90 min):**
- [ ] Study: Tree construction from traversals
- [ ] Understand: Inorder + Preorder → Tree
- [ ] Learn: Tree modification patterns
- [ ] Review: Serialization/Deserialization

**📝 Problems (3 hours):**

### Tree Construction

- [ ]  **LC 105** - Construct Binary Tree from Preorder and Inorder ⭐⭐⭐
    - Pattern: Recursion with index tracking
    - Learning: Pre-order gives root, in-order gives left/right
    - Time: 35 min target
    - **WHY CRITICAL:** Tests tree understanding deeply
- [ ]  **LC 106** - Construct Binary Tree from Inorder and Postorder ⭐⭐
    - Pattern: Similar to LC 105
    - Learning: Post-order root at end
    - Time: 30 min target

### Tree Modification

- [ ]  **LC 226** - Invert Binary Tree ⭐⭐
    - Pattern: Swap children recursively
    - Learning: Simple recursion
    - Time: 10 min target
    - **WHY FAMOUS:** “Homebrew creator failed this at Google”
- [ ]  **LC 114** - Flatten Binary Tree to Linked List ⭐⭐
    - Pattern: Recursion or Morris traversal
    - Learning: In-place modification
    - Time: 25 min target

### Serialization

- [ ]  **LC 297** - Serialize and Deserialize Binary Tree ⭐⭐⭐
    - Pattern: Pre-order + null markers
    - Learning: String encoding
    - Time: 40 min target
    - **WHY IMPORTANT:** Design + trees combined

**🔄 Revision (90 min):**
- [ ] Draw how LC 105 builds tree step-by-step
- [ ] Re-solve LC 226 (famous problem)
- [ ] Practice serialization on custom trees

**✅ Achievement Unlocked:**
Can construct and modify any tree

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 25: Binary Search Trees (BST) 🔍

**🎯 Goal:** Master BST properties and operations

**📚 Learn (90 min):**
- [ ] Watch: BST property explanation
- [ ] Study: In-order gives sorted array
- [ ] Understand: Insert, delete, search in BST
- [ ] Learn: BST validation technique

**🔑 Pattern Template:**

```
BST Property:
├─ Left subtree: All values < root
├─ Right subtree: All values > root
├─ In-order traversal: Sorted order
└─ Operations: O(h) where h = height

Validation:
def isValid(root, min_val, max_val):
    if not root: return True
    if not (min_val < root.val < max_val):
        return False
    return isValid(root.left, min_val, root.val) and \
           isValid(root.right, root.val, max_val)

Time: O(h) for search, insert, delete
Best case: O(log n) balanced
Worst case: O(n) skewed tree
```

**📝 Problems (3 hours):**

### BST Basics

- [ ]  **LC 700** - Search in a BST
    - Pattern: Binary search on tree
    - Learning: Left or right based on value
    - Time: 10 min target
- [ ]  **LC 701** - Insert into a BST ⭐
    - Pattern: Find position + insert
    - Learning: Recursive insertion
    - Time: 20 min target
- [ ]  **LC 450** - Delete Node in a BST ⭐⭐
    - Pattern: Three cases (leaf, one child, two children)
    - Learning: Complex BST operation
    - Time: 35 min target

### BST Validation

- [ ]  **LC 98** - Validate Binary Search Tree ⭐⭐⭐
    - Pattern: Range validation
    - Learning: In-order or min/max ranges
    - Time: 25 min target
    - **WHY CRITICAL:** Most asked BST problem
- [ ]  **LC 230** - Kth Smallest Element in BST ⭐
    - Pattern: In-order traversal
    - Learning: BST sorted property
    - Time: 20 min target

### BST Applications

- [ ]  **LC 938** - Range Sum of BST
    - Pattern: Prune branches outside range
    - Learning: BST property optimization
    - Time: 15 min target

**🔄 Revision (90 min):**
- [ ] Draw BST and perform insert/delete manually
- [ ] Re-solve LC 98 (extremely important)
- [ ] Compare: Binary Tree vs BST use cases

**✅ Achievement Unlocked:**
Master BST properties and operations

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/6

---

### DAY 26: Advanced Tree Problems - LCA & More 🌳

**🎯 Goal:** Master complex tree algorithms

**📚 Learn (90 min):**
- [ ] Study: Lowest Common Ancestor concept
- [ ] Understand: Tree to list conversions
- [ ] Learn: Tree views (right, left, top, bottom)

**📝 Problems (3 hours):**

### Lowest Common Ancestor

- [ ]  **LC 236** - Lowest Common Ancestor of a Binary Tree ⭐⭐⭐
    - Pattern: Recursion with node tracking
    - Learning: Most important tree problem
    - Time: 30 min target
    - **WHY CRITICAL:** Asked in 70% of tree interviews
- [ ]  **LC 235** - Lowest Common Ancestor of a BST ⭐
    - Pattern: Use BST property
    - Learning: Simpler than general tree
    - Time: 15 min target

### Tree Views

- [ ]  **LC 199** - Binary Tree Right Side View ⭐⭐
    - Pattern: Level order + rightmost node
    - Learning: View from right
    - Time: 20 min target
- [ ]  **LC 515** - Find Largest Value in Each Tree Row
    - Pattern: Level order + max tracking
    - Learning: Row-wise processing
    - Time: 20 min target

### Advanced Problems

- [ ]  **LC 124** - Binary Tree Maximum Path Sum ⭐⭐⭐
    - Pattern: Recursion with global max
    - Learning: Path through node
    - Time: 35 min target
    - **WHY IMPORTANT:** Hard problem testing tree mastery

**🔄 Revision (90 min):**
- [ ] Draw LCA for different node pairs
- [ ] Re-solve LC 236 (critical understanding)
- [ ] Re-solve LC 124 (hard but important)

**✅ Achievement Unlocked:**
Can solve advanced tree problems confidently

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 27: Tries (Prefix Trees) 🌿

**🎯 Goal:** Master trie data structure for string problems

**📚 Learn (90 min):**
- [ ] Watch: Trie visualization
- [ ] Study: Trie node structure
- [ ] Understand: Insert, search, prefix search
- [ ] Learn: Time/space complexity

**🔑 Pattern Template:**

```
Trie Structure:
class TrieNode:
    children = {}  # HashMap of char to TrieNode
    is_end_of_word = False

Operations:
├─ Insert: O(m) where m = word length
├─ Search: O(m)
├─ StartsWith: O(m)
└─ Space: O(N * M) where N = words, M = avg length

Use cases:
- Autocomplete
- Spell checker
- IP routing
- Word search in grid
```

**💡 When to Use Trie:**
- ✅ Multiple words with common prefixes
- ✅ Prefix search / autocomplete
- ✅ Word search in 2D grid
- ✅ Dictionary implementation

**📝 Problems (3 hours):**

### Trie Basics

- [ ]  **LC 208** - Implement Trie (Prefix Tree) ⭐⭐⭐
    - Pattern: Basic trie operations
    - Learning: Trie structure and methods
    - Time: 30 min target
    - **WHY CRITICAL:** Foundation for all trie problems
- [ ]  **LC 211** - Design Add and Search Words Data Structure ⭐⭐
    - Pattern: Trie + wildcard search
    - Learning: DFS in trie
    - Time: 35 min target

### Trie Applications

- [ ]  **LC 212** - Word Search II ⭐⭐⭐
    - Pattern: Trie + DFS backtracking
    - Learning: Complex trie application
    - Time: 50 min target
    - **WHY IMPORTANT:** Combines trie + backtracking
- [ ]  **LC 421** - Maximum XOR of Two Numbers ⭐⭐
    - Pattern: Binary trie
    - Learning: Bit manipulation + trie
    - Time: 40 min target

**🔄 Revision (90 min):**
- [ ] Implement trie from scratch
- [ ] Draw trie for [“cat”, “car”, “card”]
- [ ] Re-solve LC 208 (must be automatic)

**✅ Achievement Unlocked:**
Can use tries for string optimization

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 28: WEEK 4 REVISION + TREE MASTERY TEST 🏆

**🎯 Goal:** Solidify all tree concepts before moving to graphs

**📚 Morning Session (3 hours): Comprehensive Tree Revision**

### Phase 1: Re-solve Key Tree Problems

- [ ]  LC 102 - Binary Tree Level Order (Target: 15 min)
- [ ]  LC 543 - Diameter of Binary Tree (Target: 15 min)
- [ ]  LC 105 - Construct Binary Tree (Target: 25 min)
- [ ]  LC 98 - Validate BST (Target: 20 min)
- [ ]  LC 236 - Lowest Common Ancestor (Target: 20 min)
- [ ]  LC 208 - Implement Trie (Target: 20 min)

### Phase 2: Pattern Templates

- [ ]  Write all 4 traversal templates
- [ ]  Write BST validation template
- [ ]  Write LCA template
- [ ]  Draw trie structure and operations

**📝 Afternoon Session (2 hours): Tree Mock Interview**

**Full Tree Interview (90 minutes):**

- [ ]  **Problem 1 (Easy):** LC 617 - Merge Two Binary Trees
    - Expected: 15 min
    - Pattern: Recursion
- [ ]  **Problem 2 (Medium):** LC 652 - Find Duplicate Subtrees
    - Expected: 30 min
    - Pattern: Serialization + HashMap
- [ ]  **Problem 3 (Medium):** LC 437 - Path Sum III
    - Expected: 30 min
    - Pattern: Prefix sum + trees

**Interview Debrief:**
- [ ] Problems solved: ____/3
- [ ] Explanation quality: **/10
- [ ] Code cleanliness:** /10

**🧠 Evening Session (90 min): Week 4 Complete Analysis**

### Tree Mastery Check:

- Binary Tree Traversals: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Tree Recursion: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- BST Operations: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Tree Construction: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Trie: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

### Week 4 Metrics:

- [ ]  Total problems (cumulative): ____/~100
- [ ]  Tree problems confidence: __/10
- [ ]  Can explain tree recursion clearly: Yes/No

**✅ Week 4 Achievement Unlocked:**
- ✅ Mastered all tree types and operations
- ✅ Comfortable with tree recursion
- ✅ Ready for graphs and advanced patterns

**📊 Overall Progress After 4 Weeks:**
- Patterns Mastered: 22+ total
- Problems Solved: 100+
- Confidence: 8/10
- **MILESTONE: You’re now better than 60-70% of candidates**

**🚀 Preparation for Week 5:**
- [ ] Read about graph representations
- [ ] Watch one BFS/DFS video
- [ ] Review queue implementation

---

# 📗 PHASE 3: GRAPHS & ADVANCED PATTERNS (Days 29-45)

## 🌐 WEEK 5: Graphs - BFS, DFS & Traversals (Days 29-35)

---

### DAY 29: Graph Basics & Representations 🗺️

**🎯 Goal:** Understand graph fundamentals and representations

**📚 Learn (2 hours):**
- [ ] Watch: Graph theory introduction
- [ ] Study: Directed vs undirected graphs
- [ ] Understand: Weighted vs unweighted
- [ ] Learn: Adjacency matrix vs adjacency list

**🔑 Key Concepts:**

```
Graph Representations:

1. Adjacency Matrix: 2D array
   - Space: O(V²)
   - Edge lookup: O(1)
   - Use when: Dense graphs

2. Adjacency List: HashMap of lists
   - Space: O(V + E)
   - Edge lookup: O(degree)
   - Use when: Sparse graphs (most common)

Graph Types:
├─ Undirected: Edges have no direction
├─ Directed (Digraph): Edges have direction
├─ Weighted: Edges have costs
├─ Cyclic vs Acyclic (DAG)
└─ Connected vs Disconnected
```

**💡 Graph Terminology:**
- Vertex/Node: Individual points
- Edge: Connection between vertices
- Degree: Number of edges from vertex
- Path: Sequence of vertices
- Cycle: Path that starts and ends at same vertex
- Connected: Path exists between any two vertices

**📝 Problems (3 hours):**

### Graph Building

- [ ]  **LC 1791** - Find Center of Star Graph
    - Pattern: Graph basics
    - Learning: Simple graph property
    - Time: 10 min target
- [ ]  **LC 997** - Find the Town Judge
    - Pattern: Degree counting
    - Learning: In-degree and out-degree
    - Time: 15 min target

### Graph Representation Practice

- [ ]  **LC 133** - Clone Graph ⭐⭐
    - Pattern: DFS/BFS + HashMap
    - Learning: Graph traversal and cloning
    - Time: 30 min target
- [ ]  Build adjacency list from edge list (custom practice)
    - Given: [[0,1], [0,2], [1,3]]
    - Build: {0: [1,2], 1: [0,3], 2: [0], 3: [1]}

**🔄 Revision (90 min):**
- [ ] Implement both representations from scratch
- [ ] Convert edge list → adj matrix → adj list
- [ ] Draw sample graphs and identify properties

**✅ Achievement Unlocked:**
Understand graph representations and terminology

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/3

---

### DAY 30: DFS (Depth-First Search) 🏊

**🎯 Goal:** Master DFS traversal - most common graph pattern

**📚 Learn (90 min):**
- [ ] Watch: DFS visualization
- [ ] Study: Recursive vs iterative DFS
- [ ] Understand: Visited set importance
- [ ] Learn: DFS on trees vs graphs

**🔑 Pattern Template:**

```
DFS (Recursive):
def dfs(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    process(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited, graph)

DFS (Iterative with Stack):
def dfs(start, graph):
    stack = [start]
    visited = set([start])
    while stack:
        node = stack.pop()
        process(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

Time: O(V + E)
Space: O(V) for visited set + O(H) recursion stack
```

**💡 When to Use DFS:**
- ✅ Path finding
- ✅ Cycle detection
- ✅ Connected components
- ✅ Topological sort (DAG)
- ✅ Maze solving

**📝 Problems (3 hours):**

### DFS Basics

- [ ]  **LC 200** - Number of Islands ⭐⭐⭐
    - Pattern: DFS on 2D grid
    - Learning: Counting connected components
    - Time: 25 min target
    - **WHY CRITICAL:** #1 Most asked graph problem
- [ ]  **LC 695** - Max Area of Island ⭐
    - Pattern: DFS with area counting
    - Learning: Aggregation during DFS
    - Time: 20 min target

### Path Problems

- [ ]  **LC 733** - Flood Fill
    - Pattern: DFS with color change
    - Learning: Grid modification
    - Time: 20 min target
- [ ]  **LC 1020** - Number of Enclaves ⭐
    - Pattern: DFS from boundary
    - Learning: Reverse thinking
    - Time: 25 min target

### Cycle Detection

- [ ]  **LC 547** - Number of Provinces ⭐
    - Pattern: DFS on adjacency matrix
    - Learning: Connected components in graph
    - Time: 25 min target

**🔄 Revision (90 min):**
- [ ] Implement DFS both recursively and iteratively
- [ ] Re-solve LC 200 (MUST be automatic)
- [ ] Draw DFS traversal order on sample graph

**✅ Achievement Unlocked:**
Master DFS for any graph traversal

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 31: BFS (Breadth-First Search) 🌊

**🎯 Goal:** Master BFS - shortest path in unweighted graphs

**📚 Learn (90 min):**
- [ ] Watch: BFS visualization
- [ ] Study: Level-by-level traversal
- [ ] Understand: Queue usage for BFS
- [ ] Learn: When BFS beats DFS

**🔑 Pattern Template:**

```
BFS (Queue-based):
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        process(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

Time: O(V + E)
Space: O(V) for queue and visited

BFS vs DFS:
├─ BFS: Shortest path in unweighted graph
├─ BFS: Level-order traversal
├─ DFS: Path finding, cycle detection
└─ DFS: Uses less memory for deep graphs
```

**💡 When to Use BFS:**
- ✅ Shortest path (unweighted)
- ✅ Level-by-level processing
- ✅ Minimum steps/distance
- ✅ Word ladder type problems

**📝 Problems (3 hours):**

### BFS Basics

- [ ]  **LC 994** - Rotting Oranges ⭐⭐⭐
    - Pattern: Multi-source BFS
    - Learning: Time-based propagation
    - Time: 30 min target
    - **WHY IMPORTANT:** Classic BFS problem
- [ ]  **LC 1091** - Shortest Path in Binary Matrix ⭐⭐
    - Pattern: BFS for shortest path
    - Learning: 8-directional movement
    - Time: 30 min target

### Level Processing

- [ ]  **LC 1730** - Shortest Path to Get Food
    - Pattern: BFS with obstacles
    - Learning: Grid navigation
    - Time: 25 min target
- [ ]  **LC 863** - All Nodes Distance K in Binary Tree ⭐⭐
    - Pattern: Tree to graph + BFS
    - Learning: BFS on tree
    - Time: 35 min target

### Word Problems

- [ ]  **LC 127** - Word Ladder ⭐⭐⭐
    - Pattern: BFS on word graph
    - Learning: Implicit graph construction
    - Time: 40 min target
    - **WHY CRITICAL:** Tests BFS + graph building

**🔄 Revision (90 min):**
- [ ] Implement BFS from scratch
- [ ] Compare BFS vs DFS for same problem
- [ ] Re-solve LC 994 (important pattern)

**✅ Achievement Unlocked:**
Know when to use BFS over DFS

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 32: Topological Sort & Cycle Detection 🔄

**🎯 Goal:** Master DAG (Directed Acyclic Graph) algorithms

**📚 Learn (90 min):**
- [ ] Watch: Topological sort explanation
- [ ] Study: Kahn’s algorithm (BFS-based)
- [ ] Understand: DFS-based topological sort
- [ ] Learn: Cycle detection in directed graphs

**🔑 Pattern Template:**

```
Topological Sort (Kahn's Algorithm - BFS):
1. Calculate in-degree for all nodes
2. Add nodes with in-degree 0 to queue
3. Process queue:
   - Remove node
   - Decrease in-degree of neighbors
   - Add neighbors with in-degree 0 to queue
4. If all nodes processed → DAG, else cycle exists

Cycle Detection (DFS with colors):
WHITE (0): Unvisited
GRAY (1): Visiting (in current path)
BLACK (2): Visited (path complete)

If we reach a GRAY node → Cycle exists

Time: O(V + E)
```

**💡 Topological Sort Use Cases:**
- ✅ Course prerequisites
- ✅ Build systems (dependencies)
- ✅ Task scheduling
- ✅ Deadlock detection

**📝 Problems (3 hours):**

### Topological Sort

- [ ]  **LC 207** - Course Schedule ⭐⭐⭐
    - Pattern: Cycle detection
    - Learning: Can finish all courses?
    - Time: 30 min target
    - **WHY CRITICAL:** Most asked topological sort
- [ ]  **LC 210** - Course Schedule II ⭐⭐⭐
    - Pattern: Topological sort order
    - Learning: Kahn’s algorithm
    - Time: 30 min target

### Dependency Problems

- [ ]  **LC 310** - Minimum Height Trees ⭐⭐
    - Pattern: Reverse topological (trim leaves)
    - Learning: Center of tree
    - Time: 35 min target
- [ ]  **LC 269** - Alien Dictionary ⭐⭐⭐
    - Pattern: Build graph + topological sort
    - Learning: Complex dependency extraction
    - Time: 45 min target
    - **WHY IMPORTANT:** Hard but important pattern

**🔄 Revision (90 min):**
- [ ] Draw topological sort step-by-step
- [ ] Implement both Kahn’s and DFS approaches
- [ ] Re-solve LC 207 and 210 (critical problems)

**✅ Achievement Unlocked:**
Master DAG algorithms and cycle detection

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 33: Union-Find (Disjoint Set) 🔗

**🎯 Goal:** Master Union-Find for connected components

**📚 Learn (2 hours):**
- [ ] Watch: Union-Find visualization
- [ ] Study: Path compression optimization
- [ ] Understand: Union by rank/size
- [ ] Learn: Time complexity analysis

**🔑 Pattern Template:**

```
Union-Find (Disjoint Set):

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        self.components -= 1
        return True

Time: O(α(n)) ≈ O(1) amortized (with optimizations)
α(n) = Inverse Ackermann (practically constant)
```

**💡 When to Use Union-Find:**
- ✅ Connected components in undirected graph
- ✅ Cycle detection in undirected graph
- ✅ Kruskal’s MST algorithm
- ✅ Network connectivity
- ✅ Dynamic connectivity

**📝 Problems (3 hours):**

### Union-Find Basics

- [ ]  **LC 323** - Number of Connected Components in Undirected Graph ⭐⭐
    - Pattern: Basic union-find
    - Learning: Counting components
    - Time: 25 min target
- [ ]  **LC 684** - Redundant Connection ⭐⭐
    - Pattern: Cycle detection with union-find
    - Learning: Finding extra edge
    - Time: 25 min target

### Advanced Applications

- [ ]  **LC 685** - Redundant Connection II ⭐⭐⭐
    - Pattern: Union-find in directed graph
    - Learning: Complex edge removal
    - Time: 45 min target
- [ ]  **LC 547** - Number of Provinces (Alternative) ⭐
    - Pattern: Union-find approach
    - Learning: Compare with DFS solution
    - Time: 20 min target
- [ ]  **LC 959** - Regions Cut By Slashes ⭐⭐
    - Pattern: Union-find on grid
    - Learning: Creative problem modeling
    - Time: 40 min target

**🔄 Revision (90 min):**
- [ ] Implement Union-Find from memory
- [ ] Draw path compression effect
- [ ] Compare union-find vs DFS for same problem

**✅ Achievement Unlocked:**
Master Union-Find for connectivity problems

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/5

---

### DAY 34: Shortest Path Algorithms (Dijkstra) 🛣️

**🎯 Goal:** Master weighted graph shortest path

**📚 Learn (2 hours):**
- [ ] Watch: Dijkstra’s algorithm visualization
- [ ] Study: Priority queue (min-heap) usage
- [ ] Understand: Why greedy works here
- [ ] Learn: Bellman-Ford (negative weights)

**🔑 Pattern Template:**

```
Dijkstra's Algorithm:

import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist

Time: O((V + E) log V) with min-heap
Space: O(V)

Use when: Weighted graph, non-negative weights
```

**💡 Shortest Path Algorithms:**
- ✅ Dijkstra: Non-negative weights, single source
- ✅ Bellman-Ford: Negative weights allowed
- ✅ Floyd-Warshall: All pairs shortest path
- ✅ BFS: Unweighted graphs (special case)

**📝 Problems (3 hours):**

### Dijkstra Implementation

- [ ]  **LC 743** - Network Delay Time ⭐⭐⭐
    - Pattern: Basic Dijkstra
    - Learning: Shortest path to all nodes
    - Time: 30 min target
    - **WHY IMPORTANT:** Classic Dijkstra problem
- [ ]  **LC 1514** - Path with Maximum Probability ⭐⭐
    - Pattern: Dijkstra with max instead of min
    - Learning: Modified priority queue
    - Time: 30 min target

### Path Reconstruction

- [ ]  **LC 787** - Cheapest Flights Within K Stops ⭐⭐⭐
    - Pattern: Dijkstra with constraints
    - Learning: Limited stops
    - Time: 40 min target
- [ ]  **LC 1631** - Path With Minimum Effort ⭐⭐
    - Pattern: Dijkstra on 2D grid
    - Learning: Grid as graph
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Implement Dijkstra from scratch
- [ ] Draw shortest path tree step-by-step
- [ ] Re-solve LC 743 (fundamental)

**✅ Achievement Unlocked:**
Master shortest path algorithms

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/4

---

### DAY 35: WEEK 5 REVISION + GRAPH MASTERY 🏆

**🎯 Goal:** Consolidate all graph patterns

**📚 Morning Session (3 hours): Graph Pattern Review**

### Phase 1: Re-solve Core Problems

- [ ]  LC 200 - Number of Islands (Target: 15 min)
- [ ]  LC 994 - Rotting Oranges (Target: 20 min)
- [ ]  LC 207 - Course Schedule (Target: 20 min)
- [ ]  LC 684 - Redundant Connection (Target: 15 min)
- [ ]  LC 743 - Network Delay Time (Target: 25 min)

### Phase 2: Pattern Comparison

- [ ]  When to use DFS vs BFS?
- [ ]  When to use Union-Find vs DFS?
- [ ]  When to use Dijkstra vs BFS?
- [ ]  Draw decision tree for graph problems

**📝 Afternoon Session (2 hours): Graph Mock Interview**

- [ ]  **Problem 1 (Medium):** LC 417 - Pacific Atlantic Water Flow
    - Expected: 30 min
    - Pattern: DFS from boundary
- [ ]  **Problem 2 (Medium):** LC 399 - Evaluate Division
    - Expected: 35 min
    - Pattern: Graph + DFS/BFS
- [ ]  **Problem 3 (Hard):** LC 1168 - Optimize Water Distribution
    - Expected: 40 min
    - Pattern: Union-Find + MST

**Interview Performance:**
- [ ] Problems solved: ____/3
- [ ] Explanation clarity: **/10
- [ ] Code quality:** /10

**🧠 Evening Session: Week 5 Complete Analysis**

### Graph Mastery Check:

- DFS: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- BFS: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Topological Sort: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Union-Find: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
- Dijkstra: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

### Week 5 Metrics:

- [ ]  Total problems (cumulative): ____/~125
- [ ]  Graph confidence: __/10

**✅ Week 5 Achievement:**
- ✅ Mastered all major graph algorithms
- ✅ Can solve 90% of graph interview problems
- ✅ Ready for advanced patterns

---

## 🌟 WEEK 6: Advanced Patterns - Binary Search, Heap, Greedy (Days 36-42)

---

### DAY 36: Binary Search Mastery 🔍

**🎯 Goal:** Master binary search and all its variations

**📚 Learn (2 hours):**
- [ ] Watch: Binary search variations
- [ ] Study: Search space reduction technique
- [ ] Understand: Finding boundaries (first/last occurrence)
- [ ] Learn: Binary search on answer

**🔑 Pattern Template:**

```
Classic Binary Search:
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

Binary Search Template (Generic):
def binary_search(condition):
    left, right = min_val, max_val
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid  # Search left half
        else:
            left = mid + 1  # Search right half
    return left

Time: O(log n)
```

**💡 Binary Search Variations:**
- ✅ Find exact value
- ✅ Find first/last occurrence
- ✅ Find insertion position
- ✅ Search in rotated array
- ✅ Binary search on answer space

**📝 Problems (3 hours):**

### Basics

- [ ]  **LC 704** - Binary Search
    - Pattern: Classic template
    - Learning: Foundation
    - Time: 10 min target
- [ ]  **LC 35** - Search Insert Position
    - Pattern: Finding insertion index
    - Learning: Boundary handling
    - Time: 15 min target

### First/Last Occurrence

- [ ]  **LC 34** - Find First and Last Position ⭐⭐
    - Pattern: Two binary searches
    - Learning: Finding boundaries
    - Time: 25 min target

### Rotated Array

- [ ]  **LC 33** - Search in Rotated Sorted Array ⭐⭐⭐
    - Pattern: Modified binary search
    - Learning: Which half is sorted?
    - Time: 25 min target
    - **WHY CRITICAL:** Very common variation
- [ ]  **LC 81** - Search in Rotated Array II ⭐⭐
    - Pattern: Handle duplicates
    - Learning: Worst case O(n)
    - Time: 25 min target
- [ ]  **LC 153** - Find Minimum in Rotated Array ⭐⭐
    - Pattern: Finding pivot
    - Learning: Min element search
    - Time: 20 min target

### Binary Search on Answer

- [ ]  **LC 875** - Koko Eating Bananas ⭐⭐⭐
    - Pattern: Binary search on speed
    - Learning: Search answer space
    - Time: 30 min target
    - **WHY IMPORTANT:** Tests BS on answer concept

**🔄 Revision (90 min):**
- [ ] Implement all BS templates
- [ ] Re-solve LC 33 (very important)
- [ ] Practice finding first/last occurrence

**✅ Achievement Unlocked:**
Can apply binary search to any search space

**📊 Self-Assessment:**
- Understanding: ⭐⭐⭐⭐⭐
- Speed: ⭐⭐⭐⭐⭐
- Confidence: ⭐⭐⭐⭐⭐
- Problems solved today: ____/7

---

### DAY 37: Advanced Binary Search 🎯

**🎯 Goal:** Master complex binary search applications

**📝 Problems (3 hours):**

### Matrix Binary Search

- [ ]  **LC 74** - Search a 2D Matrix ⭐
    - Pattern: Treat 2D as 1D array
    - Learning: Index conversion
    - Time: 20 min target
- [ ]  **LC 240** - Search a 2D Matrix II ⭐⭐
    - Pattern: Start from top-right
    - Learning: Elimination technique
    - Time: 25 min target

### Capacity/Speed Problems

- [ ]  **LC 1011** - Capacity To Ship Packages Within D Days ⭐⭐⭐
    - Pattern: BS on capacity
    - Learning: Feasibility check
    - Time: 35 min target
- [ ]  **LC 410** - Split Array Largest Sum ⭐⭐⭐
    - Pattern: BS on answer
    - Learning: Complex feasibility
    - Time: 40 min target
- [ ]  **LC 1482** - Minimum Number of Days to Make m Bouquets ⭐⭐
    - Pattern: BS on days
    - Learning: Counting technique
    - Time: 30 min target

**🔄 Revision (90 min):**
- [ ] Re-solve all “BS on answer” problems
- [ ] Write feasibility function template
- [ ] Practice explaining BS approach clearly

**✅ Achievement Unlocked:**
Master advanced binary search patterns

**📊 Self-Assessment:**
- Problems solved today: ____/5

---

### DAY 38: Heap / Priority Queue 📊

**🎯 Goal:** Master heap for optimization problems

**📚 Learn (90 min):**
- [ ] Watch: Min-heap and max-heap explanation
- [ ] Study: Heapify operation
- [ ] Understand: When to use heap
- [ ] Learn: Top K problems pattern

**🔑 Pattern Template:**

```
Min Heap in Python:
import heapq

# Min heap operations
heap = []
heapq.heappush(heap, item)  # O(log n)
min_item = heapq.heappop(heap)  # O(log n)
min_item = heap[0]  # O(1) peek

# Max heap (negate values)
heap = []
heapq.heappush(heap, -item)
max_item = -heapq.heappop(heap)

# Heapify existing list
heapq.heapify(list)  # O(n)

Time: Insert/Delete O(log n), Peek O(1)
```

**💡 When to Use Heap:**
- ✅ Top K elements
- ✅ Kth largest/smallest
- ✅ Merge K sorted lists/arrays
- ✅ Running median
- ✅ Task scheduling with priorities

**📝 Problems (3 hours):**

### Top K Problems

- [ ]  **LC 215** - Kth Largest Element ⭐⭐⭐
    - Pattern: Min-heap of size K
    - Learning: Top K technique
    - Time: 20 min target
- [ ]  **LC 347** - Top K Frequent Elements ⭐⭐⭐
    - Pattern: Heap + frequency map
    - Learning: Sorting by frequency
    - Time: 25 min target
- [ ]  **LC 973** - K Closest Points to Origin ⭐⭐
    - Pattern: Max-heap of size K
    - Learning: Distance calculation
    - Time: 20 min target

### Merge Problems

- [ ]  **LC 23** - Merge k Sorted Lists ⭐⭐⭐
    - Pattern: Min-heap for merging
    - Learning: K-way merge
    - Time: 30 min target
    - **WHY CRITICAL:** Classic heap problem
- [ ]  **LC 378** - Kth Smallest Element in Sorted Matrix ⭐⭐
    - Pattern: Min-heap with matrix
    - Learning: Matrix traversal
    - Time: 30 min target

### Advanced Heap

- [ ]  **LC 295** - Find Median from Data Stream ⭐⭐⭐
    - Pattern: Two heaps (max + min)
    - Learning: Running median
    - Time: 35 min target
    - **WHY IMPORTANT:** Classic two-heap problem

**🔄 Revision (90 min):**
- [ ] Implement heap operations manually
- [ ] Re-solve LC 23 and LC 295 (critical)
- [ ] Practice top K pattern on custom data

**✅ Achievement Unlocked:**
Master heap for optimization

**📊 Self-Assessment:**
- Problems solved today: ____/6

---

### DAY 39: Greedy Algorithms 💡

**🎯 Goal:** Recognize when greedy approach works

**📚 Learn (90 min):**
- [ ] Watch: Greedy algorithm explanation
- [ ] Study: When greedy is optimal
- [ ] Understand: Greedy choice property
- [ ] Learn: Proof of correctness

**🔑 Key Concepts:**

```
Greedy Algorithm:
├─ Make locally optimal choice at each step
├─ Hope local optimum → global optimum
├─ Works when problem has "greedy choice property"
└─ Must prove correctness (or trust LeetCode)

Common Greedy Patterns:
1. Activity Selection (intervals)
2. Jump problems (array)
3. Gas station (circular)
4. Minimum platforms (scheduling)
5. Huffman coding (trees)
```

**💡 When Greedy Works:**
- ✅ Optimal substructure exists
- ✅ Greedy choice property holds
- ✅ Problem asks for “minimum/maximum”
- ✅ Local optimum leads to global

**📝 Problems (3 hours):**

### Jump Problems

- [ ]  **LC 55** - Jump Game ⭐⭐⭐
    - Pattern: Greedy reach tracking
    - Learning: Can reach end?
    - Time: 20 min target
- [ ]  **LC 45** - Jump Game II ⭐⭐⭐
    - Pattern: Greedy with jump count
    - Learning: Minimum jumps
    - Time: 30 min target

### Interval Problems

- [ ]  **LC 134** - Gas Station ⭐⭐⭐
    - Pattern: Greedy with deficit tracking
    - Learning: Circular array
    - Time: 30 min target
    - **WHY IMPORTANT:** Tricky greedy logic
- [ ]  **LC 406** - Queue Reconstruction by Height ⭐⭐
    - Pattern: Sort + greedy insertion
    - Learning: Two-step greedy
    - Time: 30 min target

### Other Greedy

- [ ]  **LC 621** - Task Scheduler ⭐⭐
    - Pattern: Greedy with frequency
    - Learning: Idle time calculation
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Re-solve LC 55 and 45 (important jump problems)
- [ ] Practice explaining why greedy works
- [ ] Compare greedy vs DP for same problem

**✅ Achievement Unlocked:**
Recognize and apply greedy strategies

**📊 Self-Assessment:**
- Problems solved today: ____/5

---

### DAY 40: Monotonic Stack Advanced + Backtracking Intro 🔙

**🎯 Goal:** Complex monotonic stack + backtracking preview

**📝 Problems (3 hours):**

### Hard Monotonic Stack

- [ ]  **LC 316** - Remove Duplicate Letters ⭐⭐⭐
    - Pattern: Monotonic stack + greedy
    - Learning: Lexicographic order
    - Time: 40 min target
- [ ]  **LC 402** - Remove K Digits ⭐⭐
    - Pattern: Monotonic increasing stack
    - Learning: Number minimization
    - Time: 35 min target

### Backtracking Introduction

- [ ]  **LC 78** - Subsets ⭐⭐⭐
    - Pattern: Basic backtracking
    - Learning: Power set generation
    - Time: 25 min target
    - **WHY IMPORTANT:** Foundation for backtracking
- [ ]  **LC 90** - Subsets II ⭐⭐
    - Pattern: Backtracking with duplicates
    - Learning: Duplicate handling
    - Time: 30 min target

**🔄 Revision (90 min):**
- [ ] Review all monotonic stack problems
- [ ] Practice backtracking template
- [ ] Draw recursion tree for subsets

**✅ Achievement Unlocked:**
Ready for complex patterns

**📊 Self-Assessment:**
- Problems solved today: ____/4

---

### DAY 41: Bit Manipulation Advanced 🔢

**🎯 Goal:** Master advanced bit manipulation tricks

**📝 Problems (3 hours):**

### Bit Counting

- [ ]  **LC 190** - Reverse Bits
    - Pattern: Bit shifting
    - Learning: Bit reversal
    - Time: 20 min target
- [ ]  **LC 201** - Bitwise AND of Numbers Range ⭐⭐
    - Pattern: Common prefix finding
    - Learning: Range bit operations
    - Time: 25 min target

### Bit Tricks

- [ ]  **LC 137** - Single Number II ⭐⭐
    - Pattern: Bit counting (appears 3 times)
    - Learning: Advanced XOR
    - Time: 35 min target
- [ ]  **LC 260** - Single Number III ⭐⭐
    - Pattern: XOR partitioning
    - Learning: Finding two singles
    - Time: 35 min target

**🔄 Revision (90 min):**
- [ ] Review all bit manipulation patterns
- [ ] Create bit tricks cheat sheet

**✅ Achievement Unlocked:**
Master bit manipulation

**📊 Self-Assessment:**
- Problems solved today: ____/4

---

### DAY 42: WEEK 6 REVISION + PATTERN CONSOLIDATION 🏆

**🎯 Goal:** Master all advanced patterns before DP

**📚 Full Day Revision (6 hours):**

### Morning: Pattern Review

- [ ]  Binary Search: Re-solve 5 problems
- [ ]  Heap: Re-solve 3 problems
- [ ]  Greedy: Re-solve 3 problems
- [ ]  Write templates for each pattern

### Afternoon: Mock Contest

- [ ]  3 Medium problems (90 min timer)
- [ ]  Focus on speed and accuracy
- [ ]  Simulate interview pressure

### Evening: Weak Area Focus

- [ ]  Identify weakest pattern
- [ ]  Solve 3 more problems in that area
- [ ]  Review mistakes and improve

**✅ Week 6 Complete:**
- ✅ 150+ total problems solved
- ✅ Ready for Dynamic Programming
- ✅ Confidence: 8.5/10

---

# 🧮 PHASE 4: DYNAMIC PROGRAMMING & BACKTRACKING (Days 43-55)

## WEEK 7: Dynamic Programming Fundamentals (Days 43-49)

---

### DAY 43-49: Complete DP Coverage

*Note: This section would include all DP patterns from the original roadmap:*
- Day 43: DP Introduction + 1D DP
- Day 44: Take/Not Take (0/1 Knapsack)
- Day 45: Infinite Supply
- Day 46: DP on Strings (LCS, Edit Distance)
- Day 47: DP on Grids
- Day 48: DP on Stocks
- Day 49: Week 7 Revision

---

## WEEK 8: Advanced DP & Final Preparation (Days 50-56)

### DAY 50-55: Backtracking + Final Topics

- Day 50: Backtracking Patterns
- Day 51: N-Queens + Sudoku
- Day 52: Partition DP
- Day 53: Advanced Backtracking
- Day 54: System Design Introduction
- Day 55: Week 8 Revision

---

### DAY 56-60: FINAL SPRINT - MOCK INTERVIEWS & COMPANY-SPECIFIC 🚀

**🎯 Goal:** Interview-ready with company-specific practice

### DAY 56-58: Company-Specific Problems

- [ ]  **Amazon:** 10 tagged problems
- [ ]  **Google:** 10 tagged problems
- [ ]  **Microsoft:** 10 tagged problems
- [ ]  **Meta:** 10 tagged problems

### DAY 59: Full Mock Interviews

- [ ]  Morning: 2-hour coding interview simulation
- [ ]  Afternoon: System design basics
- [ ]  Evening: Behavioral questions prep

### DAY 60: FINAL REVISION

- [ ]  Review all pattern templates
- [ ]  Re-solve 20 hardest problems
- [ ]  Confidence check: Should be 9/10+

---

## 🎯 FINAL COMPLETION CHECKLIST

### Pattern Mastery (Check all 25+):

- [ ]  Two Pointers
- [ ]  Sliding Window (Fixed & Variable)
- [ ]  Prefix Sum
- [ ]  Hashing
- [ ]  Fast-Slow Pointers
- [ ]  Cyclic Sort
- [ ]  Sorting Algorithms
- [ ]  Intervals
- [ ]  Linked Lists
- [ ]  Stack
- [ ]  Monotonic Stack
- [ ]  Queue/Deque
- [ ]  Binary Trees (All Traversals)
- [ ]  BST
- [ ]  Trie
- [ ]  Graphs (DFS/BFS)
- [ ]  Topological Sort
- [ ]  Union-Find
- [ ]  Dijkstra
- [ ]  Binary Search (All Variants)
- [ ]  Heap
- [ ]  Greedy
- [ ]  DP (All Types)
- [ ]  Backtracking
- [ ]  Design Problems

### Overall Metrics:

- [ ]  Total Problems Solved: 220+ ✅
- [ ]  Can solve Easy in: 10-15 min
- [ ]  Can solve Medium in: 25-35 min
- [ ]  Can explain approach before coding
- [ ]  Mock interview performance: 8+/10
- [ ]  Confidence level: 9-10/10

---

## 🎊 CONGRATULATIONS! YOU’RE NOW IN THE TOP 1%

**What You’ve Achieved:**
✅ Mastered 25+ interview patterns
✅ Solved 220+ curated problems
✅ Can tackle any DSA interview question
✅ Ready for Google, Amazon, Microsoft, Meta, and any top company

**Your Advantage:**
- Pattern recognition is AUTOMATIC
- You think in templates, not brute force
- 30-minute problem-solving speed
- Can explain approach clearly

**Next Steps:**
1. Apply to 20+ companies immediately
2. Schedule interviews starting Week 10
3. Continue 1-2 problems daily to stay sharp
4. Focus on company-specific interview prep

---

## 💪 MOTIVATION FOR TOUGH DAYS

**When Week 6 (DP) feels impossible:**
“DP is pattern recognition, not magic. After 50 DP problems, it clicks.”

**When you want to quit:**
“You’re jobless NOW but won’t be for long. This is temporary pain for permanent gain.”

**When progress feels slow:**
“Every problem you solve is one step closer to 15+ LPA at a product company.”

**Remember:**
The pain of discipline is temporary.
The pain of regret lasts forever.

**You’ve got this! 🔥**

---

*Track your daily progress, stay consistent, and trust the process. See you at Google/Amazon in 60 days!*