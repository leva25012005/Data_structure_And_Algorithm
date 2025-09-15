<div align="center">

# 🧠 [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201281-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                             |
| **Acceptance Rate** | `86.6%`                                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                      |

## Description

<!-- description:start -->

Given an integer number <code>n</code>, return the difference between the product of its digits and the sum of its digits.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 234
<strong>Output:</strong> 15 
<b>Explanation:</b> 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4421
<strong>Output:</strong> 21
<b>Explanation: 
</b>Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Quora** 🔥 87.2%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert number n into a string.
> - Extract digits one by one.
> - Compute the product of digits and sum of digits separately.
> - Return product - sum.
> - Simple, but uses string operations.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    s = to_string(n)
    product = 1
    sum = 0
    for each char c in s:
        digit = c - '0'
        product *= digit
        sum += digit
    return product - sum
```

#### 💻 Implementation

```cpp
// Brute force solution using string conversion

class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int product = 1, sum = 0;
        for (char c : s) {
            int digit = c - '0';
            product *= digit;  // Multiply for product
            sum += digit;      // Add for sum
        }
        return product - sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Instead of converting to string, extract digits directly using % 10 and / 10.
> - Update product and sum as we go.
> - Return product - sum.
> - This avoids string operations and works in pure math.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    product = 1
    sum = 0
    while n > 0:
        digit = n % 10
        product *= digit
        sum += digit
        n //= 10
    return product - sum
```

#### 💻 Implementation

```cpp
/// Optimized approach using digit extraction

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0;
        while (n > 0) {
            int digit = n % 10;   // Get last digit
            product *= digit;     // Multiply into product
            sum += digit;         // Add into sum
            n /= 10;              // Remove last digit
        }
        return product - sum;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - This problem is already very small in complexity (O(d) with d ≤ 6 because n ≤ 10^5).
> - The optimal way is just a clean one-pass calculation without extra storage.
> - Same as Approach 2, but written more compactly and elegantly.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    result = 1
    sum = 0
    while n > 0:
        d = n % 10
        result *= d
        sum += d
        n //= 10
    return result - sum
```

#### 💻 Implementation

```cpp
// Most optimal and elegant approach

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0;
        // One-pass calculation
        for (; n > 0; n /= 10) {
            int d = n % 10;
            product *= d;
            sum += d;
        }
        return product - sum;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                           | Cons                   |
| -------------- | --------------- | ---------------- | ------------------------------ | ---------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, easy to implement | Extra string overhead  |
| 🥈 Optimized   | O(d)            | O(1)             | Pure math, avoids strings      | Slightly more verbose  |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Clean, compact, efficient      | None (already optimal) |

- Here d = number of digits (at most 6 since n ≤ 100000).

---

<div align="center">

**🎯 Problem 1281 Completed!**

_Happy Coding! 🚀_

</div>
