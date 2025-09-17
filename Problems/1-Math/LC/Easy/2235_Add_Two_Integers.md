<div align="center">

# 🧠 [2235. Add Two Integers](https://leetcode.com/problems/add-two-integers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202235-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/add-two-integers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `88.0%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/add-two-integers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

Given two integers <code>num1</code> and <code>num2</code>, return <em>the <strong>sum</strong> of the two integers</em>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 12, num2 = 5
<strong>Output:</strong> 17
<strong>Explanation:</strong> num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = -10, num2 = 4
<strong>Output:</strong> -6
<strong>Explanation:</strong> num1 + num2 = -6, so -6 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100 &lt;= num1, num2 &lt;= 100</code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Jane Street** ⭐ 76.5%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

### 📊 Low Frequency Companies

- **Atlassian** 📊 30.0%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Direct Addition)

#### 📝 Intuition

> - Just return num1 + num2.
> - This is the most straightforward approach since the problem directly asks for the sum

#### 🔍 Algorithm

```pseudo
function bruteForce(num1, num2):
    return num1 + num2
```

#### 💻 Implementation

```cpp
/// Brute force approach with direct addition

class Solution {
public:
    int solutionBruteForce(int num1, int num2) {
        return num1 + num2; // Simply add and return
    }
};
```

### 🥇 Approach 2: Optimal Solution ⭐ (Bitwise Addition)

#### 📝 Intuition

> - se bit manipulation to perform addition without using the + operator:
>   - Use XOR (^) to add numbers without carry.
>   - Use AND (&) and left shift to calculate the carry.
>   - Repeat until carry becomes 0.
> - This is how addition is done at the hardware level.

#### 🔍 Algorithm

```pseudo
function bitwiseAddition(num1, num2):
    while num2 != 0:
        carry = (num1 & num2) << 1
        num1 = num1 ^ num2
        num2 = carry
    return num1
```

#### 💻 Implementation

```cpp
// Optimal approach using bitwise operations (no + operator)

class Solution {
public:
    int solutionBitwise(int num1, int num2) {
        while (num2 != 0) {
            int carry = (num1 & num2) << 1; // Calculate carry
            num1 = num1 ^ num2;             // Sum without carry
            num2 = carry;                   // Assign carry to num2
        }
        return num1;
    }
};
```

## 📊 Comparison of Approaches

| Approach              | Time Complexity | Space Complexity | Pros                                  | Cons                        |     |     |
| --------------------- | --------------- | ---------------- | ------------------------------------- | --------------------------- | --- | --- |
| 🥉 Direct Addition    | O(1)            | O(1)             | Clean, simplest, one line             | Too trivial, no learning    |     |     |
| 🥇 Bitwise Optimal ⭐ | O(log(max))     | O(1)             | Shows how addition works at low level | More complex than necessary |     |     |

---

<div align="center">

**🎯 Problem 2235 Completed!**

_Happy Coding! 🚀_

</div>
