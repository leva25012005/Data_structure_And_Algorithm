<div align="center">

# 🧠 [Maximum number of 2X2 squares](https://www.geeksforgeeks.org/problems/maximum-number-of-22-squares/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/maximum-number-of-22-squares/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `706369`                                                                                                                                                          |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                       |
| **Accuracy**     | `66.64%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/maximum-number-of-22-squares/1)                                                                    |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square)                                                                                    |

## Description

<!-- description:start -->

<p>Given the base <strong>N</strong> (in units) of a right-angled isosceles triangle, find the maximum number of <strong>2×2</strong> squares that can fit inside the triangle.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> N = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
We can place 3 squares in the first row, 2 in the second row, and 1 in the third row, making a total of 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> N = 7
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
In the base row we can place 2 squares, and in the row above it we can place only 1 square. 
So the total number of squares is 3.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ N ≤ 10<sup>9</sup></code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/maximum-number-2x2-squares-can-fit-inside-right-isosceles-triangle/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Imagine filling the triangle row by row.
> - Each row (starting from the base) can hold a certain number of 2×2 squares.
> - For row i (0-based from the bottom), the row can hold floor((N/2) - i) squares.
> - Sum over all rows until it becomes zero.
> - This works but is inefficient for very large N (up to 10^9).

#### 🔍 Algorithm

```pseudo
function bruteForce(N):
    rows = floor(N / 2)
    total = 0
    for i in 0..rows-1:
        total += (rows - i)
    return total
```

#### 💻 Implementation

**C++:**

```cpp
// Brute force simulation (not feasible for very large N)

class Solution {
public:
    long long maxSquaresBruteForce(long long N) {
        long long rows = N / 2; // Number of possible square rows
        long long total = 0;
        for (long long i = 0; i < rows; i++) {
            total += (rows - i); // Decreasing squares per row
        }
        return total;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - From brute force, we see that the number of squares forms a sequence:
>   - For N = 8: 3 + 2 + 1 = 6
>   - For N = 7: 2 + 1 = 3
> - General case: Let k = floor(N / 2).
> - Then result = k + (k-1) + ... + 1 = k\*(k+1)/2.
> - This gives us O(1) solution.

#### 🔍 Algorithm

```pseudo
function optimized(N):
    k = floor(N / 2)
    return k * (k + 1) / 2
```

#### 💻 Implementation

```cpp
// Optimized approach using direct formula

class Solution {
public:
    long long maxSquaresOptimized(long long N) {
        long long k = N / 2; // Maximum squares in base row
        return k * (k + 1) / 2; // Arithmetic series sum
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - The optimal solution is already the formula k\*(k+1)/2.
> - To make it elegant:
>   - Handle both odd and even N seamlessly with integer division (N/2).
>   - Use 64-bit integers (long long) since N can be up to 10^9 (answer can be ~10^18).

#### 🔍 Algorithm

```pseudo
function optimal(N):
    k = N // 2
    return k * (k + 1) / 2
```

#### 💻 Implementation

**C++:**

```cpp
// Most optimal and elegant solution

class Solution {
public:
    long long maxSquares(long long N) {
        long long k = N / 2; // Number of 2x2 squares along the base
        return (k * (k + 1)) / 2; // Use arithmetic progression formula
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                                |
| -------------- | --------------- | ---------------- | ----------------------------------- | ----------------------------------- |
| 🥉 Brute Force | O(N)            | O(1)             | Very intuitive, simulates process   | Impossible for N up to 10^9         |
| 🥈 Optimized   | O(1)            | O(1)             | Simple formula, fast                | Requires recognizing arithmetic sum |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, direct formula, efficient | Nothing really!                     |

---

<div align="center">

**🎯 Problem 706369 Completed!**

_Happy Coding! 🚀_

</div>
