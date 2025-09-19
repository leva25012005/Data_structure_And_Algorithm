<div align="center">

# 🧠 [Square Root](https://www.geeksforgeeks.org/problems/square-root/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/square-root/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `700226`                                                                                                                                                                                                                                                                                                                                                                                   |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                                                                                                                |
| **Accuracy**     | `54.03%`                                                                                                                                                                                                                                                                                                                                                                                   |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/square-root/1)                                                                                                                                                                                                                                                                                                              |
| **Topic Tags**   | ![Searching](https://img.shields.io/badge/-Searching-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Binary Search](https://img.shields.io/badge/-Binary%20Search-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                      |
| **Company Tags** | ![VMWare](https://img.shields.io/badge/-VMWare-orange?style=flat-square) ![Flipkart](https://img.shields.io/badge/-Flipkart-orange?style=flat-square) ![Accolite](https://img.shields.io/badge/-Accolite-orange?style=flat-square) ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, find the <strong>square root</strong> of <code>n</code>. If <code>n</code> is not a perfect square, return the <strong>floor value</strong> of its square root.</p>

<p><strong>Note:</strong> The floor value of a number is the greatest integer less than or equal to that number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> 4 is a perfect square, so its square root is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 is not a perfect square, so floor(sqrt(11)) = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 is a perfect square, so its square root is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 3*10<sup>4</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/square-root-of-an-integer/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Try all integers i starting from 1 upwards.
> - Stop when i\*i > n.
> - The largest i such that i\*i ≤ n is the floor of the square root.
> - Simple and easy to understand, but O(√n) time.

#### 🔍 Algorithm

```pseudo
function bruteForceSqrt(n):
    i = 1
    while i * i <= n:
        i += 1
    return i - 1
```

#### 💻 Implementation

```cpp
// Brute force approach: O(√n)

class Solution {
public:
    int floorSqrt(int n) {
        int i = 1;
        while (i * i <= n) {
            i++;
        }
        return i - 1; // Last i whose square <= n
    }
};
```

### 🥈 Approach 2: Optimized Solution (Binary Search)

#### 📝 Intuition

> - Use binary search between 1 and n to find the floor of square root.
> - If mid\*mid == n, return mid.
> - If mid\*mid < n, move right (start = mid+1).
> - Else move left (end = mid-1).
> - This is efficient and runs in O(log n) time.

#### 🔍 Algorithm

```pseudo
function binarySearchSqrt(n):
    start = 1
    end = n
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid*mid == n: return mid
        if mid*mid < n: ans = mid; start = mid + 1
        else: end = mid - 1
    return ans
```

#### 💻 Implementation

```cpp
// Binary search approach: O(log n)

class Solution {
public:
    int floorSqrt(int n) {
        if (n == 0 || n == 1) return n;

        int start = 1, end = n, ans = 0;
        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (mid <= n / mid) { // Avoid overflow
                ans = mid;       // mid*mid <= n, possible answer
                start = mid + 1; // Try higher
            } else {
                end = mid - 1;   // mid*mid > n, go lower
            }
        }
        return ans;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Built-in Function)

#### 📝 Intuition

> - Use the square root function sqrt(n) from <cmath> and take floor().
> - This gives O(1) time complexity as expected by the problem.

#### 🔍 Algorithm

```pseudo
function sqrtFloor(n):
    return floor(sqrt(n))
```

#### 💻 Implementation

```cpp
// Optimal approach: O(1)

#include <cmath>

class Solution {
public:
    int floorSqrt(int n) {
        return (int) sqrt(n); // Automatically floor the result
    }
};
```

## 📊 Comparison of Approaches

| Approach         | Time Complexity | Space Complexity | Pros                      | Cons                       |
| ---------------- | --------------- | ---------------- | ------------------------- | -------------------------- |
| 🥉 Brute Force   | O(√n)           | O(1)             | Simple, easy to implement | Slow for large n           |
| 🥈 Binary Search | O(log n)        | O(1)             | Fast, no library needed   | Slightly more code         |
| 🥇 Optimal ⭐    | O(1)            | O(1)             | Very fast, minimal code   | Relies on library function |

---

<div align="center">

**🎯 Problem 700226 Completed!**

_Happy Coding! 🚀_

</div>
