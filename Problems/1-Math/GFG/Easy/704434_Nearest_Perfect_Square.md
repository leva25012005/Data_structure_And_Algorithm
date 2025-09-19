<div align="center">

# 🧠 [Nearest Perfect Square](https://www.geeksforgeeks.org/problems/are-you-perfect4926/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/are-you-perfect4926/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `704434`                                                                                                                                                                                                                                   |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                |
| **Accuracy**     | `42.84%`                                                                                                                                                                                                                                   |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/are-you-perfect4926/1)                                                                                                                                                      |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Numbers](https://img.shields.io/badge/-Numbers-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <strong>n</strong>, determine the <strong>nearest perfect square</strong> and compute the <strong>absolute difference</strong> between <strong>n</strong> and that perfect square.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> [25, 0]
<strong>Explanation:</strong> Since 25 is a perfect square, it is the closest perfect square to itself. Absolute difference: 25 - 25 = 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 86
<strong>Output:</strong> [81, 5]
<strong>Explanation:</strong> The closest perfect square to 86 is 81. Absolute difference: 86 - 81 = 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(sqrt(n))<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Check all perfect squares from 1^2, 2^2, ... until we pass n.
> - Keep track of the square that gives the smallest absolute difference with n.
> - Simple to implement but inefficient for large n (up to 10^9).

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    i = 1
    minDiff = infinity
    closestSquare = 0
    while i*i <= n:
        diff = n - i*i
        if diff < minDiff:
            minDiff = diff
            closestSquare = i*i
        i += 1
    return [closestSquare, n - closestSquare]
```

#### 💻 Implementation

```cpp
// Brute force: check all squares up to n

class Solution {
public:
    vector<int> nearestPerfectSquare(int n) {
        int closest = 0;
        int minDiff = n; // Initialize with max possible diff

        for (long long i = 1; i * i <= n; i++) {
            int square = i * i;
            int diff = n - square;
            if (diff < minDiff) {
                minDiff = diff;
                closest = square;
            }
        }
        return {closest, n - closest};
    }
};
```

### 🥈 Approach 2: Optimized Solution (sqrt and floor/ceil)

#### 📝 Intuition

> - Compute the integer square root of n → floor(sqrt(n)).
> - The nearest perfect square is either floor(sqrt(n))^2 or ceil(sqrt(n))^2.
> - Choose the one with the smaller absolute difference.
> - Much faster than brute force (O(1) time).

#### 🔍 Algorithm

```pseudo
function optimized(n):
    root = floor(sqrt(n))
    square1 = root^2
    square2 = (root+1)^2
    if |n-square1| <= |square2-n|:
        return [square1, abs(n-square1)]
    else:
        return [square2, abs(n-square2)]
```

#### 💻 Implementation

```cpp
// Optimized: check only floor and ceil of sqrt(n)

#include <cmath>

class Solution {
public:
    vector<int> nearestPerfectSquare(int n) {
        int root = (int)sqrt(n);
        int square1 = root * root;
        int square2 = (root + 1) * (root + 1);

        if (abs(n - square1) <= abs(square2 - n)) {
            return {square1, abs(n - square1)};
        } else {
            return {square2, abs(n - square2)};
        }
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Binary Search)

#### 📝 Intuition

> - Use binary search to find the integer square root of n.
> - The closest perfect square is either mid^2 or (mid+1)^2.
> - Works well even if n is large (up to 10^9).

#### 🔍 Algorithm

```pseudo
function binarySearch(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid*mid == n:
            return [n, 0]
        elif mid*mid < n:
            left = mid + 1
        else:
            right = mid - 1
    closest = max(right^2, left^2) with minimal abs difference
    return [closest, abs(n - closest)]
```

#### 💻 Implementation

```cpp
// Optimal: binary search to find nearest perfect square

class Solution {
public:
    vector<int> nearestPerfectSquare(int n) {
        long long left = 0, right = n;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            long long square = mid * mid;
            if (square == n) return {n, 0};
            else if (square < n) left = mid + 1;
            else right = mid - 1;
        }

        // right^2 <= n < left^2
        long long square1 = right * right;
        long long square2 = left * left;
        if (abs(n - square1) <= abs(square2 - n))
            return {(int)square1, (int)abs(n - square1)};
        else
            return {(int)square2, (int)abs(n - square2)};
    }
};
```

## 📊 Comparison of Approaches

| Approach            | Time Complexity | Space Complexity | Pros                           | Cons                |
| ------------------- | --------------- | ---------------- | ------------------------------ | ------------------- |
| 🥉 Brute Force      | O(√n)           | O(1)             | Easy to understand             | Slow for large n    |
| 🥈 Optimized        | O(1)            | O(1)             | Very fast, simple              | Needs sqrt function |
| 🥇 Binary Search ⭐ | O(log n)        | O(1)             | Elegant, scalable, avoids sqrt | Slightly more code  |

---

<div align="center">

**🎯 Problem 704434 Completed!**

_Happy Coding! 🚀_

</div>
