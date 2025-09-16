<div align="center">

# 🧠 [2579. Count Total Number of Colored Cells](https://leetcode.com/problems/count-total-number-of-colored-cells/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202579-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/count-total-number-of-colored-cells/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                          |
| **Acceptance Rate** | `66.2%`                                                                                |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/count-total-number-of-colored-cells/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                     |

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## Description

<!-- description:start -->

<p>There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer <code>n</code>, indicating that you must do the following routine for <code>n</code> minutes:</p>

<ul>
	<li>At the first minute, color <strong>any</strong> arbitrary unit cell blue.</li>
	<li>Every minute thereafter, color blue <strong>every</strong> uncolored cell that touches a blue cell.</li>
</ul>

<p>Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2500-2599/2579.Count%20Total%20Number%20of%20Colored%20Cells/images/example-copy-2.png" style="width: 500px; height: 279px;" />
<p>Return <em>the number of <strong>colored cells</strong> at the end of </em><code>n</code> <em>minutes</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> After 1 minute, there is only 1 blue cell, so we return 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## 🔗 Related Problems

| Problem                                                                                           | Difficulty  | Relationship  |
| ------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| [Minimum Cuts to Divide a Circle](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - We can simulate the grid growth minute by minute.
> - Start with one colored cell.
> - At each step, expand outward to all adjacent cells.
> - Use a set (or matrix) to keep track of colored cells.
> - This is intuitive but impossible for n = 10^5 (too slow, too much memory).

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    grid = set()
    add (0,0) as starting cell
    for minute = 2..n:
        newCells = all neighbors of currently colored cells
        add to grid
    return size of grid
```

#### 💻 Implementation

```cpp
// Brute force simulation (works only for small n, e.g. n <= 10)

class Solution {
public:
    int solutionBruteForce(int n) {
        set<pair<int,int>> colored;
        colored.insert({0, 0}); // start with one cell

        // Directions (up, down, left, right)
        vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        for (int minute = 2; minute <= n; minute++) {
            set<pair<int,int>> newCells;
            for (auto &cell : colored) {
                for (auto &d : dirs) {
                    int x = cell.first + d.first;
                    int y = cell.second + d.second;
                    if (!colored.count({x, y})) {
                        newCells.insert({x, y});
                    }
                }
            }
            // Add all new cells
            for (auto &c : newCells) colored.insert(c);
        }
        return colored.size();
    }
};
```

### 🥈 Approach 2: Optimized Solution - Pattern Recognition (Iterative Formula)

#### 📝 Intuition

📝 **Intuition**

> - After 1 minute → 1 cell.
> - After 2 minutes → 5 cells.
> - After 3 minutes → 13 cells.
> - After 4 minutes → 25 cells.
> - Notice: the shape is a diamond (rhombus) expanding each minute.
> - At minute k, the new layer adds \(4 \cdot (k-1)\) cells.
> - So total colored cells: $\text{total}(n) = 1 + \sum_{i=2}^{n} 4 \cdot (i-1)$

#### 🔍 Algorithm

```pseudo
function iterative(n):
    total = 1
    for i = 2..n:
        total += 4 * (i-1)
    return total
```

#### 💻 Implementation

```cpp
// Optimized approach with Iterative pattern recognition

class Solution {
public:
    long long solutionIterative(int n) {
        long long total = 1;
        for (int i = 2; i <= n; i++) {
            total += 4LL * (i - 1);
        }
        return total;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Closed Formula)

#### 📝 Intuition

> > From the iterative formula:
> > From the iterative formula:
>
> $$
> \text{total}(n) = 1 + 4 \cdot (1 + 2 + 3 + \cdots + (n-1))
> $$
>
> We know:
>
> $$
> 1 + 2 + \cdots + (n-1) = \frac{(n-1)n}{2}
> $$
>
> So:
>
> $$
> \text{total}(n) = 1 + 4 \cdot \frac{(n-1)n}{2} = 1 + 2n(n-1)
> $$
>
> Final closed formula:
>
> $$
> \text{total}(n) = 2n^2 - 2n + 1
> $$

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return 2 * n * n - 2 * n + 1
```

#### 💻 Implementation

```cpp
// Most optimal approach with closed formula O(1)

class Solution {
public:
    long long coloredCells(int n) {
        return 2LL * n * n - 2LL * n + 1;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                         | Cons                         |
| -------------- | --------------- | ---------------- | ---------------------------- | ---------------------------- |
| 🥉 Brute Force | Exponential     | Very High        | Intuitive simulation         | Not feasible for n > 10      |
| 🥈 Iterative   | O(n)            | O(1)             | Simple formula, easy to code | Slow for very large n (10^5) |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant closed-form solution | Requires math insight        |

---

<div align="center">

**🎯 Problem 2579 Completed!**

_Happy Coding! 🚀_

</div>
