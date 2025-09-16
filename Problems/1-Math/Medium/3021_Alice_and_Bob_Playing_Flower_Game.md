<div align="center">

# 🧠 [3021. Alice and Bob Playing Flower Game](https://leetcode.com/problems/alice-and-bob-playing-flower-game/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203021-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/alice-and-bob-playing-flower-game/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Difficulty**      | 🟡 **Medium**                                                                        |
| **Acceptance Rate** | `46.1%`                                                                              |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/alice-and-bob-playing-flower-game/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                   |

## Description

<!-- description:start -->

<p>Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are <code>x</code> flowers in the first lane between Alice and Bob, and <code>y</code> flowers in the second lane between them.</p>

<p><img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/3000-3099/3021.Alice%20and%20Bob%20Playing%20Flower%20Game/images/3021.png" style="width: 300px; height: 150px;" /></p>

<p>The game proceeds as follows:</p>

<ol>
	<li>Alice takes the first turn.</li>
	<li>In each turn, a player must choose either one of the lane&nbsp;and pick one flower from that side.</li>
	<li>At the end of the turn, if there are no flowers left at all in either lane, the <strong>current</strong> player captures their opponent and wins the game.</li>
</ol>

<p>Given two integers, <code>n</code> and <code>m</code>, the task is to compute the number of possible pairs <code>(x, y)</code> that satisfy the conditions:</p>

<ul>
	<li>Alice must win the game according to the described rules.</li>
	<li>The number of flowers <code>x</code> in the first lane must be in the range <code>[1,n]</code>.</li>
	<li>The number of flowers <code>y</code> in the second lane must be in the range <code>[1,m]</code>.</li>
</ul>

<p>Return <em>the number of possible pairs</em> <code>(x, y)</code> <em>that satisfy the conditions mentioned in the statement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, m = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> No pairs satisfy the conditions described in the statement.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Rubrik** ⭐ 62.6%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

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

**🎯 Problem 3021 Completed!**

_Happy Coding! 🚀_

</div>
