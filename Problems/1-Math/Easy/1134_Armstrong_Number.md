<div align="center">

# 🧠 [1134. Armstrong Number](https://leetcode.com/problems/armstrong-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201134-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/armstrong-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `77.9%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/armstrong-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <code>true</code> <em>if and only if it is an <strong>Armstrong number</strong></em>.</p>

<p>The <code>k</code>-digit number <code>n</code> is an Armstrong number if and only if the <code>k<sup>th</sup></code> power of each digit sums to <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 153
<strong>Output:</strong> true
<strong>Explanation:</strong> 153 is a 3-digit number, and 153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 123
<strong>Output:</strong> false
<strong>Explanation:</strong> 123 is a 3-digit number, and 123 != 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>8</sup></code></li>
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

> - Convert the integer n into a string to get the number of digits k.
> - For each digit, raise it to the power of k and sum them up.
> - Compare the result with the original number.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    s = convert n to string
    k = length(s)
    sum = 0
    for each char in s:
        digit = int(char)
        sum += digit^k
    return sum == n
```

#### 💻 Implementation

```cpp
// Brute force solution using string conversion

class Solution {
public:
    bool isArmstrong(int n) {
        string s = to_string(n);        // Convert number to string
        int k = s.size();               // Number of digits
        long long sum = 0;

        for (char c : s) {
            int digit = c - '0';
            sum += pow(digit, k);       // Add digit^k
        }

        return sum == n;                // Armstrong check
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math-Based Digit Extraction)

#### 📝 Intuition

> - Avoid string conversion.
> - Extract digits by repeatedly dividing by 10.
> - Count the digits first to know k.
> - Then recompute the sum of digit^k.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    k = count digits in n
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit^k
        temp = temp // 10
    return sum == n
```

#### 💻 Implementation

```cpp
// Optimized math-based solution

class Solution {
public:
    bool isArmstrong(int n) {
        int k = 0, temp = n;
        // Step 1: Count digits
        while (temp > 0) {
            k++;
            temp /= 10;
        }

        // Step 2: Compute sum of digit^k
        long long sum = 0;
        temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += pow(digit, k);
            temp /= 10;
        }

        return sum == n;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Precompute Powers)

#### 📝 Intuition

> - Each digit is between 0..9.
> - Precompute digit^k values for all digit to avoid repeated pow() calls.
> - Then extract digits and sum quickly.
> - This reduces redundant computation and makes it faster for multiple queries.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    k = count digits in n
    precompute power[d] = d^k for d in [0..9]
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += power[digit]
        temp = temp // 10
    return sum == n
```

#### 💻 Implementation

```cpp
// Most optimal solution with precomputation

class Solution {
public:
    bool isArmstrong(int n) {
        int k = 0, temp = n;
        // Step 1: Count digits
        while (temp > 0) {
            k++;
            temp /= 10;
        }

        // Step 2: Precompute digit^k for all digits 0..9
        vector<int> power(10, 0);
        for (int d = 0; d <= 9; d++) {
            power[d] = pow(d, k);
        }

        // Step 3: Sum using precomputed powers
        long long sum = 0;
        temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            sum += power[digit];
            temp /= 10;
        }

        return sum == n;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                        |
| -------------- | --------------- | ---------------- | ----------------------------------- | --------------------------- |
| 🥉 Brute Force | O(d)            | O(1)             | Very simple, easy to write          | Uses string conversion      |
| 🥈 Optimized   | O(d)            | O(1)             | Pure math, no string overhead       | Recomputes `pow` for digits |
| 🥇 Optimal ⭐  | O(d)            | O(10)            | Precomputes digit powers, efficient | Slightly more code overhead |

---

<div align="center">

**🎯 Problem 1134 Completed!**

_Happy Coding! 🚀_

</div>
