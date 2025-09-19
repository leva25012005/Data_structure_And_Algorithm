<div align="center">

# 🧠 [Modular Exponentiation](https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703909`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Accuracy**     | `52.56%`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Topic Tags**   | ![Divide and Conquer](https://img.shields.io/badge/-Divide%20and%20Conquer-blue?style=flat-square) ![Binary Search](https://img.shields.io/badge/-Binary%20Search-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) ![number-theory](https://img.shields.io/badge/-number-theory-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Modular Arithmetic](https://img.shields.io/badge/-Modular%20Arithmetic-blue?style=flat-square) |
| **Company Tags** | ![Google](https://img.shields.io/badge/-Google-orange?style=flat-square)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Description

<!-- description:start -->

<p>Given three integers <strong>x</strong>, <strong>n</strong>, and <strong>M</strong>, compute <code>(x^n) % M</code>, i.e., the remainder when <strong>x</strong> raised to the power <strong>n</strong> is divided by <strong>M</strong>.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> x = 3, n = 2, M = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> 3^2 % 4 = 9 % 4 = 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> x = 2, n = 6, M = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> 2^6 % 10 = 64 % 10 = 4
</pre>

## Constraints

<ul>
  <li><code>1 ≤ x, n, M ≤ 10^9</code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(log n)</li>
  <li><strong>Auxiliary Space:</strong> O(1)</li>
</ul>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Directly compute x^n by multiplying x repeatedly n times.
> - Then take % M.
> - This is simple but very slow when n is large (n can be up to 10^9).

#### 🔍 Algorithm

```pseudo
function bruteForce(x, n, M):
    result = 1
    for i from 1 to n:
        result = result * x
    return result % M
```

#### 💻 Implementation

```cpp
// Brute force approach (not feasible for large n)

class Solution {
public:
    int modPowBruteForce(int x, int n, int M) {
        long long result = 1;
        for (int i = 0; i < n; i++) {
            result = (result * x); // multiply repeatedly
        }
        return result % M;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Iterative Modular Multiplication)

#### 📝 Intuition

> - Multiply iteratively taking modulo at each step to avoid overflow.
> - Still O(n) but handles large numbers safely.

#### 🔍 Algorithm

```pseudo
function iterativeMod(x, n, M):
    result = 1
    for i from 1 to n:
        result = (result * x) % M
    return result
```

#### 💻 Implementation

```cpp
// Iterative modular multiplication

class Solution {
public:
    int modPowIterative(int x, int n, int M) {
        long long result = 1;
        for (int i = 0; i < n; i++) {
            result = (result * x) % M; // take modulo at each step
        }
        return result;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Binary Exponentiation)

#### 📝 Intuition

> - Use binary exponentiation (exponentiation by squaring):
>   - If n is even → x^n = (x^(n/2))^2
>   - If n is odd → x^n = x \* (x^(n-1))
> - Take modulo M at each step.
> - This reduces time complexity to O(log n).

#### 🔍 Algorithm

```pseudo
function modPow(x, n, M):
    result = 1
    base = x % M
    while n > 0:
        if n is odd:
            result = (result * base) % M
        base = (base * base) % M
        n = n // 2
    return result
```

#### 💻 Implementation

```cpp
// Binary exponentiation (optimal)

class Solution {
public:
    int modPow(int x, int n, int M) {
        long long result = 1;
        long long base = x % M; // handle large x
        while (n > 0) {
            if (n % 2 == 1) {         // if n is odd
                result = (result * base) % M;
            }
            base = (base * base) % M; // square the base
            n /= 2;                   // divide n by 2
        }
        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                           | Cons                         |
| -------------- | --------------- | ---------------- | ------------------------------ | ---------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Simple to understand           | Too slow for large n         |
| 🥈 Iterative   | O(n)            | O(1)             | Prevents overflow using modulo | Still too slow for n \~ 10^9 |
| 🥇 Optimal ⭐  | O(log n)        | O(1)             | Fastest, handles large numbers | Slightly more complex logic  |

---

<div align="center">

**🎯 Problem 703909 Completed!**

_Happy Coding! 🚀_

</div>
