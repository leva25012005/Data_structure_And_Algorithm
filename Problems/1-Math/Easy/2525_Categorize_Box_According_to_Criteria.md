<div align="center">

# 🧠 [2525. Categorize Box According to Criteria](https://leetcode.com/problems/categorize-box-according-to-criteria/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202525-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/categorize-box-according-to-criteria/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                             |
| **Acceptance Rate** | `37.9%`                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/categorize-box-according-to-criteria/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                      |

## Description

<!-- description:start -->

<p>Given four integers <code>length</code>, <code>width</code>, <code>height</code>, and <code>mass</code>, representing the dimensions and mass of a box, respectively, return <em>a string representing the <strong>category</strong> of the box</em>.</p>

<ul>
	<li>The box is <code>&quot;Bulky&quot;</code> if:

  <li><strong>Bulky</strong> if <strong>any</strong> of the following conditions hold:
    <ul>
      <li>Any of the dimensions of the box is greater or equal to <code>10<sup>4</sup></code>.</li>
      <li>Or, the <strong>volume</strong> of the box is greater or equal to <code>10<sup>9</sup></code>.</li>
    </ul>
  </li>
  <li>If the mass of the box is greater or equal to <code>100</code>, it is <code>"Heavy"</code>.</li>
  <li>If the box is both <code>"Bulky"</code> and <code>"Heavy"</code>, then its category is <code>"Both"</code>.</li>
  <li>If the box is neither <code>"Bulky"</code> nor <code>"Heavy"</code>, then its category is <code>"Neither"</code>.</li>
  <li>If the box is <code>"Bulky"</code> but not <code>"Heavy"</code>, then its category is <code>"Bulky"</code>.</li>
  <li>If the box is <code>"Heavy"</code> but not <code>"Bulky"</code>, then its category is <code>"Heavy"</code>.</li>
</ul>

</ul>

<p><strong>Note</strong> that the volume of the box is the product of its length, width and height.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> length = 1000, width = 35, height = 700, mass = 300
<strong>Output:</strong> &quot;Heavy&quot;
<strong>Explanation:</strong> 
None of the dimensions of the box is greater or equal to 10<sup>4</sup>. 
Its volume = 24500000 &lt;= 10<sup>9</sup>. So it cannot be categorized as &quot;Bulky&quot;.
However mass &gt;= 100, so the box is &quot;Heavy&quot;.
Since the box is not &quot;Bulky&quot; but &quot;Heavy&quot;, we return &quot;Heavy&quot;.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> length = 200, width = 50, height = 800, mass = 50
<strong>Output:</strong> &quot;Neither&quot;
<strong>Explanation:</strong> 
None of the dimensions of the box is greater or equal to 10<sup>4</sup>.
Its volume = 8 * 10<sup>6</sup> &lt;= 10<sup>9</sup>. So it cannot be categorized as &quot;Bulky&quot;.
Its mass is also less than 100, so it cannot be categorized as &quot;Heavy&quot; either. 
Since its neither of the two above categories, we return &quot;Neither&quot;.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= length, width, height &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= mass &lt;= 10<sup>3</sup></code></li>
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

| Problem                                                                                               | Difficulty  | Relationship    |
| ----------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)                                                 | 🟢 **Easy** | Similar logic   |
| [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | 🟢 **Easy** | Related concept |
| [Best Poker Hand](https://leetcode.com/problems/best-poker-hand/)                                     | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Zendesk** 🔥 100.0%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

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

**🎯 Problem 2525 Completed!**

_Happy Coding! 🚀_

</div>
