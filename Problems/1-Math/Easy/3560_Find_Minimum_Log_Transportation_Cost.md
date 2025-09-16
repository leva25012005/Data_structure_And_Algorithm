<div align="center">

# 🧠 [3560. Find Minimum Log Transportation Cost](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203560-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                             |
| **Acceptance Rate** | `41.5%`                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-minimum-log-transportation-cost/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                      |

## Description

<!-- description:start -->

<p>You are given integers <code>n</code>, <code>m</code>, and <code>k</code>.</p>

<p>There are two logs of lengths <code>n</code> and <code>m</code> units, which need to be transported in three trucks where each truck can carry one log with length <strong>at most</strong> <code>k</code> units.</p>

<p>You may cut the logs into smaller pieces, where the cost of cutting a log of length <code>x</code> into logs of length <code>len1</code> and <code>len2</code> is <code>cost = len1 * len2</code> such that <code>len1 + len2 = x</code>.</p>

<p>Return the <strong>minimum total cost</strong> to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6, m = 5, k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 = 5. 
Now the three logs of length 1, 5, and 5 can fit in one truck each.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, m = 4, k = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> The two logs can fit in the trucks already, hence we don't need to cut the logs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>2 &lt;= k &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= n, m &lt;= 2 * k</code></li>
    <li>The input is generated such that it is always possible to transport the logs.</li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `DD-MM-YYYY` | First attempt, understanding the problem |
| ✅ **Solved**    | `DD-MM-YYYY` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> Mô tả ý tưởng đơn giản nhất để giải quyết bài toán

#### 🔍 Algorithm

```pseudo
// Write your pseudocode here
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int solutionBruteForce(vector<int>& nums) {
        // Implementation here
        return 0;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Mô tả cách tối ưu hóa từ approach đầu tiên

#### 🔍 Algorithm

```pseudo
// Write your pseudocode here
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity

class Solution {
public:
    int solutionOptimized(vector<int>& nums) {
        // Optimized implementation here
        return 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Mô tả giải pháp tốt nhất, elegant nhất

#### 🔍 Algorithm

```pseudo
// Write your pseudocode here
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int solutionOptimal(vector<int>& nums) {
        // Optimal implementation here
        return 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros | Cons |
| -------------- | --------------- | ---------------- | ---- | ---- |
| 🥉 Brute Force | O(?)            | O(?)             | ...  | ...  |
| 🥈 Optimized   | O(?)            | O(?)             | ...  | ...  |
| 🥇 Optimal ⭐  | O(?)            | O(?)             | ...  | ...  |
| ...            | ....            | ...              | ...  | ...  |

---

<div align="center">

**🎯 Problem 3560 Completed!**

_Happy Coding! 🚀_

</div>
