<div align="center">

# 🧠 [1276. Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201276-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                                     |
| **Acceptance Rate** | `50.5%`                                                                                           |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                |

## Description

<!-- description:start -->

<p>Given two integers <code>tomatoSlices</code> and <code>cheeseSlices</code>. The ingredients of different burgers are as follows:</p>

<ul>
	<li><strong>Jumbo Burger:</strong> <code>4</code> tomato slices and <code>1</code> cheese slice.</li>
	<li><strong>Small Burger:</strong> <code>2</code> Tomato slices and <code>1</code> cheese slice.</li>
</ul>

<p>Return <code>[total_jumbo, total_small]</code> so that the number of remaining <code>tomatoSlices</code> equal to <code>0</code> and the number of remaining <code>cheeseSlices</code> equal to <code>0</code>. If it is not possible to make the remaining <code>tomatoSlices</code> and <code>cheeseSlices</code> equal to <code>0</code> return <code>[]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 16, cheeseSlices = 7
<strong>Output:</strong> [1,6]
<strong>Explantion:</strong> To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
There will be no remaining ingredients.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 17, cheeseSlices = 4
<strong>Output:</strong> []
<strong>Explantion:</strong> There will be no way to use all ingredients to make small and jumbo burgers.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 4, cheeseSlices = 17
<strong>Output:</strong> []
<strong>Explantion:</strong> Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= tomatoSlices, cheeseSlices &lt;= 10<sup>7</sup></code></li>
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

**🎯 Problem 1276 Completed!**

_Happy Coding! 🚀_

</div>
