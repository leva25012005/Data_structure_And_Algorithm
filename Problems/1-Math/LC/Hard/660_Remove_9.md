<div align="center">

# 🧠 [660. Remove 9](https://leetcode.com/problems/remove-9/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20660-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/remove-9/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🔴 **Hard**                                                        |
| **Acceptance Rate** | `57.4%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/remove-9/)        |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Start from integer <code>1</code>, remove any integer that contains <code>9</code> such as <code>9</code>, <code>19</code>, <code>29</code>...</p>

<p>Now, you will have a new integer sequence <code>[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...]</code>.</p>

<p>Given an integer <code>n</code>, return <em>the</em> <code>n<sup>th</sup></code> (<strong>1-indexed</strong>) integer in the new sequence.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 10
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 11
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8 * 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Houzz** 🔥 100.0%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Start from 1 and keep generating numbers.
> - Skip any number that contains digit 9.
> - Keep a counter until we reach the nth valid number.
> - This is straightforward but too slow for large n (up to 8 \* 10^8).

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if num contains digit '9': continue
        count += 1
    return num
```

#### 💻 Implementation

```cpp
// Brute force solution (not feasible for large n)

class Solution {
public:
    bool hasNine(int x) {
        while (x > 0) {
            if (x % 10 == 9) return true;
            x /= 10;
        }
        return false;
    }

    int newIntegerBruteForce(int n) {
        int count = 0;
        int num = 0;
        while (count < n) {
            num++;
            if (!hasNine(num)) count++;
        }
        return num;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Base Conversion Idea)

#### 📝 Intuition

> - Notice that the sequence without digit 9 looks like base-9 numbers written in decimal.
> - Example:
>   - Sequence: 1,2,3,4,5,6,7,8,10,...
>   - Base-9: 1,2,3,4,5,6,7,8,10,...
> - So the nth number = just write n in base-9 and interpret it as decimal.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    result = 0
    place = 1
    while n > 0:
        digit = n % 9
        result += digit * place
        place *= 10
        n //= 9
    return result
```

#### 💻 Implementation

```cpp
// Optimized solution using base-9 conversion

class Solution {
public:
    int newIntegerOptimized(int n) {
        int res = 0, place = 1;
        while (n > 0) {
            int digit = n % 9;      // Get base-9 digit
            res += digit * place;   // Place it in decimal position
            place *= 10;
            n /= 9;
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Conversion)

#### 📝 Intuition

> - Approach 2 is already optimal in O(log₉ n).
> - This is the cleanest form:
>   - Directly compute base-9 representation.
>   - No need to store digits, just accumulate.
> - This works efficiently for n up to 8 \* 10^8.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    ans = 0
    base = 1
    while n > 0:
        ans += (n % 9) * base
        n //= 9
        base *= 10
    return ans
```

#### 💻 Implementation

```cpp
// Most optimal solution (base-9 trick)

class Solution {
public:
    int newInteger(int n) {
        int ans = 0, base = 1;
        while (n > 0) {
            ans += (n % 9) * base; // Add base-9 digit
            n /= 9;                // Move to next digit
            base *= 10;            // Shift decimal place
        }
        return ans;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                               | Cons                              |
| -------------- | --------------- | ---------------- | ---------------------------------- | --------------------------------- |
| 🥉 Brute Force | O(n \* log n)   | O(1)             | Very intuitive                     | Impossible for large `n`          |
| 🥈 Optimized   | O(log₉ n)       | O(1)             | Uses mathematical insight (base-9) | Slightly less intuitive           |
| 🥇 Optimal ⭐  | O(log₉ n)       | O(1)             | Elegant, fastest, memory-efficient | Requires recognizing base-9 trick |

---

<div align="center">

**🎯 Problem 660 Completed!**

_Happy Coding! 🚀_

</div>
