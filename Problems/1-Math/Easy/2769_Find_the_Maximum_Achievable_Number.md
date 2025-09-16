<div align="center">

# 🧠 [2769. Find the Maximum Achievable Number](https://leetcode.com/problems/find-the-maximum-achievable-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202769-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-the-maximum-achievable-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                           |
| **Acceptance Rate** | `91.0%`                                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-the-maximum-achievable-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                    |

## Description

<!-- description:start -->

<p>Given two integers, <code>num</code> and <code>t</code>. A <strong>number </strong><code>x</code><strong> </strong>is <strong>achievable</strong> if it can become equal to <code>num</code> after applying the following operation <strong>at most</strong> <code>t</code> times:</p>

<ul>
    <li>Increase or decrease <code>x</code> by <code>1</code>, and <em>simultaneously</em> increase or decrease <code>num</code> by <code>1</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> possible value of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 4, t = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> Apply the following operation once to make the maximum achievable number equal to <code>num</code>:
- Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 3, t = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Apply the following operation twice to make the maximum achievable number equal to <code>num</code>:
- Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= num, t &lt;= 50</code></li>
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

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Start with x = num.
> - At each operation, we can increase x by 1 while decreasing num by 1, or decrease x by 1 while increasing num by 1.
> - To maximize x, always pick the operation that increases x.
> - Simulate up to t steps.

#### 🔍 Algorithm

```pseudo
function bruteForce(num, t):
    x = num
    repeat t times:
        x = x + 1
        num = num + 1
    return x
```

#### 💻 Implementation

```cpp
/// Brute force with simulation

class Solution {
public:
    int solutionBruteForce(int num, int t) {
        int x = num;
        // Simulate t operations
        for (int i = 0; i < t; i++) {
            x += 1;   // increase x
            num += 1; // increase num
        }
        return x;
    }
};
```

### 🥇 Approach 2: Optimal Solution ⭐ (One-Liner)

#### 📝 Intuition

> - The problem reduces directly to the formula: x = num + 2 × t.
> - No loops, no extra variables, constant time.

#### 🔍 Algorithm

```pseudo
function optimal(num, t):
    return num + 2 * t
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int solutionOptimal(int num, int t) {
        return num + 2 * t;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                          |
| -------------- | --------------- | ---------------- | ----------------------------- | ----------------------------- |
| 🥉 Brute Force | O(t)            | O(1)             | Intuitive, simulates directly | Too slow if t were very large |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, one-liner solution  | None                          |

---

<div align="center">

**🎯 Problem 2769 Completed!**

_Happy Coding! 🚀_

</div>
