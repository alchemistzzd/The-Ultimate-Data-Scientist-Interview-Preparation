# DFS-Depth First Search (Recursion)

- Binary trees

- Binary search trees

## Direct recursion vs Indirect recursion

Direct recursion:

Base case: when the recursion stops;

Recursive case: when the recursion needs to continue;

The progrom should do to the recrusive case until the base case is met.

Indirect recursion : 

Functions call each other in a cycle

# Indications to use recursion

1. subprocess

2. You do not know how many number of loops you need to do


## Keys

1. The key of writing the recursion part is to determine what operation(function or operation itself) we need to do with next node repetitively until we found what we need; For problems where we need to track values, what is the child node returning to the parent node exactly?

2. Sometimes defining the sub-recursion part as variables ahead will make the code much easier to understand, and more efficient.

3. Always need a visited since you do not want to do dfs on the same node again

# BFS(Breath First Search) - Queue

- double ended queue: q = deque(); q.leftpop()

- "while q" is used since we will be doing bfs until there is no element left in q

- if for BFS you want to track how many levels we go down, you need to do for i in range(len(q)), so you have a separate for loop for each level

- When do we need visited when do I not need it? If visiting the same cell again will result in same operations again

- When to add cell to visited? More standard pattern is to mark a node as visited when you enqueue it, not when you dequeue. Otherwise, the same position can be enqueued multiple times from different paths



# Integers / Bit Manipulation
- Hamming Weight (#191 Number of 1 Bits)

Bit shift one place to the right: n = n >> 1

- Basic Calculator (#224)

Skipped for now

- Integers Rescaling

Reverse Integer: 

sign = 1 if x>0 else -1; after turning x to positive, res > 2^31 - 1 not res > 2^31  because the biggest is  2**31 - 1

- Moving Average from Data Stream

**Edge case is when the number of data points in the stream is smaller than the side of the window, then we need to divide by actual number of data points rather than window size**

self.list[-self.size:] creates a new list copy of size k

sum(...) loops over k elements

So each next() call is: O(k)

If next() is called n times: O(nk)

Use deque() for sliding windows

- Hit Counter

**Either hit or getHit will happen every time, when hit happens just add it to the queue, but when getHit happens need to examine and trim the queue**

remove timestamps in getHits not in hit. Time and space is O(1), O(k), time is O(k) for worst case but since every element only get added and removed once, amortized time is O(1)

- Sorting

Why is time complexity nlog(n)?
Sorting functions work by dividing by two, look at each element, hence n, and then dividing by two again, hence log(n), hence nlog(n)

- Car Fleet

**We only need to check if each car catches up with the immediate car in front of it. If it does, we can remove the car, since they will be one fleet**

- If sorting

Space: O(n)

- Shortest distance from buildings

1. BFS should be reset at each building. So q is reset each building

2. when using -1 each time to mark visited, did you actually mark visited??

- Find Peak Element

When doing binary search, since mid = (left + right) // 2, mid <= right - 1(imagine if we have odd numbers, mid would be the middle one, if we have even numbers, mid would be middle left, since //2 is flooring)

- Possible Bipartition

1. When we reach a node that is not colored yet (not visited yet), it means we are starting a disconnected part of the graph

2. There could be case that a node is not in the neighbor map, so when checking neighbors for a node, there could be that a key does not exist in the neighbor map to start with

3. When doing coloring inside bfs, because we do not know the color of the node, so the neighors' color should be -color of node, not -1 necessarily

- Valid Sudoku
** Use sets for each row, col and mini 9*9 board, check if a val has already been in the same row or col or miniboard.**

1. The index for mini board is created by row//3, col//3

2. First need to check if a cell is empty


- Big-O combination

Rule 1: Take the larger term if one dominates the other

Rule 2: Add them if the runtimes happen sequentially

Rule 3: Multiply them if nested

