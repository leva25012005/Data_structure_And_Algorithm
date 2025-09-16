<div align="center">

# 🧠 [1276. Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201276-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                                     |
| **Acceptance Rate** | `50.5%`                                                                                           |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                |

## Description

<!-- description:start -->

<p>Given two integers <code>tomatoSlices</code> and <code>cheeseSlices</code>. The ingredients of different burgers are as follows:</p>

<ul>
	<li><strong>Jumbo Burger:</strong> <code>4</code> tomato slices and <code>1</code> cheese slice.</li>
	<li><strong>Small Burger:</strong> <code>2</code> Tomato slices and <code>1</code> cheese slice.</li>
</ul>

<p>Return <code>[total_jumbo, total_small]</code> so that the number of remaining <code>tomatoSlices</code> equal to <code>0</code> and the number of remaining <code>cheeseSlices</code> equal to <code>0</code>. If it is not possible to make the remaining <code>tomatoSlices</code> and <code>cheeseSlices</code> equal to <code>0</code> return <code>[]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 16, cheeseSlices = 7
<strong>Output:</strong> [1,6]
<strong>Explantion:</strong> To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
There will be no remaining ingredients.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 17, cheeseSlices = 4
<strong>Output:</strong> []
<strong>Explantion:</strong> There will be no way to use all ingredients to make small and jumbo burgers.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tomatoSlices = 4, cheeseSlices = 17
<strong>Output:</strong> []
<strong>Explantion:</strong> Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= tomatoSlices, cheeseSlices &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `16-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `16-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - The simplest idea is to try all possible combinations of jumbo and small burgers.
>   - A jumbo uses 4 tomatoes and 1 cheese.
>   - A small uses 2 tomatoes and 1 cheese.
>   - We can brute force the number of jumbo burgers from 0 to cheeseSlices, then calculate the number of small burgers, and check if tomatoes match.

#### 🔍 Algorithm

```pseudo
for jumbo in range(0, cheeseSlices + 1):
    small = cheeseSlices - jumbo
    if 4*jumbo + 2*small == tomatoSlices:
        return [jumbo, small]
return []
```

#### 💻 Implementation

```cpp
// Brute force solution

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // Try every possible number of jumbo burgers
        for (int jumbo = 0; jumbo <= cheeseSlices; jumbo++) {
            int small = cheeseSlices - jumbo;
            // Check if the tomato condition matches
            if (4 * jumbo + 2 * small == tomatoSlices) {
                return {jumbo, small};
            }
        }
        // No valid combination found
        return {};
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math Equation Solving)

#### 📝 Intuition

> - Instead of brute force, we can use equations:
> - Let x = jumbo, y = small
> - We have:
>   - x + y = cheeseSlices
>   - 4x + 2y = tomatoSlices
> - Solve system of equations:
>   - x = (tomatoSlices - 2\*cheeseSlices) / 2
>   - y = cheeseSlices - x
> - Check if x and y are non-negative integers.

#### 🔍 Algorithm

```pseudo
x = (tomatoSlices - 2*cheeseSlices) / 2
y = cheeseSlices - x
if x >= 0 and y >= 0 and (tomatoSlices - 2*cheeseSlices) % 2 == 0:
    return [x, y]
else:
    return []
```

#### 💻 Implementation

```cpp
// Optimized equation-based solution

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // Solve the equations:
        // 4x + 2y = tomatoSlices
        // x + y = cheeseSlices
        if ((tomatoSlices - 2 * cheeseSlices) % 2 != 0) return {};

        int jumbo = (tomatoSlices - 2 * cheeseSlices) / 2;
        int small = cheeseSlices - jumbo;

        if (jumbo < 0 || small < 0) return {};

        return {jumbo, small};
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - The math-based approach is already optimal, but we can make it cleaner and constant-time by:
>   - Directly validating feasibility: 2*cheeseSlices <= tomatoSlices <= 4*cheeseSlices
>   - Checking if (tomatoSlices % 2 == 0)
>   - Then compute values.
> - This ensures O(1) time and O(1) space.

#### 🔍 Algorithm

```pseudo
if tomatoSlices % 2 != 0 or
   tomatoSlices < 2*cheeseSlices or
   tomatoSlices > 4*cheeseSlices:
    return []
jumbo = (tomatoSlices - 2*cheeseSlices) / 2
small = cheeseSlices - jumbo
return [jumbo, small]
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // Quick feasibility checks
        if (tomatoSlices % 2 != 0 || tomatoSlices < 2 * cheeseSlices || tomatoSlices > 4 * cheeseSlices)
            return {};

        int jumbo = (tomatoSlices - 2 * cheeseSlices) / 2;
        int small = cheeseSlices - jumbo;

        return {jumbo, small};
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity                | Space Complexity | Pros                       | Cons                                                |
| -------------- | ------------------------------ | ---------------- | -------------------------- | --------------------------------------------------- |
| 🥉 Brute Force | O(n) (loop up to cheeseSlices) | O(1)             | Easy to understand, simple | Very slow for large values (cheeseSlices up to 1e7) |
| 🥈 Optimized   | O(1)                           | O(1)             | Uses math, very efficient  | Slightly more math reasoning required               |
| 🥇 Optimal ⭐  | O(1)                           | O(1)             | Clean, elegant, fast       | None                                                |

---

<div align="center">

**🎯 Problem 1276 Completed!**

_Happy Coding! 🚀_

</div>
