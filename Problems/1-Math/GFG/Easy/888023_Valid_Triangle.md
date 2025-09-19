<div align="center">

# 🧠 [Valid Triangle](https://www.geeksforgeeks.org/problems/valid-triangle--121441/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/valid-triangle--121441/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------- |
| **Problem ID**   | `888023`                                                                                 |
| **Difficulty**   | 🟢 **Easy**                                                                              |
| **Accuracy**     | `45.57%`                                                                                 |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/valid-triangle--121441/1) |

## Description

<!-- description:start -->

<p>Given the three sides of a triangle <strong>a</strong>, <strong>b</strong>, and <strong>c</strong>, check whether the triangle is valid or not.</p>
<p>A triangle is valid if the sum of any two sides is strictly greater than the third side.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> a = 8, b = 15, c = 17
<strong>Output:</strong> Valid
<strong>Explanation:</strong> 8 + 15 > 17, 8 + 17 > 15, and 15 + 17 > 8.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> a = 3, b = 6, c = 9
<strong>Output:</strong> Invalid
<strong>Explanation:</strong> 3 + 6 is not greater than 9, so the triangle is not valid.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ a, b, c ≤ 10⁶</code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-whether-triangle-valid-not-sides-given/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Direct Condition Checking)

#### 📝 Intuition

> - A triangle is valid if it satisfies the Triangle Inequality Theorem:
>   - a + b > c
>   - a + c > b
>   - b + c > a
> - Simply check all three conditions.
> - This is the most direct and simple solution.

#### 🔍 Algorithm

```pseudo
function bruteForce(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "Valid"
    else:
        return "Invalid"
```

#### 💻 Implementation

```cpp
// Brute force approach: direct condition checks

class Solution {
public:
    string checkTriangle(int a, int b, int c) {
        // Check triangle inequality theorem
        if (a + b > c && a + c > b && b + c > a) {
            return "Valid";
        }
        return "Invalid";
    }
};
```

### 🥈 Approach 2: Optimized Solution (Sorting)

#### 📝 Intuition

> - Instead of checking all three inequalities, sort the sides: x ≤ y ≤ z.
> - Then we only need to check x + y > z.
> - If true → valid triangle; otherwise invalid.
> - Because the largest side z will always be the strictest inequality.

#### 🔍 Algorithm

```pseudo
function optimized(a, b, c):
    sides = sort([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        return "Valid"
    else:
        return "Invalid"
```

#### 💻 Implementation

```cpp
// Optimized solution using sorting

class Solution {
public:
    string checkTriangle(int a, int b, int c) {
        vector<int> sides = {a, b, c};
        sort(sides.begin(), sides.end()); // Sort sides in ascending order

        // Only need to check the largest side
        if (sides[0] + sides[1] > sides[2]) {
            return "Valid";
        }
        return "Invalid";
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Insight)

#### 📝 Intuition

> - The largest side must be strictly less than the sum of the other two sides.
> - Without sorting, we can find the max side maxSide and compare with (sum - maxSide).
> - If maxSide < sum - maxSide → Valid.
> - This avoids sorting (O(1)) and is the most elegant.

#### 🔍 Algorithm

```pseudo
function optimal(a, b, c):
    sum = a + b + c
    maxSide = max(a, b, c)
    if maxSide < sum - maxSide:
        return "Valid"
    else:
        return "Invalid"
```

#### 💻 Implementation

```cpp
// Most optimal approach: O(1) check with max side

class Solution {
public:
    string checkTriangle(int a, int b, int c) {
        int sum = a + b + c;
        int maxSide = max({a, b, c});

        // Valid if largest side < sum of other two
        if (maxSide < sum - maxSide) {
            return "Valid";
        }
        return "Invalid";
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                    | Cons                           |
| -------------- | --------------- | ---------------- | --------------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(1)            | O(1)             | Very simple, directly checks conditions | Slightly repetitive conditions |
| 🥈 Optimized   | O(log 3) ≈ O(1) | O(1)             | Cleaner (only one check needed)         | Requires sorting step          |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Most elegant, uses math insight         | Needs careful handling of max  |

---

<div align="center">

**🎯 Problem 888023 Completed!**

_Happy Coding! 🚀_

</div>
