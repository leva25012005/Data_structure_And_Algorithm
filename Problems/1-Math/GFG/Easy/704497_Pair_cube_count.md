<div align="center">

# 🧠 [Pair cube count](https://www.geeksforgeeks.org/problems/pair-cube-count4132/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/pair-cube-count4132/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704497`                                                                                                                                                          |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                       |
| **Accuracy**     | `30.87%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/pair-cube-count4132/1)                                                                             |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Adobe](https://img.shields.io/badge/-Adobe-orange?style=flat-square)                                                                                            |

## Description

<!-- description:start -->

<p>Given a positive integer <strong>n</strong>, count all pairs of integers <strong>a</strong> (≥1) and <strong>b</strong> (≥0) such that:</p>

<p><strong>a<sup>3</sup> + b<sup>3</sup> = n</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two solutions: (a=1, b=2) and (a=2, b=1)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 27
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only one solution: (a=3, b=0)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 ≤ n ≤ 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(cbrt(n))<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/count-pairs-a-b-whose-sum-of-cubes-is-n-a3-b3-n/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Try all a, b)

#### 📝 Intuition

> - We need pairs (a, b) such that a^3 + b^3 = n.
> - Brute force: Try all a from 1 to n and all b from 0 to n, check if a^3 + b^3 = n.
> - Correct but very slow for large n.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    count = 0
    for a in 1..n:
        for b in 0..n:
            if a^3 + b^3 == n:
                count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute force solution: O(n^2)
class Solution {
public:
    int countPairs(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 0; b <= n; b++) {
                if (a*a*a + b*b*b == n) {
                    count++; // valid pair found
                }
            }
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Limit by cube root)

#### 📝 Intuition

> - The cube of a cannot exceed n, so a ≤ cbrt(n).
> - Similarly, b ≤ cbrt(n).
> - Only iterate a from 1 to floor(cbrt(n)) and compute b = cbrt(n - a^3).
> - Check if b^3 matches n - a^3.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    count = 0
    for a in 1..cbrt(n):
        remainder = n - a^3
        b = floor(cbrt(remainder))
        if b^3 == remainder:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Optimized approach: O(cbrt(n))
#include <cmath>

class Solution {
public:
    int countPairs(int n) {
        int count = 0;
        int limit = cbrt(n); // maximum possible value for a
        for (int a = 1; a <= limit; a++) {
            int remainder = n - a*a*a;
            if (remainder < 0) break; // no solution possible
            int b = round(cbrt(remainder)); // candidate b
            if (b*b*b == remainder && b >= 0) {
                count++; // valid pair found
            }
        }
        return count;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Two-Pointer)

#### 📝 Intuition

> - Use two pointers: a = 1 and b = floor(cbrt(n)).
> - If a^3 + b^3 < n, increment a.
> - If a^3 + b^3 > n, decrement b.
> - If a^3 + b^3 == n, count the pair and increment a, decrement b.
> - Very fast, O(cbrt(n)), no floating point rounding issues.

#### 🔍 Algorithm

```pseudo
function twoPointer(n):
    count = 0
    a = 1
    b = floor(cbrt(n))
    while a <= b:
        sum = a^3 + b^3
        if sum == n:
            count += 1
            a += 1
            b -= 1
        else if sum < n:
            a += 1
        else:
            b -= 1
    return count
```

#### 💻 Implementation

```cpp
// Two-pointer solution: O(cbrt(n))
#include <cmath>

class Solution {
public:
    int countPairs(int n) {
        int count = 0;
        int a = 1;
        int b = cbrt(n); // start with largest possible b
        while (a <= b) {
            long long sum = (long long)a*a*a + (long long)b*b*b;
            if (sum == n) {
                count++;  // valid pair found
                a++;
                b--;
            } else if (sum < n) {
                a++; // need bigger sum
            } else {
                b--; // need smaller sum
            }
        }
        return count;
    }
};
```

## 📊 Comparison of Approaches

| Approach          | Time Complexity | Space Complexity | Pros                            | Cons                     |
| ----------------- | --------------- | ---------------- | ------------------------------- | ------------------------ |
| 🥉 Brute Force    | O(n^2)          | O(1)             | Very simple to understand       | Too slow for n > 100     |
| 🥈 Optimized      | O(cbrt(n))      | O(1)             | Fast enough, simple             | Needs cube root rounding |
| 🥇 Two-Pointer ⭐ | O(cbrt(n))      | O(1)             | Elegant, avoids rounding issues | Slightly more logic      |

---

<div align="center">

**🎯 Problem 704497 Completed!**

_Happy Coding! 🚀_

</div>
