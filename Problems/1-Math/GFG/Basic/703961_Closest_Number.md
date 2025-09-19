<div align="center">

# 🧠 [Closest Number](https://www.geeksforgeeks.org/problems/closest-number5728/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/closest-number5728/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703961`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `15.77%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/closest-number5728/1)                                                                              |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square)                                                                                    |

## Description

<!-- description:start -->

<p>Given two integers <code>n</code> and <code>m</code> (<code>m ≠ 0</code>), the task is to find the number closest to <code>n</code> that is divisible by <code>m</code>. If there is more than one such number, return the one having the <strong>maximum absolute value</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 13, m = 4
<strong>Output:</strong> 12
<strong>Explanation:</strong> 12 is the closest number to 13 which is divisible by 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = -15, m = 6
<strong>Output:</strong> -18
<strong>Explanation:</strong> Both -12 and -18 are closest to -15 and divisible by 6, 
but -18 has the maximum absolute value. So, output is -18.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>-10<sup>5</sup> ≤ n, m ≤ 10<sup>5</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-number-closest-n-divisible-m/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Linear Search)

#### 📝 Intuition

> - Start from n and check outward:
> - Check n, then n-1, then n+1, then n-2, n+2, ... until we find a number divisible by m.
> - If two candidates are equally close, return the one with maximum absolute value.
> - This is simple but inefficient because in the worst case we may need up to |m| checks.

#### 🔍 Algorithm

```pseudo
function bruteForce(n, m):
    for offset in range(0, |m|):
        if (n - offset) % m == 0: return n - offset
        if (n + offset) % m == 0: return n + offset
```

#### 💻 Implementation

```cpp
// Brute force approach using linear search

class Solution {
public:
    int closestNumber(int n, int m) {
        for (int offset = 0; offset <= abs(m); offset++) {
            // Check left side
            if ((n - offset) % m == 0) return n - offset;
            // Check right side
            if ((n + offset) % m == 0) return n + offset;
        }
        return 0; // should never reach here
    }
};
```

### 🥈 Approach 2: Optimized Solution (Floor and Ceil Multiples)

#### 📝 Intuition

> - Compute the nearest multiple of m to n using integer division.
> - Formula:
>   - q = n / m (integer division)
>   - Candidate 1: m \_ q (floor multiple)
>   - Candidate 2: m \_ (q + 1) (ceil multiple)
> - Compare which one is closer. If tie, return the one with maximum absolute value.

#### 🔍 Algorithm

```pseudo
function optimized(n, m):
    q = n // m
    cand1 = m * q
    cand2 = m * (q + 1)
    if abs(n - cand1) < abs(n - cand2): return cand1
    else if abs(n - cand1) > abs(n - cand2): return cand2
    else return the one with max(abs(cand1), abs(cand2))
```

#### 💻 Implementation

```cpp
// Optimized approach using floor and ceil multiples
class Solution {
public:
    int closestNumber(int n, int m) {
        int q = n / m;          // integer division
        int cand1 = m * q;      // multiple just below or equal to n
        int cand2 = m * (q + 1);// multiple just above n

        // Compare distances
        if (abs(n - cand1) < abs(n - cand2)) return cand1;
        else if (abs(n - cand1) > abs(n - cand2)) return cand2;
        else return (abs(cand1) > abs(cand2)) ? cand1 : cand2;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - Instead of computing two candidates, we can directly round n to nearest multiple of m:
> - Formula:
> - res = round(n / m) \* m
> - But since integer division truncates toward zero, we need to carefully handle ties:
> - If distance is equal, pick the one with larger absolute value.
> - This is elegant and efficient.

#### 🔍 Algorithm

```pseudo
function optimal(n, m):
    q = n / m (integer division)
    cand1 = m * q
    cand2 = m * (q + 1)
    return closer one (handle tie with abs value)
```

#### 💻 Implementation

```cpp
// Most optimal solution: direct nearest multiple
class Solution {
public:
    int closestNumber(int n, int m) {
        int q = n / m;              // quotient
        int cand1 = m * q;          // floor multiple
        int cand2 = m * (q + (n * m > 0 ? 1 : -1)); // nearest in correct direction

        // Compare distances
        if (abs(n - cand1) < abs(n - cand2)) return cand1;
        else if (abs(n - cand1) > abs(n - cand2)) return cand2;
        else return (abs(cand1) > abs(cand2)) ? cand1 : cand2;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                              | Cons                                |     |     |     |     |
| -------------- | --------------- | ---------------- | --------------------------------- | ----------------------------------- | --- | --- | --- | --- |
| 🥉 Brute Force | O(m)            | O(1)             | Very simple to implement          | Too slow for large                  |     |     |
| 🥈 Optimized   | O(1)            | O(1)             | Uses math, only two candidates    | Slightly more code than brute force |     |     |     |     |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Clean formula, elegant, efficient | Needs careful tie-breaking logic    |     |     |     |     |

---

<div align="center">

**🎯 Problem 703961 Completed!**

_Happy Coding! 🚀_

</div>
