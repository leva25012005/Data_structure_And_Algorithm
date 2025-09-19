<div align="center">

# 🧠 [Check for Power](https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703757`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `34.59%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1)                                                |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Zoho](https://img.shields.io/badge/-Zoho-orange?style=flat-square) ![SAP Labs](https://img.shields.io/badge/-SAP%20Labs-orange?style=flat-square)               |

## Description

<!-- description:start -->

<p>Given two positive integers <code>x</code> and <code>y</code>, determine if <code>y</code> is a power of <code>x</code>. If <code>y</code> is a power of <code>x</code>, return <code>true</code>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 8
<strong>Output:</strong> true
<strong>Explanation:</strong> 2<sup>3</sup> = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 1, y = 8
<strong>Output:</strong> false
<strong>Explanation:</strong> Any power of 1 is always 1, so it cannot equal 8.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= x &lt;= 10<sup>3</sup></code></li>
  <li><code>1 &lt;= y &lt;= 10<sup>8</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(log y)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>
<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-if-a-number-is-power-of-another-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Repeated Multiplication)

#### 📝 Intuition

> - Start with value = 1.
> - Keep multiplying by x until value ≥ y.
> - If value == y → return true, else false.
> - This directly simulates "is y a power of x".

#### 🔍 Algorithm

```pseudo
function bruteForce(x, y):
    if x == 1:
        return (y == 1)
    value = 1
    while value < y:
        value = value * x
    return (value == y)
```

#### 💻 Implementation

```cpp
// Brute force approach with repeated multiplication

class Solution {
public:
    bool isPowerOfX(int x, int y) {
        if (x == 1) return y == 1; // Edge case

        long long value = 1;
        while (value < y) {
            value *= x; // Keep multiplying by x
        }
        return value == y;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Division Check)

#### 📝 Intuition

> - Instead of multiplying up, divide y down by x.
> - If at the end we reach 1, then y is a power of x.
> - If at some step y % x != 0, then it’s not possible.
> - This is more efficient and avoids overflow.

#### 🔍 Algorithm

```pseudo
function divisionCheck(x, y):
    if x == 1:
        return (y == 1)
    while y % x == 0:
        y = y / x
    return y == 1
```

#### 💻 Implementation

```cpp
// Division-based approach

class Solution {
public:
    bool isPowerOfX(int x, int y) {
        if (x == 1) return y == 1; // Special case: powers of 1 are always 1
        while (y % x == 0) {
            y /= x; // Keep dividing y by x
        }
        return y == 1;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Logarithm)

#### 📝 Intuition

> If $y$ is a power of $x$, then:
>
> $$
> \log_x(y) = k \quad \text{for some integer } k
> $$
>
> We can compute:
>
> $$
> k = \frac{\log(y)}{\log(x)}
> $$
>
> If $k$ is an integer (within floating point tolerance), then return **true**.
>
> This is elegant but needs care with floating point errors.

#### 🔍 Algorithm

```pseudo
function logCheck(x, y):
    if x == 1:
        return (y == 1)
    k = log(y) / log(x)
    return abs(k - round(k)) < epsilon
```

#### 💻 Implementation

```cpp
// Optimal logarithmic approach

#include <cmath>

class Solution {
public:
    bool isPowerOfX(int x, int y) {
        if (x == 1) return y == 1; // Edge case

        double k = log(y) / log(x); // Compute log base x of y
        double rounded = round(k);  // Closest integer

        // Check if k is close enough to an integer
        return fabs(k - rounded) < 1e-10;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                       | Cons                             |
| -------------- | --------------- | ---------------- | -------------------------- | -------------------------------- |
| 🥉 Brute Force | O(logₓ y)       | O(1)             | Simple, easy to implement  | May overflow if `x^k` grows fast |
| 🥈 Division    | O(logₓ y)       | O(1)             | Efficient, avoids overflow | Requires integer division        |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant, fastest           | Floating-point precision issues  |

---

<div align="center">

**🎯 Problem 703757 Completed!**

_Happy Coding! 🚀_

</div>
