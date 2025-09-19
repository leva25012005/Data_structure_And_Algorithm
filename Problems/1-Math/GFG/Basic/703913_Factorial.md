<div align="center">

# 🧠 [Factorial](https://www.geeksforgeeks.org/problems/factorial5739/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/factorial5739/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703913`                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Accuracy**     | `40.58%`                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/factorial5739/1)                                                                                                                                                                                                                                                                                                                                |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                                                                                                                                                                                                              |
| **Company Tags** | ![Morgan Stanley](https://img.shields.io/badge/-Morgan%20Stanley-orange?style=flat-square) ![Samsung](https://img.shields.io/badge/-Samsung-orange?style=flat-square) ![FactSet](https://img.shields.io/badge/-FactSet-orange?style=flat-square) ![MAQ Software](https://img.shields.io/badge/-MAQ%20Software-orange?style=flat-square) ![Wipro](https://img.shields.io/badge/-Wipro-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, find the factorial of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 120
<strong>Explanation:</strong> 1 × 2 × 3 × 4 × 5 = 120
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 24
<strong>Explanation:</strong> 1 × 2 × 3 × 4 = 24
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>0 &lt;= n &lt;= 12</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(n)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-for-factorial-of-a-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force Recursive)

#### 📝 Intuition

> - The factorial is defined as:
>
> $$
> n! = n \times (n-1)!
> $$
>
> - Base case:
>
> $$
> 0! = 1
> $$
>
> - Use recursion to compute factorial step by step.
> - This approach is simple and very close to the mathematical definition.

#### 🔍 Algorithm

```pseudo
function factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
```

#### 💻 Implementation

```cpp
// Brute force recursive solution

class Solution {
public:
    int factorialRecursive(int n) {
        // Base case: 0! = 1
        if (n == 0) return 1;
        // Recursive case: n! = n * (n-1)!
        return n * factorialRecursive(n - 1);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Iterative Solution)

#### 📝 Intuition

> - Instead of recursion, loop from 1 to n and multiply.
> - This avoids recursion overhead and stack usage.
> - Works efficiently since n ≤ 12.

#### 🔍 Algorithm

```pseudo
function factorialIterative(n):
    result = 1
    for i in 1..n:
        result *= i
    return result
```

#### 💻 Implementation

```cpp
// Iterative approach using a loop

class Solution {
public:
    int factorialIterative(int n) {
        int res = 1;
        for (int i = 1; i <= n; i++) {
            res *= i; // Multiply each number
        }
        return res;
    }
};

```

### 🥇 Approach 3: Optimal Solution ⭐ (Precomputation / Lookup Table)

#### 📝 Intuition

> - Since the constraint is small (0 ≤ n ≤ 12), we can precompute all factorials in an array.
> - Just return fact[n] in O(1).
> - This is the most efficient for repeated queries.

#### 🔍 Algorithm

```pseudo
precompute fact[0..12]
function factorialOptimal(n):
    return fact[n]
```

#### 💻 Implementation

```cpp
// Optimal solution with precomputation

class Solution {
public:
    int factorialOptimal(int n) {
        // Precomputed factorials from 0! to 12!
        static vector<int> fact = {
            1,       // 0!
            1,       // 1!
            2,       // 2!
            6,       // 3!
            24,      // 4!
            120,     // 5!
            720,     // 6!
            5040,    // 7!
            40320,   // 8!
            362880,  // 9!
            3628800, // 10!
            39916800,// 11!
            479001600// 12!
        };
        return fact[n];
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity         | Pros                             | Cons                                     |
| ------------- | --------------- | ------------------------ | -------------------------------- | ---------------------------------------- |
| 🥉 Recursive  | O(n)            | O(n) (recursion stack)   | Simple, matches definition       | Risk of stack overflow (if n were large) |
| 🥈 Iterative  | O(n)            | O(1)                     | Efficient, no recursion overhead | Still O(n), not instant                  |
| 🥇 Optimal ⭐ | O(1)            | O(1) (or O(n) for table) | Fastest, instant lookup          | Only works for small bounded `n`         |

---

<div align="center">

**🎯 Problem 703913 Completed!**

_Happy Coding! 🚀_

</div>
