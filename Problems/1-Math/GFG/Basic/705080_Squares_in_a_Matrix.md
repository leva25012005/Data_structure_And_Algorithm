<div align="center">

# 🧠 [Squares in a Matrix](https://www.geeksforgeeks.org/problems/squares-in-a-matrix5716/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/squares-in-a-matrix5716/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `705080`                                                                                                                                                                                                                                         |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                     |
| **Accuracy**     | `34.59%`                                                                                                                                                                                                                                         |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/squares-in-a-matrix5716/1)                                                                                                                                                        |
| **Topic Tags**   | ![Matrix](https://img.shields.io/badge/-Matrix-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Junglee Games](https://img.shields.io/badge/-Junglee%20Games-orange?style=flat-square)                                                                                                                                                         |

## Description

<!-- description:start -->

<p>Given an <code>m x n</code> matrix, count the total number of <strong>squares</strong> present in the matrix.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> m = 2, n = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are a total of 5 squares in a 2x2 matrix:
- Four 1x1 squares
- One 2x2 square
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 4, n = 3
<strong>Output:</strong> 20
<strong>Explanation:</strong> There are a total of 20 squares in a 4x3 matrix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/count-number-of-squares-in-a-rectangle/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Enumeration)

#### 📝 Intuition

> - In an m x n grid, a square can be of size k x k where k ≤ min(m, n).
> - For each possible size k, slide the square across the matrix and count how many positions it fits.
> - The number of k x k squares = (m - k + 1) \* (n - k + 1).
> - Add up for all k.
> - This brute force explicitly checks each size.

#### 🔍 Algorithm

```pseudo
function bruteForce(m, n):
    total = 0
    for k = 1 to min(m, n):
        total += (m - k + 1) * (n - k + 1)
    return total
```

#### 💻 Implementation

```cpp
// Brute force approach (enumerate all square sizes)

class Solution {
public:
    long long countSquares(int m, int n) {
        long long total = 0;
        for (int k = 1; k <= min(m, n); k++) {
            total += (long long)(m - k + 1) * (n - k + 1);
        }
        return total;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Formula-based)

#### 📝 Intuition

> - From Approach 1, we know:
>
> $$
> total = \sum_{k=1}^{\min(m,n)} (m - k + 1)(n - k + 1)
> $$
>
> - This can be simplified by algebra (expand and use arithmetic series sums).
> - But instead of doing heavy math, we can compute directly in a single loop.
> - This is faster because we avoid generating sub-results.

#### 🔍 Algorithm

```pseudo
function optimized(m, n):
    min_side = min(m, n)
    total = 0
    for k = 1 to min_side:
        total += (m - k + 1) * (n - k + 1)
    return total
```

#### 💻 Implementation

```cpp
// Optimized solution using direct summation

class Solution {
public:
    long long countSquares(int m, int n) {
        long long total = 0;
        int minSide = min(m, n);
        for (int k = 1; k <= minSide; k++) {
            total += (long long)(m - k + 1) * (n - k + 1);
        }
        return total;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Closed-Form Formula)

#### 📝 Intuition

> The sum can be expressed in closed form using formula of arithmetic series:
>
> $$
> total = \sum_{k=1}^{\min(m,n)} (m-k+1)(n-k+1)
> $$
>
> Expand:
>
> $$
> = \sum_{k=1}^{\min(m,n)} \Big( mn - m(k-1) - n(k-1) + (k-1)^2 \Big)
> $$
>
> This can be computed using:
>
> - Sum of first $p$ integers:
>
>   $$
>   \sum_{i=1}^{p} i = \frac{p(p+1)}{2}
>   $$
>
> - Sum of squares of first $p$ integers:
>   $$
>   \sum_{i=1}^{p} i^2 = \frac{p(p+1)(2p+1)}{6}
>   $$
>
> That gives an **$O(1)$ solution**.

#### 🔍 Algorithm

```pseudo
function optimal(m, n):
    p = min(m, n)
    total = p*mn - (m+n)*p*(p-1)/2 + (p-1)p(2p-1)/6
    return total
```

#### 💻 Implementation

```cpp
// Optimal solution using closed-form formula

class Solution {
public:
    long long countSquares(int m, int n) {
        long long p = min(m, n);

        // Use formula for sums
        // sum(i=0 to p-1) = (p-1)*p/2
        // sum(i^2 for i=0 to p-1) = (p-1)*p*(2p-1)/6

        long long total = p * 1LL * m * n
                        - (m + n) * 1LL * (p * (p - 1) / 2)
                        + ( (p - 1) * p * (2 * p - 1) / 6 );
        return total;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                      |
| -------------- | --------------- | ---------------- | ------------------------------- | ------------------------- |
| 🥉 Brute Force | O(min(m,n))     | O(1)             | Very intuitive, easy to code    | Redundant repeated math   |
| 🥈 Optimized   | O(min(m,n))     | O(1)             | Clean, works fast up to 1e4     | Still linear in min(m, n) |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant closed form, super fast | Harder to derive formula  |

---

<div align="center">

**🎯 Problem 705080 Completed!**

_Happy Coding! 🚀_

</div>
