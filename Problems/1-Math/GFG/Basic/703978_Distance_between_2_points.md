<div align="center">

# 🧠 [Distance between 2 points](https://www.geeksforgeeks.org/problems/distance-between-2-points3200/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/distance-between-2-points3200/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703978`                                                                                                                                                                                                                                       |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                   |
| **Accuracy**     | `49.98%`                                                                                                                                                                                                                                       |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/distance-between-2-points3200/1)                                                                                                                                                |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Geometric](https://img.shields.io/badge/-Geometric-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Zoho](https://img.shields.io/badge/-Zoho-orange?style=flat-square)                                                                                                                                                                           |

## Description

<!-- description:start -->

<p>Given coordinates of two points on a Cartesian plane, find the distance between them rounded up to the nearest integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x1 = 0, y1 = 0, x2 = 2, y2 = -2
<strong>Output:</strong> 3
<strong>Explanation:</strong> Distance between (0, 0) and (2, -2) is sqrt((2-0)^2 + (-2-0)^2) = sqrt(8) ≈ 2.82, rounded up to 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x1 = -20, y1 = 23, x2 = -15, y2 = 68
<strong>Output:</strong> 45
<strong>Explanation:</strong> Distance between (-20, 23) and (-15, 68) is sqrt((−15+20)^2 + (68−23)^2) = sqrt(25 + 2025) = sqrt(2050) ≈ 45.27, rounded up to 45.
</pre>

<p>&nbsp;</p>
<strong>Your Task:</strong>  
You don't need to read or print anything. Your task is to complete the function <code>distance(x1, y1, x2, y2)</code> which returns the distance between the given two points.

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>-1000 &lt;= x1, y1, x2, y2 &lt;= 1000</code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-calculate-distance-two-points/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Direct Formula)

#### 📝 Intuition

> - Use the standard Euclidean distance formula:
>
> $$
> distance = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
> $$
>
> - Round up the result to the nearest integer.
> - Simple, straightforward, works for all inputs.

#### 🔍 Algorithm

```pseudo
function distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dist = sqrt(dx^2 + dy^2)
    return ceil(dist)
```

#### 💻 Implementation

```cpp
#include <cmath> // for sqrt and ceil

class Solution {
public:
    int distance(int x1, int y1, int x2, int y2) {
        // Step 1: Calculate differences
        int dx = x2 - x1;
        int dy = y2 - y1;

        // Step 2: Compute Euclidean distance
        double dist = sqrt(dx * dx + dy * dy);

        // Step 3: Round up to nearest integer
        return (int)ceil(dist);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Avoid Extra Variables)

#### 📝 Intuition

> - We can compute the distance directly inside the sqrt function without storing intermediate dx and dy.
> - Same formula, slightly more concise.

#### 🔍 Algorithm

```pseudo
function distance(x1, y1, x2, y2):
    return ceil(sqrt((x2 - x1)^2 + (y2 - y1)^2))
```

#### 💻 Implementation

**C++:**

```cpp
#include <cmath>

class Solution {
public:
    int distance(int x1, int y1, int x2, int y2) {
        // Directly compute distance without extra variables
        return (int)ceil(sqrt((x2 - x1) * (x2 - x1) +
                              (y2 - y1) * (y2 - y1)));
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (One-liner using pow)

#### 📝 Intuition

> - Use pow(a, 2) instead of a \* a for clarity.
> - Still O(1) time and O(1) space, very elegant one-liner.

#### 🔍 Algorithm

```pseudo
function distance(x1, y1, x2, y2):
    return ceil(sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)))
```

#### 💻 Implementation

```cpp
#include <cmath>

class Solution {
public:
    int distance(int x1, int y1, int x2, int y2) {
        // Elegant one-liner using pow
        return (int)ceil(sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)));
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                     |
| -------------- | --------------- | ---------------- | ----------------------------- | ------------------------ |
| 🥉 Brute Force | O(1)            | O(1)             | Very clear and easy to follow | Uses extra variables     |
| 🥈 Optimized   | O(1)            | O(1)             | Concise, no extra variables   | Slightly less readable   |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant, one-liner            | Relies on `pow` function |

---

<div align="center">

**🎯 Problem 703978 Completed!**

_Happy Coding! 🚀_

</div>
