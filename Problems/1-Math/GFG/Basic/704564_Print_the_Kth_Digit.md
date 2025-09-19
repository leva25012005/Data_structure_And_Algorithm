<div align="center">

# 🧠 [Print the Kth Digit](https://www.geeksforgeeks.org/problems/print-the-kth-digit3520/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/print-the-kth-digit3520/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704564`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `38.65%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/print-the-kth-digit3520/1)                                                                         |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Flipkart](https://img.shields.io/badge/-Flipkart-orange?style=flat-square)                                                                                      |

## Description

<!-- description:start -->

<p>Given two numbers <code>a</code> and <code>b</code>, find the <code>k<sup>th</sup></code> digit from the right of <code>a<sup>b</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 3, b = 3, k = 1
<strong>Output:</strong> 7
<strong>Explanation:</strong> 3^3 = 27 and the 1st digit from the right is 7
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 5, b = 2, k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5^2 = 25 and the 2nd digit from the right is 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= a, b &lt;= 15</code></li>
  <li><code>1 &lt;= k &lt;= digits_in(a^b)</code></li>
</ul>

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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/k-th-digit-raised-power-b/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Compute a^b directly.
> - Convert it to a string or array of digits.
> - Pick the kth digit from the right.
> - This works because constraints are small (a, b ≤ 15).

#### 🔍 Algorithm

```pseudo
function bruteForce(a, b, k):
    val = a^b
    convert val to string
    return digit at position len(val)-k
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    int kthDigitBruteForce(int a, int b, int k) {
        long long val = 1;
        // Compute a^b
        for (int i = 0; i < b; i++) val *= a;

        string s = to_string(val);         // Convert to string
        int n = s.size();
        return s[n - k] - '0';             // kth digit from right
    }
};
```

### 🥈 Approach 2: Optimized Solution Using Modular Arithmetic (Optimized)

#### 📝 Intuition

> - We only need the last k digits, not the full number.
> - Compute a^b mod 10^k to get the last k digits.
> - Then extract the last digit (or kth from right).
> - This avoids unnecessary large numbers.

#### 🔍 Algorithm

```pseudo
function optimized(a, b, k):
    mod = 10^k
    val = (a^b) % mod
    return kth digit from right of val
```

#### 💻 Implementation

```cpp
// Optimized approach using modular arithmetic

class Solution {
public:
    int kthDigitOptimized(int a, int b, int k) {
        int mod = 1;
        for (int i = 0; i < k; i++) mod *= 10;

        long long val = 1;
        for (int i = 0; i < b; i++) val = (val * a) % mod;

        string s = to_string(val);
        int n = s.size();
        return s[n - k] - '0';
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Computation with String)

#### 📝 Intuition

> - Compute a^b directly (small numbers, safe).
> - Convert to string and index directly from the right.
> - This is clean and avoids modulo computations if numbers are small (a^b ≤ 15^15).

#### 🔍 Algorithm

```pseudo
function optimal(a, b, k):
    val = a^b
    convert val to string
    return s[length - k]
```

#### 💻 Implementation

```cpp
// Elegant approach using string conversion

class Solution {
public:
    int kthDigitOptimal(int a, int b, int k) {
        long long val = 1;
        for (int i = 0; i < b; i++) val *= a;

        string s = to_string(val);
        return s[s.size() - k] - '0';
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                        | Cons                         |
| -------------- | --------------- | ---------------- | --------------------------- | ---------------------------- |
| 🥉 Brute Force | O(b)            | O(d)             | Simple, easy to implement   | Large numbers for bigger a,b |
| 🥈 Optimized   | O(b)            | O(k)             | Only computes needed digits | Slightly more complex        |
| 🥇 Optimal ⭐  | O(b)            | O(d)             | Elegant, readable code      | Only works for small numbers |

---

<div align="center">

**🎯 Problem 704564 Completed!**

_Happy Coding! 🚀_

</div>
