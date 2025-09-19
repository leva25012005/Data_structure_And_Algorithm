<div align="center">

# 🧠 [Series AP](https://www.geeksforgeeks.org/problems/series-ap5310/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/series-ap5310/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703967`                                                                                                                                                                                                                                 |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                             |
| **Accuracy**     | `59.24%`                                                                                                                                                                                                                                 |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/series-ap5310/1)                                                                                                                                                          |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![series](https://img.shields.io/badge/-series-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given the first two terms <code>a1</code> and <code>a2</code> of an Arithmetic Series, find the <strong>n<sup>th</sup></strong> term of the series.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a1 = 2, a2 = 3, n = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> The series is 2, 3, 4, 5, 6 ... Thus, the 4th term is 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a1 = 1, a2 = 3, n = 10
<strong>Output:</strong> 19
<strong>Explanation:</strong> The series is 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ... Thus, the 10th term is 19.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>-10<sup>4</sup> &lt;= a1, a2 &lt;= 10<sup>4</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/how-to-find-the-nth-term-of-an-arithmetic-sequence/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/nth-term-of-ap-from-first-two-terms/)
3. [GeeksforGeeks Article 3](https://www.geeksforgeeks.org/program-n-th-term-arithmetic-progression-series/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Iterative)

#### 📝 Intuition

> - Start from a1 and a2.
> - Compute the common difference d = a2 - a1.
> - Iteratively generate each term until reaching the nth term.
> - This is simple but not the most efficient.

#### 🔍 Algorithm

```pseudo
function nthTerm(a1, a2, n):
    d = a2 - a1
    term = a1
    for i = 2 to n:
        term += d
    return term
```

#### 💻 Implementation

```cpp
// Brute force: iterative computation

class Solution {
public:
    int nthTerm(int a1, int a2, int n) {
        int d = a2 - a1; // Common difference
        int term = a1;
        for (int i = 2; i <= n; i++) {
            term += d; // Generate next term iteratively
        }
        return term;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Formula-Based)

#### 📝 Intuition

> - Arithmetic series has formula: an = a1 + (n-1) \* d, where d = a2 - a1.
> - Directly compute the nth term without iteration.
> - Much faster for large n.

#### 🔍 Algorithm

```pseudo
function nthTerm(a1, a2, n):
    d = a2 - a1
    return a1 + (n - 1) * d
```

#### 💻 Implementation

```cpp
// Optimized approach using formula

class Solution {
public:
    int nthTerm(int a1, int a2, int n) {
        int d = a2 - a1;         // Compute common difference
        return a1 + (n - 1) * d; // Direct formula
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (One-Liner)

#### 📝 Intuition

> Same as approach 2, but write as a single concise return statement.
> Minimal code, easy to read, O(1) time and space

#### 🔍 Algorithm

```pseudo
function nthTerm(a1, a2, n):
    return a1 + (n - 1) * (a2 - a1)
```

#### 💻 Implementation

```cpp
// Elegant one-liner solution

class Solution {
public:
    int nthTerm(int a1, int a2, int n) {
        return a1 + (n - 1) * (a2 - a1); // Direct computation in one line
    }
};
```

## 📊 Comparison of Approaches

| Approach        | Time Complexity | Space Complexity | Pros                       | Cons               |
| --------------- | --------------- | ---------------- | -------------------------- | ------------------ |
| 🥉 Brute Force  | O(n)            | O(1)             | Simple, easy to understand | Slower for large n |
| 🥈 Formula      | O(1)            | O(1)             | Fast, optimal for large n  | None               |
| 🥇 One-Liner ⭐ | O(1)            | O(1)             | Very concise and elegant   | None               |

---

<div align="center">

**🎯 Problem 703967 Completed!**

_Happy Coding! 🚀_

</div>
