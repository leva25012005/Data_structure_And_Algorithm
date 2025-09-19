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

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - The idea is to try all integers between n - |m| and n + |m| and see which one is divisible by m
> - Then choose the number closest to n. If two numbers are equidistant, choose the one with the larger absolute value.

#### 🔍 Algorithm

```pseudo
function closestNumber(n, m):
    closet ← 0
    minDifference ← ∞

    for i from (n - |m|) to (n + |m|):
        if i % m == 0:
            difference ← |n - i|
            if difference < minDifference OR
               (difference == minDifference AND |i| > |closet|):
                closet ← i
                minDifference ← difference

    return closet
```

#### 💻 Implementation

```cpp
// Brute force approach using linear search
class Solution {
public:
    int closestNumber(int n, int m) {
        int closet = 0;                  // the closet number
        int minDifference = INT_MAX;     // save minumum distance

        // Just check within range [n - |m|, n + |m|]
        for (int i = n - abs(m); i <= n + abs(m); i++) {
            if (i % m == 0) { // kiểm tra số chia hết cho m
                int difference = abs(n - i);
                //Choose the number with the smaller gap or if equal, choose the number larger in absolute value
                if (difference < minDifference ||
                   (difference == minDifference && abs(i) > abs(closet))) {
                    closet = i;
                    minDifference = difference;
                }
            }
        }
        return closet;
    }
};
```

### 🥇 Approach 2: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - Instead of trying each number, we can use the formula directly:
>   - Take the quotient q = n / m.
>   - The closest number can be n1 = m _ q or n2 = m _ (q+1) (or (q-1) if n and m have different signs).
>   - Compare the distance to choose the result.

#### 🔍 Algorithm

```pseudo
function closestNumber(n, m):
    q ← n // m                 # integer division
    n1 ← m * q                 # nearest multiple below

    if n * m > 0:
        n2 ← m * (q + 1)       # same sign → take the upper multiple
    else:
        n2 ← m * (q - 1)       # different signs → take the multiple below

    if |n - n1| < |n - n2|:
        return n1
    else:
        return n2
```

#### 💻 Implementation

```cpp
// Most optimal solution: direct nearest multiple
class Solution {
public:
    int closestNumber(int n, int m) {
        int q = n / m;
        int n1 = m * q;
        int n2 = (n * m) > 0 ? (m * (q + 1)) : (m * (q - 1));

        if (abs(n - n1) < abs(n - n2))
            return n1;
        return n2;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                       | Cons                                  |
| -------------- | --------------- | ---------------- | ------------------------------------------ | ------------------------------------- |
| 🥉 Brute Force | O(abs(m))       | O(1)             | Simple to understand and implement         | Linear in abs(m) — slow if m is large |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Extremely fast — only a few arithmetic ops | Must handle sign cases carefully      |

---

<div align="center">

**🎯 Problem 703961 Completed!**

_Happy Coding! 🚀_

</div>
