<div align="center">

# 🧠 [Overlapping rectangles](https://www.geeksforgeeks.org/problems/overlapping-rectangles1924/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/overlapping-rectangles1924/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `705474`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Accuracy**     | `26.6%`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/overlapping-rectangles1924/1)                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Geometric](https://img.shields.io/badge/-Geometric-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                                                                                                                                                                                                                  |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![Snapdeal](https://img.shields.io/badge/-Snapdeal-orange?style=flat-square) ![Goldman Sachs](https://img.shields.io/badge/-Goldman%20Sachs-orange?style=flat-square) ![OATS Systems](https://img.shields.io/badge/-OATS%20Systems-orange?style=flat-square) ![Expedia](https://img.shields.io/badge/-Expedia-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given two rectangles, check if they overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the <strong>left top corner</strong> and the <strong>right bottom corner</strong>. Two rectangles sharing a side are considered overlapping. (<strong>L1</strong> and <strong>R1</strong> are the extreme points of the first rectangle and <strong>L2</strong> and <strong>R2</strong> are the extreme points of the second rectangle).</p>

<p><strong>Note:</strong> It may be assumed that the rectangles are parallel to the coordinate axis.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> L1=(0,10), R1=(10,0), L2=(5,5), R2=(15,0)
<strong>Output:</strong> 1
<strong>Explanation:</strong> The rectangles overlap.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> L1=(0,2), R1=(1,1), L2=(-2,0), R2=(0,-3)
<strong>Output:</strong> 0
<strong>Explanation:</strong> The rectangles do not overlap.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task:</strong></p>

<p>You don't need to read input or print anything. Complete the function that takes the coordinates of two rectangles and returns <code>1</code> if they overlap, else <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>-10<sup>9</sup> ≤ x-coordinate, y-coordinate ≤ 10<sup>9</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-two-rectangles-overlap/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Bounding Box Check)

#### 📝 Intuition

> - Overlap happens when the rectangles share any area.
> - They do not overlap if:
>   - One rectangle is completely to the left of the other.
>   - One rectangle is completely above the other.
> - If none of these conditions hold, then they overlap.

#### 🔍 Algorithm

```pseudo
function bruteForce(L1, R1, L2, R2):
    if R1.x < L2.x OR R2.x < L1.x:
        return 0   // one is to the left of the other
    if L1.y < R2.y OR L2.y < R1.y:
        return 0   // one is above the other
    return 1
```

#### 💻 Implementation

**C++:**

```cpp
// Brute force check for overlap

class Solution {
public:
    // L1 = top-left of rect1, R1 = bottom-right of rect1
    // L2 = top-left of rect2, R2 = bottom-right of rect2
    int doOverlap(int L1x, int L1y, int R1x, int R1y,
                  int L2x, int L2y, int R2x, int R2y) {

        // Case 1: One rectangle is completely to the left
        if (R1x < L2x || R2x < L1x) return 0;

        // Case 2: One rectangle is completely above the other
        if (L1y < R2y || L2y < R1y) return 0;

        // Otherwise, they overlap
        return 1;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Think in 1D projection:
>   - On the x-axis, two intervals [L1.x, R1.x] and [L2.x, R2.x] must overlap.
>   - On the y-axis, two intervals [R1.y, L1.y] and [R2.y, L2.y] must overlap.
> - If both projections overlap, then rectangles overlap.

#### 🔍 Algorithm

```pseudo
function intervalOverlap(a1, a2, b1, b2):
    return max(a1, b1) <= min(a2, b2)

function optimized(L1, R1, L2, R2):
    xOverlap = intervalOverlap(L1.x, R1.x, L2.x, R2.x)
    yOverlap = intervalOverlap(R1.y, L1.y, R2.y, L2.y)
    return xOverlap AND yOverlap
```

#### 💻 Implementation

```cpp
// Interval overlap approach

class Solution {
public:
    bool intervalsOverlap(int a1, int a2, int b1, int b2) {
        return max(a1, b1) <= min(a2, b2);
    }

    int doOverlap(int L1x, int L1y, int R1x, int R1y,
                  int L2x, int L2y, int R2x, int R2y) {
        // Check overlap on x-axis
        bool xOverlap = intervalsOverlap(L1x, R1x, L2x, R2x);

        // Check overlap on y-axis
        bool yOverlap = intervalsOverlap(R1y, L1y, R2y, L2y);

        return (xOverlap && yOverlap) ? 1 : 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Condition)

#### 📝 Intuition

> - Directly combine both conditions in one statement:
>   - Not overlapping if R1.x < L2.x OR R2.x < L1.x OR L1.y < R2.y OR L2.y < R1.y.
> - Otherwise, they overlap.
> - This is O(1), constant space, one-liner logic.

#### 🔍 Algorithm

```pseudo
function optimal(L1, R1, L2, R2):
    if R1.x < L2.x or R2.x < L1.x or L1.y < R2.y or L2.y < R1.y:
        return 0
    return 1
```

#### 💻 Implementation

```cpp
// Most optimal approach: one-liner condition

class Solution {
public:
    int doOverlap(int L1x, int L1y, int R1x, int R1y,
                  int L2x, int L2y, int R2x, int R2y) {
        // Check the non-overlap cases
        if (R1x < L2x || R2x < L1x || L1y < R2y || L2y < R1y)
            return 0;
        return 1;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                    | Cons                         |
| -------------- | --------------- | ---------------- | --------------------------------------- | ---------------------------- |
| 🥉 Brute Force | O(1)            | O(1)             | Very clear, checks all cases explicitly | Slightly verbose             |
| 🥈 Optimized   | O(1)            | O(1)             | Uses interval overlap intuition         | Needs helper function        |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, minimal conditions            | Less intuitive at first read |

---

<div align="center">

**🎯 Problem 705474 Completed!**

_Happy Coding! 🚀_

</div>
