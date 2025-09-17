<div align="center">

# 🧠 [3492. Maximum Containers on a Ship](https://leetcode.com/problems/maximum-containers-on-a-ship/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203492-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/maximum-containers-on-a-ship/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                           |
| ------------------- | ------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                     |
| **Acceptance Rate** | `74.7%`                                                                         |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/maximum-containers-on-a-ship/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)              |

## Description

<!-- Decription:start -->

<p>You are given a positive integer <code>n</code> representing an <code>n x n</code> cargo deck on a ship. Each cell on the deck can hold one container with a weight of <strong>exactly</strong> <code>w</code>.</p>

<p>However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, <code>maxWeight</code>.</p>

<p>Return the <strong>maximum</strong> number of containers that can be loaded onto the ship.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2, w = 3, maxWeight = 15
<strong>Output:</strong> 4
<strong>Explanation:</strong> The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed <code>maxWeight</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, w = 5, maxWeight = 20
<strong>Output:</strong> 4
<strong>Explanation:</strong> The deck has 9 cells, and each container weighs 5. The maximum number of containers that can be loaded without exceeding <code>maxWeight</code> is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n &lt;= 1000</code></li>
    <li><code>1 &lt;= w &lt;= 1000</code></li>
    <li><code>1 &lt;= maxWeight &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `09-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `09-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - We have an n x n cargo deck → total capacity for n² containers.
> - Each container weighs w.
> - Start loading containers one by one until the total weight would exceed maxWeight.
> - Return how many containers got loaded.
> - This is straightforward but inefficient for large n because it simulates each container.

#### 🔍 Algorithm

```pseudo
function bruteForce(n, w, maxWeight):
    total = 0
    count = 0
    while count < n*n and total + w <= maxWeight:
        total += w
        count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute force simulation approach

class Solution {
public:
    int maxContainers(int n, int w, long long maxWeight) {
        int totalCells = n * n;
        long long total = 0;
        int count = 0;

        // Load containers one by one
        while (count < totalCells && total + w <= maxWeight) {
            total += w;
            count++;
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution - Mathematical Calculation (Floor Division)

#### 📝 Intuition

> - Instead of simulating, compute directly:
>   - Maximum possible containers = n².
>   - Maximum weight capacity allows at most maxWeight // w containers.
> - Answer = min(n², maxWeight // w).
> - This avoids looping and is much faster.

#### 🔍 Algorithm

```pseudo
function optimized(n, w, maxWeight):
    maxCells = n * n
    maxByWeight = maxWeight // w
    return min(maxCells, maxByWeight)
```

#### 💻 Implementation

```cpp
// Optimized formula-based approach

class Solution {
public:
    int maxContainers(int n, int w, long long maxWeight) {
        long long maxCells = 1LL * n * n;        // total deck cells
        long long maxByWeight = maxWeight / w;   // how many containers by weight limit
        return (int)min(maxCells, maxByWeight);  // minimum of the two
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Clean Formula)

#### 📝 Intuition

> - Approach 2 already gives the correct O(1) solution.
> - We can present it more elegantly:
>   - Answer = min(n², maxWeight / w).
> - This is the final, optimal solution with constant time and space complexity.

#### 🔍 Algorithm

```pseudo
function optimal(n, w, maxWeight):
    return min(n * n, maxWeight // w)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int maxContainers(int n, int w, long long maxWeight) {
        return (int)min(1LL * n * n, maxWeight / w);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                              |
| -------------- | --------------- | ---------------- | ------------------------------- | --------------------------------- |
| 🥉 Brute Force | O(n²)           | O(1)             | Very simple, intuitive          | Too slow if n = 1000 (up to 1e6)  |
| 🥈 Optimized   | O(1)            | O(1)             | Direct formula, very fast       | Slightly more code than necessary |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, most elegant solution | None                              |

---

<div align="center">

**🎯 Problem 3492 Completed!**

_Happy Coding! 🚀_

</div>
