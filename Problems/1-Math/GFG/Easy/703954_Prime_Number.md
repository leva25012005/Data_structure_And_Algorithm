<div align="center">

# 🧠 [Prime Number](https://www.geeksforgeeks.org/problems/prime-number2314/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/prime-number2314/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `703954`                                                                                                                                                                                                                                               |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                            |
| **Accuracy**     | `22.2%`                                                                                                                                                                                                                                                |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/prime-number2314/1)                                                                                                                                                                     |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Prime Number](https://img.shields.io/badge/-Prime%20Number-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![VMWare](https://img.shields.io/badge/-VMWare-orange?style=flat-square) ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![SAP Labs](https://img.shields.io/badge/-SAP%20Labs-orange?style=flat-square)                       |

## Description

<!-- description:start -->

<p>Given a number <code>n</code>, determine whether it is a <strong>prime number</strong>.</p>

<blockquote>
<p>A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.</p>
</blockquote>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> true
<strong>Explanation:</strong> 7 has exactly two divisors: 1 and 7, making it a prime number.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> false
<strong>Explanation:</strong> 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> false
<strong>Explanation:</strong> 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(sqrt(n))<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-for-prime-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check All Divisors)

#### 📝 Intuition

> - A number n is prime if it has exactly two positive divisors: 1 and itself.
> - The simplest way is to check every number from 2 to n-1.
> - If any number divides n, it is not prime

#### 🔍 Algorithm

```pseudo
function isPrime(n):
    if n <= 1: return false
    for i from 2 to n-1:
        if n % i == 0: return false
    return true
```

#### 💻 Implementation

```cpp
// Brute force: check all divisors
class Solution {
public:
    bool isPrimeBruteForce(int n) {
        if (n <= 1) return false; // 1 is not prime
        for (int i = 2; i < n; i++) { // check all numbers from 2 to n-1
            if (n % i == 0) return false; // divisible => not prime
        }
        return true; // no divisors found
    }
};
```

### 🥈 Approach 2: Optimized Solution (Check up to n/2)

#### 📝 Intuition

> - A number cannot have a divisor greater than n/2 except itself.
> - So, we only need to check divisors from 2 to n/2.

#### 🔍 Algorithm

```pseudo
function isPrime(n):
    if n <= 1: return false
    for i from 2 to n/2:
        if n % i == 0: return false
    return true
```

#### 💻 Implementation

```cpp
// Optimized: check up to n/2
class Solution {
public:
    bool isPrimeOptimized(int n) {
        if (n <= 1) return false; // 1 is not prime
        for (int i = 2; i <= n / 2; i++) { // check up to n/2
            if (n % i == 0) return false;
        }
        return true; // no divisors found
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Check up to sqrt(n))

#### 📝 Intuition

> - A larger factor of n must be paired with a smaller factor.
> - So it is sufficient to check divisors up to sqrt(n).
> - This reduces time complexity from O(n) or O(n/2) to O(√n).

#### 🔍 Algorithm

```pseudo
function isPrime(n):
    if n <= 1: return false
    for i from 2 to sqrt(n):
        if n % i == 0: return false
    return true
```

#### 💻 Implementation

```cpp
// Most optimal: check divisors up to sqrt(n)
class Solution {
public:
    bool isPrimeOptimal(int n) {
        if (n <= 1) return false; // 1 is not prime
        for (int i = 2; i * i <= n; i++) { // check up to sqrt(n)
            if (n % i == 0) return false; // divisible => not prime
        }
        return true; // no divisors found
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                    |
| -------------- | --------------- | ---------------- | ----------------------------------- | ----------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very simple, easy to understand     | Too slow for large n    |
| 🥈 Optimized   | O(n/2)          | O(1)             | Slightly faster than brute force    | Still slow for n \~ 1e9 |
| 🥇 Optimal ⭐  | O(√n)           | O(1)             | Fast, expected solution for large n | None significant        |

---

<div align="center">

**🎯 Problem 703954 Completed!**

_Happy Coding! 🚀_

</div>
