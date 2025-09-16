<div align="center">

# 🧠 [3516. Find Closest Person](https://leetcode.com/problems/find-closest-person/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203516-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-closest-person/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                            |
| **Acceptance Rate** | `83.3%`                                                                |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-closest-person/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)     |

## Description

<!-- description:start -->

<p>You are given three integers <code>x</code>, <code>y</code>, and <code>z</code>, representing the positions of three people on a number line:</p>

<ul>
    <li><code>x</code> is the position of Person 1.</li>
    <li><code>y</code> is the position of Person 2.</li>
    <li><code>z</code> is the position of Person 3, who does <strong>not</strong> move.</li>
</ul>

<p>Both Person 1 and Person 2 move toward Person 3 at the <strong>same</strong> speed.</p>

<p>Determine which person reaches Person 3 <strong>first</strong>:</p>

<ul>
    <li>Return 1 if Person 1 arrives first.</li>
    <li>Return 2 if Person 2 arrives first.</li>
    <li>Return 0 if both arrive at the <strong>same</strong> time.</li>
</ul>

<p>Return the result accordingly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 7, z = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
- Person 2 is at position 7 and can reach Person 3 in 3 steps.
Since Person 1 reaches Person 3 first, the output is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 5, z = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
- Person 2 is at position 5 and can reach Person 3 in 1 step.
Since Person 2 reaches Person 3 first, the output is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 1, y = 5, z = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
- Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
- Person 2 is at position 5 and can reach Person 3 in 2 steps.
Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= x, y, z &lt;= 100</code></li>
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

**🎯 Problem 3516 Completed!**

_Happy Coding! 🚀_

</div>
