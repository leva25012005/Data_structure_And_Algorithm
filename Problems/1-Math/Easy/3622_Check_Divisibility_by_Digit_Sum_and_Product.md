<div align="center">

# 🧠 [3622. Check Divisibility by Digit Sum and Product](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203622-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                    |
| **Acceptance Rate** | `64.1%`                                                                                        |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                             |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code>. Determine whether <code>n</code> is divisible by the <strong>sum </strong>of the following two values:</p>

<ul>
	<li>The <strong>digit sum</strong> of <code>n</code> (the sum of its digits).</li>
	<li>The <strong>digit product</strong> of <code>n</code> (the product of its digits).</li>
</ul>

<p>Return <code>true</code> if <code>n</code> is divisible by this sum; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 99
<strong>Output:</strong> true
<strong>Explanation:</strong> Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 23
<strong>Output:</strong> false
<strong>Explanation:</strong> Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
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

> - Convert the number into a string.
> - Compute digit sum by adding digits, and digit product by multiplying digits.
> - Check if n % (digit_sum + digit_product) == 0.
> - This is the most straightforward approach.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    s = to_string(n)
    sum = 0
    product = 1
    for ch in s:
        digit = int(ch)
        sum += digit
        product *= digit
    return (n % (sum + product) == 0)
```

#### 💻 Implementation

```cpp
/// Brute Force: Using string conversion

class Solution {
public:
    bool isDivisible(int n) {
        string s = to_string(n);
        int sum = 0, product = 1;

        // Compute digit sum and product
        for (char c : s) {
            int digit = c - '0';
            sum += digit;
            product *= digit;
        }

        int total = sum + product;
        return (n % total == 0);
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Instead of converting to a string, directly extract digits using % 10 and / 10.
> - Accumulate digit sum and digit product as we go.
> - Finally check divisibility.
> - This avoids string operations.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    sum = 0
    product = 1
    x = n
    while x > 0:
        digit = x % 10
        sum += digit
        product *= digit
        x = x / 10
    return (n % (sum + product) == 0)
```

#### 💻 Implementation

```cpp
// Optimized: Using math operations only

class Solution {
public:
    bool isDivisible(int n) {
        int sum = 0, product = 1;
        int x = n;

        // Extract digits using % and /
        while (x > 0) {
            int digit = x % 10;
            sum += digit;
            product *= digit;
            x /= 10;
        }

        int total = sum + product;
        return (n % total == 0);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Single-pass with early exit)

#### 📝 Intuition

> - Same as approach 2 but with a small optimization:
>   - If product becomes 0 (because one digit is 0), the final divisor = sum + 0 = sum.
>   - We can skip multiplying further digits since product will remain 0.
> - This gives a slight performance improvement.
> - Space remains O(1) and time O(d) (where d = number of digits).

#### 🔍 Algorithm

```pseudo
function optimal(n):
    sum = 0
    product = 1
    x = n
    while x > 0:
        digit = x % 10
        sum += digit
        if product != 0:
            product *= digit
        x = x / 10
    total = sum + product
    return (n % total == 0)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool isDivisible(int n) {
        int sum = 0, product = 1;
        int x = n;

        // Process digits one by one
        while (x > 0) {
            int digit = x % 10;
            sum += digit;
            if (product != 0) { // If product already zero, skip multiplication
                product *= digit;
            }
            x /= 10;
        }

        int total = sum + product;
        return (n % total == 0);
    }
};
```

## 📊 Comparison of Approaches

|                | Approach | Time Complexity | Space Complexity                    | Pros                | Cons |
| -------------- | -------- | --------------- | ----------------------------------- | ------------------- | ---- |
| 🥉 Brute Force | O(d)     | O(d)            | Very simple, uses string operations | Extra memory needed |
| 🥈 Optimized   | O(d)     | O(1)            | Efficient, pure math solution       | Still multiplies 0s |
| 🥇 Optimal ⭐  | O(d)     | O(1)            | Cleanest, handles zero early        | Slightly trickier   |

- Here d = number of digits in n (at most 6 since n ≤ 10^6).

---

<div align="center">

**🎯 Problem 3622 Completed!**

_Happy Coding! 🚀_

</div>
