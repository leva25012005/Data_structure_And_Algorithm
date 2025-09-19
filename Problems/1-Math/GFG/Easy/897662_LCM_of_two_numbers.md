<div align="center">

# 🧠 [LCM of two numbers](https://www.geeksforgeeks.org/problems/lcm-of-two-numbers/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/lcm-of-two-numbers/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Problem ID**   | `897662`                                                                             |
| **Difficulty**   | 🟢 **Easy**                                                                          |
| **Accuracy**     | `71.3%`                                                                              |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/lcm-of-two-numbers/1) |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square)   |

## Description

<!-- description:start -->

<p>You are given two positive integers <strong>a</strong> and <strong>b</strong>. Your task is to compute and return the Least Common Multiple (LCM) of the two numbers.</p>
<p>The <strong>LCM</strong> of two integers is the smallest positive integer that is divisible by both <strong>a</strong> and <strong>b</strong>.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> a = 12, b = 18
<strong>Output:</strong> 36
<strong>Explanation:</strong> LCM of 12 and 18 is 36.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> a = 5, b = 11
<strong>Output:</strong> 55
<strong>Explanation:</strong> LCM of 5 and 11 is 55.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ a, b ≤ 10⁴</code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(log(min(a, b)))<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Incremental Search)

#### 📝 Intuition

> - Start from the maximum of a and b.
> - Incrementally check each number to see if it is divisible by both a and b.
> - The first number that satisfies this is the LCM.
> - This works but is inefficient for large numbers.

#### 🔍 Algorithm

```pseudo
function bruteForceLCM(a, b):
    candidate = max(a, b)
    while true:
        if candidate % a == 0 and candidate % b == 0:
            return candidate
        candidate += 1
```

#### 💻 Implementation

```cpp
// Brute force approach (slow for large inputs)

class Solution {
public:
    int lcmBruteForce(int a, int b) {
        int candidate = max(a, b); // Start from the larger of the two
        while (true) {
            // Check divisibility
            if (candidate % a == 0 && candidate % b == 0) {
                return candidate;
            }
            candidate++;
        }
    }
};
```

### 🥈 Approach 2: Optimized Solution Using Formula with GCD

#### 📝 Intuition

> Use the mathematical relation:
>
> $$
> \text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}
> $$
>
> Compute GCD using Euclidean algorithm.  
> Then compute LCM directly.

#### 🔍 Algorithm

```pseudo
function gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

function optimizedLCM(a, b):
    return (a * b) / gcd(a, b)
```

#### 💻 Implementation

**C++:**

```cpp
// Optimized approach using GCD

class Solution {
public:
    // Euclidean algorithm to compute GCD
    int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

    int lcmOptimized(int a, int b) {
        return (a / gcd(a, b)) * b;
        // Divide before multiply to avoid overflow
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Built-in GCD / Recursive Euclidean)

#### 📝 Intuition

> - C++17 already provides std::gcd.
> - We can use it directly, which is fast and clean.
> - Or implement recursive Euclidean algorithm for elegance.

#### 🔍 Algorithm

```pseudo
function gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

function optimalLCM(a, b):
    return (a / gcd(a, b)) * b
```

#### 💻 Implementation

```cpp
// Most optimal solution using recursion (or std::gcd in C++17)

#include <numeric> // for std::gcd (C++17 and above)

class Solution {
public:
    // Recursive GCD
    int gcdRecursive(int x, int y) {
        if (y == 0) return x;
        return gcdRecursive(y, x % y);
    }

    int lcmOptimal(int a, int b) {
        // Option 1: Use recursive gcd
        int g = gcdRecursive(a, b);

        // Option 2: Use built-in gcd if available
        // int g = std::gcd(a, b);

        return (a / g) * b;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity   | Space Complexity | Pros                        | Cons                          |
| -------------- | ----------------- | ---------------- | --------------------------- | ----------------------------- |
| 🥉 Brute Force | O(max(a, b))      | O(1)             | Very simple, no math needed | Extremely slow for big inputs |
| 🥈 Optimized   | O(log(min(a, b))) | O(1)             | Efficient, works for all n  | Slightly more code            |
| 🥇 Optimal ⭐  | O(log(min(a, b))) | O(1)             | Cleanest, can use std::gcd  | Requires C++17 for built-in   |

---

<div align="center">

**🎯 Problem 897662 Completed!**

_Happy Coding! 🚀_

</div>
