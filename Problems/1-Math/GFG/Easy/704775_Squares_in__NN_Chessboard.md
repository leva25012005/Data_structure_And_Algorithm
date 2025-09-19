<div align="center">

# 🧠 [Squares in N\*N Chessboard](https://www.geeksforgeeks.org/problems/squares-in-nn-chessboard1801/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/squares-in-nn-chessboard1801/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704775`                                                                                                                                                                                                                                                                                                                                |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                                                             |
| **Accuracy**     | `66.14%`                                                                                                                                                                                                                                                                                                                                |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/squares-in-nn-chessboard1801/1)                                                                                                                                                                                                                                          |
| **Topic Tags**   | ![number-theory](https://img.shields.io/badge/-number-theory-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![permutation](https://img.shields.io/badge/-permutation-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Goldman Sachs](https://img.shields.io/badge/-Goldman%20Sachs-orange?style=flat-square) ![MAQ Software](https://img.shields.io/badge/-MAQ%20Software-orange?style=flat-square)                                                                                                                                                         |

## Description

<!-- description:start -->

<p>Find the total number of squares in an <strong>N × N</strong> chessboard.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> N = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> A 1×1 chessboard has only 1 square.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> N = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> A 2×2 chessboard has 5 squares:
4 squares of size 1×1 and 1 square of size 2×2.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task:</strong></p>

<p>You don't need to read input or print anything. Complete the function <strong>squaresInChessBoard(N)</strong> which takes an integer <strong>N</strong> and returns the total number of squares in an N×N chessboard.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ N ≤ 10<sup>5</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-to-find-number-of-squares-on-a-chessboard/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Counting)

#### 📝 Intuition

> - For each possible square size k × k (1 ≤ k ≤ N), count how many such squares fit inside the chessboard.
> - For size k, the number of possible squares = (N - k + 1)².
> - Sum over all k.
> - This is straightforward but requires looping up to N.

#### 🔍 Algorithm

```pseudo
function bruteForce(N):
    total = 0
    for k in range(1, N+1):
        total += (N - k + 1) * (N - k + 1)
    return total
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    long long squaresInChessBoard(long long N) {
        long long total = 0;
        // Count squares of each possible size
        for (long long k = 1; k <= N; k++) {
            total += (N - k + 1) * (N - k + 1);
        }
        return total;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Formula Derivation)

#### 📝 Intuition

> We know:
>
> $$
> \text{Total squares} = \sum_{k=1}^{N} (N-k+1)^2
> $$
>
> Let’s simplify:
>
> $$
> = \sum_{k=1}^{N} k^2
> $$
>
> (because reversing order gives the same sum).
>
> We use the formula:
>
> $$
> \sum_{k=1}^{N} k^2 = \frac{N(N+1)(2N+1)}{6}
> $$
>
> This gives a direct $O(1)$ solution.

#### 🔍 Algorithm

```pseudo
function optimized(N):
    return N * (N+1) * (2N+1) / 6
```

#### 💻 Implementation

```cpp
// Optimized approach using sum of squares formula

class Solution {
public:
    long long squaresInChessBoard(long long N) {
        return (N * (N + 1) * (2 * N + 1)) / 6;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Math + Clean Code)

#### 📝 Intuition

> - The O(1) formula is already optimal.
> - But we can ensure it works for large N (up to 1e5) using long long to prevent overflow.
> - Implementation remains elegant and safe.

#### 🔍 Algorithm

```pseudo
function optimal(N):
    return (N * (N+1) * (2N+1)) // 6  // use long long
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution with safe types

class Solution {
public:
    long long squaresInChessBoard(long long N) {
        // Using long long to prevent overflow for large N
        return (N * (N + 1) * (2 * N + 1)) / 6;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                   | Cons                  |
| -------------- | --------------- | ---------------- | -------------------------------------- | --------------------- |
| 🥉 Brute Force | O(N)            | O(1)             | Easy to understand                     | Too slow for N = 1e5  |
| 🥈 Optimized   | O(1)            | O(1)             | Uses mathematical formula, very fast   | Requires math insight |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, safe for large values of `N` | Nome                  |

---

<div align="center">

**🎯 Problem 704775 Completed!**

_Happy Coding! 🚀_

</div>
