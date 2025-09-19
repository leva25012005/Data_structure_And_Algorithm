<div align="center">

# 🧠 [Find n-th term of series 1, 3, 6, 10, 15, 21](https://www.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703884`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `60.58%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1)                                                     |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a number <code>n</code>, find the <code>n<sup>th</sup></code> term in the series: 1, 3, 6, 10, 15, 21, …</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 10
<strong>Explanation:</strong> The 4th term of the series is 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> The 3rd term of the series is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-nth-term-series-136101521/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Summation Loop)

#### 📝 Intuition

> - Simply sum up numbers from 1 to n.
> - Example: if n=4, compute 1+2+3+4 = 10.
> - Straightforward but takes O(n) time.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    sum = 0
    for i from 1 to n:
        sum += i
    return sum
```

#### 💻 Implementation

```cpp
// Brute force summation loop

class Solution {
public:
    int bruteForceTriangular(int n) {
        int sum = 0;
        // Add numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Recursion)

#### 📝 Intuition

> - Recursive definition:
>
> $$
> T_n = T_{n-1} + n
> \quad \text{with base case } \quad T_1 = 1
> $$
>
> - Keep reducing until we hit the base case.
> - This is more elegant mathematically, but recursion depth may be high ($n \leq 10^4$).

#### 🔍 Algorithm

```pseudo
function recursive(n):
    if n == 1: return 1
    return recursive(n-1) + n
```

#### 💻 Implementation

**C++:**

```cpp
// Recursive approach (not the best for large n but works)

class Solution {
public:
    int recursiveTriangular(int n) {
        if (n == 1) return 1;          // Base case
        return recursiveTriangular(n-1) + n; // Recursive call
    }
};

```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Formula)

#### 📝 Intuition

> - Use the formula for triangular numbers:
>
> $$
> T_n = \frac{n \times (n+1)}{2}
> $$
>
> - This runs in $O(1)$ time with $O(1)$ space.
> - Best and most elegant solution.

#### 🔍 Algorithm

```pseudo
function formula(n):
    return n * (n + 1) / 2
```

#### 💻 Implementation

```cpp
// Most optimal solution using formula

class Solution {
public:
    int formulaTriangular(int n) {
        // Direct formula: n*(n+1)/2
        return n * (n + 1) / 2;
    }
};

```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                         | Cons                         |
| -------------- | --------------- | ---------------- | ---------------------------- | ---------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Simple, easy to understand   | Slow for large n (10^4 loop) |
| 🥈 Recursion   | O(n)            | O(n) (stack)     | Matches definition elegantly | Risk of stack overflow       |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, mathematical neat   | Requires formula knowledge   |

---

<div align="center">

**🎯 Problem 703884 Completed!**

_Happy Coding! 🚀_

</div>
