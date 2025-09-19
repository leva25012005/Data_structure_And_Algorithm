<div align="center">

# 🧠 [Sum of Squares of First n Natural Numbers](https://www.geeksforgeeks.org/problems/sum-of-squares-of-first-n-natural-numbers/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/sum-of-squares-of-first-n-natural-numbers/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `887939`                                                                                                    |
| **Difficulty**   | 🟢 **Easy**                                                                                                 |
| **Accuracy**     | `81.7%`                                                                                                     |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/sum-of-squares-of-first-n-natural-numbers/1) |

## Description

<!-- description:start -->

<p>Given an integer <strong>n</strong>, the task is to calculate the sum of the squares of the first <strong>n</strong> natural numbers.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> 1² + 2² = 5
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 14
<strong>Explanation:</strong> 1² + 2² + 3² = 14
</pre>

## Constraints

<ul>
  <li><code>0 ≤ n ≤ 10³</code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/Sum of squares of first n natural numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Loop)

#### 📝 Intuition

> - Start from 1 up to n.
> - Compute the square of each number and accumulate the sum.
> - Simple and intuitive, but takes O(n) time.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    sum = 0
    for i = 1 to n:
        sum += i * i
    return sum
```

#### 💻 Implementation

```cpp
// Brute force solution using loop

class Solution {
public:
    int sumOfSquaresBrute(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i * i; // Add square of i
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Recursion)

#### 📝 Intuition

- > - Use recursion: f(n) = n² + f(n-1)
  > - Base case: f(0) = 0.
  > - Works fine for small constraints (n ≤ 1000), but recursion depth could be a limitation in larger cases.

#### 🔍 Algorithm

```pseudo
function recursive(n):
    if n == 0: return 0
    return n*n + recursive(n-1)
```

#### 💻 Implementation

```cpp
// Recursive approach

class Solution {
public:
    int sumOfSquaresRecursive(int n) {
        if (n == 0) return 0; // Base case
        return n * n + sumOfSquaresRecursive(n - 1);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Formula)

#### 📝 Intuition

> Use the direct formula for the sum of squares:
>
> $$
> 1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}
> $$
>
> This runs in $O(1)$ time with $O(1)$ space.  
> Most efficient and elegant solution.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return n*(n+1)*(2n+1) / 6
```

#### 💻 Implementation

```cpp
// Optimal approach using formula

class Solution {
public:
    int sumOfSquaresOptimal(int n) {
        // Formula: n(n+1)(2n+1)/6
        return (n * (n + 1) * (2 * n + 1)) / 6;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                           | Cons                         |
| -------------- | --------------- | ---------------- | ------------------------------ | ---------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very simple, easy to code      | Slower for large n           |
| 🥈 Recursion   | O(n)            | O(n) (stack)     | Elegant, demonstrates DP idea  | Stack overflow for big n     |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, constant-time formula | Requires knowing the formula |

---

<div align="center">

**🎯 Problem 887939 Completed!**

_Happy Coding! 🚀_

</div>
