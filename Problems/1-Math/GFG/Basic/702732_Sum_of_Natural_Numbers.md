<div align="center">

# 🧠 [Sum of Natural Numbers](https://www.geeksforgeeks.org/problems/sum-of-series2811/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/sum-of-series2811/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                               |
| ---------------- | ----------------------------------------------------------------------------------- |
| **Problem ID**   | `702732`                                                                            |
| **Difficulty**   | ⚪ **Basic**                                                                        |
| **Accuracy**     | `23.81%`                                                                            |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/sum-of-series2811/1) |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, your task is to compute the <strong>sum</strong> of all natural numbers from <code>1</code> to <code>n</code> (inclusive). If <code>n</code> is 0, the sum should be 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> For n = 3, the sum will be 6. 1 + 2 + 3 = 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 15
<strong>Explanation:</strong> For n = 5, the sum will be 15. 1 + 2 + 3 + 4 + 5 = 15
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since n = 0, there are no numbers to sum, so the result is 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<ul>
  <li><code>0 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `17-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `17-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-find-sum-first-n-natural-numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Iterative Loop)

#### 📝 Intuition

> Start from 1 up to n.
> Add all numbers into a running sum.
> Straightforward, but takes O(n) time.

#### 🔍 Algorithm

```pseudo
function iterativeSum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result
```

#### 💻 Implementation

```cpp
// Brute force iterative approach

class Solution {
public:
    int sumOfNumbers(int n) {
        int sum = 0;
        // Add numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Recursive Solution)

#### 📝 Intuition

> - Use recursion: sum(n) = n + sum(n-1).
> - Base case: sum(0) = 0.
> - Simple, but recursion depth may be high (up to 10⁴).

#### 🔍 Algorithm

```pseudo
function recursiveSum(n):
    if n == 0: return 0
    return n + recursiveSum(n-1)
```

#### 💻 Implementation

```cpp
// Recursive approach

class Solution {
public:
    int sumOfNumbers(int n) {
        if (n == 0) return 0;         // Base case
        return n + sumOfNumbers(n-1); // Recursive step
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Formula)

#### 📝 Intuition

> - The sum of first n natural numbers is:
>   $$
>   S = \frac{n \times (n+1)}{2}
>   $$
> - This runs in $O(1)$ time with $O(1)$ space.

#### 🔍 Algorithm

```pseudo
function formulaSum(n):
    return (n * (n + 1)) / 2
```

#### 💻 Implementation

```cpp
// Optimal approach using math formula

class Solution {
public:
    int sumOfNumbers(int n) {
        // Direct formula: n * (n + 1) / 2
        return (n * (n + 1)) / 2;
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                        | Cons                       |
| ------------- | --------------- | ---------------- | --------------------------- | -------------------------- |
| 🥉 Iterative  | O(n)            | O(1)             | Very simple to understand   | Slow for large `n` (loop)  |
| 🥈 Recursive  | O(n)            | O(n) (stack)     | Elegant, short code         | Stack overflow for big `n` |
| 🥇 Formula ⭐ | O(1)            | O(1)             | Fastest, uses math directly | Requires math knowledge    |

---

<div align="center">

**🎯 Problem 702732 Completed!**

_Happy Coding! 🚀_

</div>
