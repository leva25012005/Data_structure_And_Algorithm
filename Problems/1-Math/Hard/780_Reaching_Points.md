<div align="center">

# 🧠 [780. Reaching Points](https://leetcode.com/problems/reaching-points/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20780-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/reaching-points/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🔴 **Hard**                                                        |
| **Acceptance Rate** | `33.8%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/reaching-points/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given four integers <code>sx</code>, <code>sy</code>, <code>tx</code>, and <code>ty</code>, return <code>true</code><em> if it is possible to convert the point </em><code>(sx, sy)</code><em> to the point </em><code>(tx, ty)</code> <em>through some operations</em><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>The allowed operation on some point <code>(x, y)</code> is to convert it to either <code>(x, x + y)</code> or <code>(x + y, y)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sx = 1, sy = 1, tx = 3, ty = 5
<strong>Output:</strong> true
<strong>Explanation:</strong>
One series of moves that transforms the starting point to the target is:
(1, 1) -&gt; (1, 2)
(1, 2) -&gt; (3, 2)
(3, 2) -&gt; (3, 5)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sx = 1, sy = 1, tx = 2, ty = 2
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> sx = 1, sy = 1, tx = 1, ty = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sx, sy, tx, ty &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `16-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `16-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                             | Difficulty    | Relationship    |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) | 🟡 **Medium** | Similar logic   |
| [Check if Point Is Reachable](https://leetcode.com/problems/check-if-point-is-reachable/)                                                           | 🔴 **Hard**   | Related concept |
| [Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)                 | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Coursera** 🔥 97.8%
- **J.P. Morgan** 🔥 96.5%
- **Workday** 🔥 88.0%
- **Cloudflare** 🔥 84.3%
- **KLA** 🔥 80.3%

### ⭐ Medium Frequency (60-79%)

- **Docusign** ⭐ 77.0%
- **Wayfair** ⭐ 63.4%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Forward Simulation)

#### 📝 Intuition

> - Start from (sx, sy) and try all possible moves (x, x+y) or (x+y, y) until reaching (tx, ty).
> - Use recursion/DFS or BFS to explore all possible paths.
> - This works only for very small values since numbers can grow exponentially.

#### 🔍 Algorithm

```pseudo
function bruteForce(sx, sy, tx, ty):
    if (sx, sy) == (tx, ty): return true
    if (sx > tx or sy > ty): return false
    return bruteForce(sx + sy, sy, tx, ty) OR bruteForce(sx, sx + sy, tx, ty)
```

#### 💻 Implementation

```cpp
// Brute force (DFS) - only works for small numbers

class Solution {
public:
    bool reachingPointsBrute(int sx, int sy, int tx, int ty) {
        // Base cases
        if (sx > tx || sy > ty) return false;
        if (sx == tx && sy == ty) return true;

        // Try both possible moves
        return reachingPointsBrute(sx + sy, sy, tx, ty) ||
               reachingPointsBrute(sx, sx + sy, tx, ty);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Backward Simulation with Subtraction)

#### 📝 Intuition

> - Instead of starting from (sx, sy) and growing, go backward from (tx, ty) to (sx, sy).
> - Since the operations are (x, x+y) or (x+y, y), backwards means:
>   - If tx > ty, then the last step must have been (tx - ty, ty).
>   - If ty > tx, then the last step must have been (tx, ty - tx).
> - Repeat until (tx, ty) becomes smaller than (sx, sy).
> - This avoids exploring all paths but can still be slow for large numbers (O(max(tx,ty)) steps).

#### 🔍 Algorithm

```pseudo
function optimized(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if (tx, ty) == (sx, sy): return true
        if tx > ty: tx -= ty
        else: ty -= tx
    return false
```

#### 💻 Implementation

```cpp
// Optimized solution using backward subtraction

class Solution {
public:
    bool reachingPointsOptimized(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy) {
            if (tx == sx && ty == sy) return true;

            if (tx > ty) {
                tx -= ty; // undo (x+y, y)
            } else {
                ty -= tx; // undo (x, x+y)
            }
        }
        return false;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Modulo Reduction)

#### 📝 Intuition

> - The subtraction process (approach 2) is basically repeated subtraction → can be optimized with modulo.
> - If tx > ty, then the last step must be (tx - k\*ty, ty) where k is the maximum possible.
> - So instead of tx -= ty repeatedly, we can do tx %= ty.
> - Similarly for ty > tx.
> - Stop when tx < sx or ty < sy.
> - Special case: when one coordinate matches exactly, check if the other difference is divisible.

#### 🔍 Algorithm

```pseudo
function optimal(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if (tx == sx and (ty - sy) % sx == 0) return true
        if (ty == sy and (tx - sx) % sy == 0) return true

        if tx > ty:
            tx %= ty
        else:
            ty %= tx
    return false
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution using modulo reduction

class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy) {
            // Case 1: X matches, Y must be reducible by multiples of X
            if (tx == sx && (ty - sy) % sx == 0) return true;
            // Case 2: Y matches, X must be reducible by multiples of Y
            if (ty == sy && (tx - sx) % sy == 0) return true;

            if (tx > ty) {
                tx %= ty; // Reduce faster instead of subtracting
            } else {
                ty %= tx;
            }
        }
        return false;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity          | Space Complexity | Pros                                | Cons                             |
| -------------- | ------------------------ | ---------------- | ----------------------------------- | -------------------------------- |
| 🥉 Brute Force | Exponential (O(2^steps)) | O(depth)         | Very intuitive, simple recursion    | Impossible for n up to 1e9       |
| 🥈 Optimized   | O(max(tx, ty))           | O(1)             | Works better by reversing steps     | Still slow for very large values |
| 🥇 Optimal ⭐  | O(log(max(tx, ty)))      | O(1)             | Elegant, fast, handles huge numbers | Slightly harder to reason about  |

---

<div align="center">

**🎯 Problem 780 Completed!**

_Happy Coding! 🚀_

</div>
