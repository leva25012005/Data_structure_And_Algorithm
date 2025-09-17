<div align="center">

# 🧠 [263. Ugly Number](https://leetcode.com/problems/ugly-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20263-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/ugly-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `42.5%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/ugly-number/)     |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>An <strong>ugly number</strong> is a <em>positive</em> integer which does not have a prime factor other than 2, 3, and 5.</p>

<p>Given an integer <code>n</code>, return <code>true</code> <em>if</em> <code>n</code> <em>is an <strong>ugly number</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> 6 = 2 &times; 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 has no prime factors.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> 14 is not ugly since it includes the prime factor 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
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

## 🔗 Related Problems

| Problem                                                         | Difficulty    | Relationship    |
| --------------------------------------------------------------- | ------------- | --------------- |
| [Happy Number](https://leetcode.com/problems/happy-number/)     | 🟢 **Easy**   | Similar logic   |
| [Count Primes](https://leetcode.com/problems/count-primes/)     | 🟡 **Medium** | Related concept |
| [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

### 📊 Low Frequency Companies

- **J.P. Morgan** 📊 36.3%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Prime Factorization Check)

#### 📝 Intuition

> - To check if n is an ugly number, we can factorize n and verify whether all prime factors are only from {2, 3, 5}.
> - - This means dividing by all primes ≤ sqrt(n) and checking if any other prime factor appears.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    if n <= 0: return false
    factors = primeFactorization(n)
    for f in factors:
        if f not in {2, 3, 5}: return false
    return true
```

#### 💻 Implementation

```cpp
// Brute force factorization approach

class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false; // Ugly numbers must be positive
        // Divide n by all primes starting from 2
        for (int i = 2; i <= sqrt(n); i++) {
            while (n % i == 0) {
                if (i != 2 && i != 3 && i != 5) return false;
                n /= i;
            }
        }
        // If there's a remaining prime factor > 5, it's not ugly
        return (n == 1 || n == 2 || n == 3 || n == 5);
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Instead of full prime factorization, we only care about factors 2, 3, and 5.
> - Repeatedly divide n by 2, 3, and 5 as long as possible.
> - If the final result = 1 → it’s an ugly number. Otherwise → not ugly.
> - This is simpler and much faster.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    if n <= 0: return false
    while n divisible by 2: n /= 2
    while n divisible by 3: n /= 3
    while n divisible by 5: n /= 5
    return n == 1
```

#### 💻 Implementation

```cpp
// Optimized divide-by-2-3-5 approach

class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        // Keep dividing by 2, 3, 5
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        // If reduced to 1, it's ugly
        return n == 1;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Use a loop to try dividing n by [2, 3, 5] factors directly.
>
> - This avoids writing 3 separate loops.
> - This makes the code short and elegant.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    if n <= 0: return false
    for factor in [2,3,5]:
        while n divisible by factor:
            n /= factor
    return n == 1
```

#### 💻 Implementation

```cpp
// Most elegant solution with factor loop

class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        // Try dividing by only allowed factors
        for (int factor : {2, 3, 5}) {
            while (n % factor == 0) {
                n /= factor;
            }
        }
        return n == 1;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                   | Cons                      |
| -------------- | --------------- | ---------------- | -------------------------------------- | ------------------------- |
| 🥉 Brute Force | O(√n)           | O(1)             | Uses generic prime factorization logic | Overkill for this problem |
| 🥈 Optimized   | O(log n)        | O(1)             | Simple & efficient, easy to understand | Slightly repetitive code  |
| 🥇 Optimal ⭐  | O(log n)        | O(1)             | Clean, elegant, minimal code           | Same logic as approach 2  |

---

<div align="center">

**🎯 Problem 263 Completed!**

_Happy Coding! 🚀_

</div>
