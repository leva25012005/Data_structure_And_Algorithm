<div align="center">

# 🧠 [3099. Harshad Number](https://leetcode.com/problems/harshad-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203099-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/harshad-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `83.3%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/harshad-number/)  |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>An integer divisible by the <strong>sum</strong> of its digits is said to be a <strong>Harshad</strong> number. You are given an integer <code>x</code>. Return <em>the sum of the digits</em> of <code>x</code> if <code>x</code> is a <strong>Harshad</strong> number; otherwise, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 18
<strong>Output:</strong> 9
<strong>Explanation:</strong> The sum of digits of <code>x</code> is <code>9</code>. <code>18</code> is divisible by <code>9</code>. So <code>18</code> is a Harshad number and the answer is <code>9</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 23
<strong>Output:</strong> -1
<strong>Explanation:</strong> The sum of digits of <code>x</code> is <code>5</code>. <code>23</code> is not divisible by <code>5</code>. So <code>23</code> is not a Harshad number and the answer is <code>-1</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= x &lt;= 100</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert x into a string.
> - Compute the sum of digits easily.
> - If x is divisible by that sum, return it; otherwise return -1.

#### 🔍 Algorithm

```pseudo
function bruteForce(x):
    s = string of x
    sumDigits = 0
    for ch in s:
        sumDigits += int(ch)
    if x % sumDigits == 0:
        return sumDigits
    else:
        return -1
```

#### 💻 Implementation

```cpp
// Brute force approach using string conversion

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        string s = to_string(x);  // Convert number to string
        int sum = 0;
        for (char c : s) {
            sum += (c - '0');    // Sum of digits
        }
        if (x % sum == 0) return sum; // Harshad condition
        return -1;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math Digit Extraction)

#### 📝 Intuition

> - Avoid converting to string.
> - Extract digits using % 10 and / 10.
> - Compute digit sum in O(d).

#### 🔍 Algorithm

```pseudo
function optimized(x):
    sumDigits = 0
    temp = x
    while temp > 0:
        sumDigits += temp % 10
        temp //= 10
    if x % sumDigits == 0:
        return sumDigits
    else:
        return -1
```

#### 💻 Implementation

```cpp
// Optimized approach using digit extraction

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0, temp = x;
        while (temp > 0) {
            sum += temp % 10; // Add last digit
            temp /= 10;       // Remove last digit
        }
        if (x % sum == 0) return sum;
        return -1;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (One-pass inline computation)

#### 📝 Intuition

> - Since x ≤ 100, at most 3 digits → very small.
> - We can compute digit sum in one compact pass, without extra storage.
> - This is the most elegant way: compute sum while checking divisibility at the end.

#### 🔍 Algorithm

```pseudo
function optimal(x):
    sumDigits = digit sum of x
    return sumDigits if x % sumDigits == 0 else -1
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        for (int temp = x; temp > 0; temp /= 10) {
            sum += temp % 10; // Add last digit directly
        }
        return (x % sum == 0) ? sum : -1;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                        | Cons                        |
| -------------- | --------------- | ---------------- | --------------------------- | --------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Easiest to implement        | Uses string conversion      |
| 🥈 Optimized   | O(d)            | O(1)             | Efficient, no string needed | Slightly longer code        |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Compact, clean, very fast   | None (best for constraints) |

- Here d = number of digits in x (≤ 3 since x ≤ 100).

---

<div align="center">

**🎯 Problem 3099 Completed!**

_Happy Coding! 🚀_

</div>
