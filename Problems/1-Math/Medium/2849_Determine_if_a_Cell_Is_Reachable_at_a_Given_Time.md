<div align="center">

# 🧠 [2849. Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202849-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                                       |
| **Acceptance Rate** | `37.1%`                                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                  |

## Description

<!-- description:start -->

<p>You are given four integers <code>sx</code>, <code>sy</code>, <code>fx</code>, <code>fy</code>, and a <strong>non-negative</strong> integer <code>t</code>.</p>

<p>In an infinite 2D grid, you start at the cell <code>(sx, sy)</code>. Each second, you <strong>must</strong> move to any of its adjacent cells.</p>

<p>Return <code>true</code> <em>if you can reach cell </em><code>(fx, fy)</code> <em>after<strong> exactly</strong></em> <code>t</code> <strong><em>seconds</em></strong>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>A cell&#39;s <strong>adjacent cells</strong> are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2849.Determine%20if%20a%20Cell%20Is%20Reachable%20at%20a%20Given%20Time/images/example2.svg" style="width: 443px; height: 243px;" />
<pre>
<strong>Input:</strong> sx = 2, sy = 4, fx = 7, fy = 7, t = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2849.Determine%20if%20a%20Cell%20Is%20Reachable%20at%20a%20Given%20Time/images/example1.svg" style="width: 383px; height: 202px;" />
<pre>
<strong>Input:</strong> sx = 3, sy = 1, fx = 7, fy = 3, t = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sx, sy, fx, fy &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= t &lt;= 10<sup>9</sup></code></li>
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

## 🔗 Related Problems

| Problem                                                           | Difficulty  | Relationship  |
| ----------------------------------------------------------------- | ----------- | ------------- |
| [Reaching Points](https://leetcode.com/problems/reaching-points/) | 🔴 **Hard** | Similar logic |

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

**🎯 Problem 2849 Completed!**

_Happy Coding! 🚀_

</div>
