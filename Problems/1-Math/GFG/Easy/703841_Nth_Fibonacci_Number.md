<div align="center">

# 🧠 [Nth Fibonacci Number](https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703841`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Accuracy**     | `22.3%`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Topic Tags**   | ![Dynamic Programming](https://img.shields.io/badge/-Dynamic%20Programming-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Fibonacci](https://img.shields.io/badge/-Fibonacci-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                                                                                                                                                                                                                                                                             |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![OYO Rooms](https://img.shields.io/badge/-OYO%20Rooms-orange?style=flat-square) ![Snapdeal](https://img.shields.io/badge/-Snapdeal-orange?style=flat-square) ![MakeMyTrip](https://img.shields.io/badge/-MakeMyTrip-orange?style=flat-square) ![Goldman Sachs](https://img.shields.io/badge/-Goldman%20Sachs-orange?style=flat-square) ![MAQ Software](https://img.shields.io/badge/-MAQ%20Software-orange?style=flat-square) ![Adobe](https://img.shields.io/badge/-Adobe-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a non-negative integer <code>n</code>, find the <strong>nth Fibonacci number</strong>.</p>

<p>The <a href="https://www.geeksforgeeks.org/fibonacci-series/" target="_blank" rel="noopener">Fibonacci sequence</a> is defined as follows:</p>

<ul>
  <li>F(0) = 0</li>
  <li>F(1) = 1</li>
  <li>F(n) = F(n - 1) + F(n - 2) for n > 1</li>
</ul>

<p>For example, the sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> The 5th Fibonacci number is 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> The 0th Fibonacci number is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The 1st Fibonacci number is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>0 &lt;= n &lt;= 30</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/cpp-program-for-fibonacci-numbers/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursive)

#### 📝 Intuition

> - Directly follow the definition of Fibonacci: F(n) = F(n-1) + F(n-2).
> - Simple recursion mirrors the mathematical definition.
> - Extremely slow for large n due to repeated calculations (O(2^n))

#### 🔍 Algorithm

```pseudo
function fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
```

#### 💻 Implementation

```cpp
// Brute force recursive approach

class Solution {
public:
    int fibBruteForce(int n) {
        if (n == 0) return 0; // Base case F(0)
        if (n == 1) return 1; // Base case F(1)
        return fibBruteForce(n - 1) + fibBruteForce(n - 2); // Recursive call
    }
};
```

### 🥈 Approach 2: Optimized Solution (Iterative / DP)

#### 📝 Intuition

> - Avoid repeated calculations by computing Fibonacci iteratively.
> - Keep only the last two values since F(n) only depends on F(n-1) and F(n-2).
> - Linear time complexity O(n) and constant space O(1).

#### 🔍 Algorithm

```pseudo
function fibIterative(n):
    if n == 0: return 0
    prev = 0
    curr = 1
    for i in 2..n:
        next = prev + curr
        prev = curr
        curr = next
    return curr
```

#### 💻 Implementation

```cpp
// Iterative approach

class Solution {
public:
    int fibIterative(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int prev = 0, curr = 1;

        for (int i = 2; i <= n; i++) {
            int next = prev + curr; // Compute F(i)
            prev = curr;            // Shift previous
            curr = next;            // Update current
        }

        return curr;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Closed-form / Formula)

#### 📝 Intuition

> Use Binet’s formula to compute Fibonacci in $O(1)$ time:
>
> $$
> F(n) = \frac{\phi^n - \psi^n}{\sqrt{5}}
> $$
>
> where
>
> $$
> \phi = \frac{1 + \sqrt{5}}{2}, \quad \psi = \frac{1 - \sqrt{5}}{2}.
> $$
>
> Very fast, but might have slight floating-point rounding issues for large $n$.
>
> Perfect here because $0 \le n \le 30$.

#### 🔍 Algorithm

```pseudo
function fibOptimal(n):
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return round((phi^n - psi^n) / sqrt(5))
```

#### 💻 Implementation

```cpp
// Optimal solution using Binet's formula

#include <cmath>

class Solution {
public:
    int fibOptimal(int n) {
        const double sqrt5 = sqrt(5);
        const double phi = (1 + sqrt5) / 2;
        const double psi = (1 - sqrt5) / 2;

        return (int)round((pow(phi, n) - pow(psi, n)) / sqrt5);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                           |
| -------------- | --------------- | ---------------- | ------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(2^n)          | O(n) recursion   | Very simple, mirrors definition | Extremely slow for n > 20      |
| 🥈 Iterative   | O(n)            | O(1)             | Fast, safe for all n in range   | Still linear time              |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Constant time, elegant formula  | Floating-point rounding issues |

---

<div align="center">

**🎯 Problem 703841 Completed!**

_Happy Coding! 🚀_

</div>
