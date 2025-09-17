<div align="center">

# 🧠 [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201317-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                                           |
| **Acceptance Rate** | `54.3%`                                                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                    |

## Description

<!-- description:start -->

<p><strong>No-Zero integer</strong> is a positive integer that <strong>does not contain any <code>0</code></strong> in its decimal representation.</p>

<p>Given an integer <code>n</code>, return <em>a list of two integers</em> <code>[a, b]</code> <em>where</em>:</p>

<ul>
	<li><code>a</code> and <code>b</code> are <strong>No-Zero integers</strong>.</li>
	<li><code>a + b = n</code></li>
</ul>

<p>The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [1,1]
<strong>Explanation:</strong> Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> [2,9]
<strong>Explanation:</strong> Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Hudson River Trading** 🔥 97.8%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Iterate through all numbers a from 1 to n-1.
> - Let b = n - a.
> - Check if both a and b are No-Zero integers (i.e., they don’t contain digit 0).
> - Return the first valid pair.
> - This works because the constraint n ≤ 10^4 is small.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    for a from 1 to n-1:
        b = n - a
        if isNoZero(a) and isNoZero(b):
            return [a, b]
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    // Helper to check if a number is a No-Zero integer
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false; // Contains 0
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        // Try all possible splits
        for (int a = 1; a < n; a++) {
            int b = n - a;
            if (isNoZero(a) && isNoZero(b)) {
                return {a, b}; // Return the first valid pair
            }
        }
        return {}; // Should never reach here because a solution is guaranteed
    }
};
```

### 🥈 Approach 2: Optimized Solution - Greedy (Constructive)

#### 📝 Intuition

> - Start with a = 1, b = n - 1.
> - If either a or b contains 0, increment a and decrement b.
> - Continue until both are valid.
> - This avoids checking all pairs from scratch.

#### 🔍 Algorithm

```pseudo
function greedy(n):
    a = 1
    b = n - 1
    while not (isNoZero(a) and isNoZero(b)):
        a += 1
        b -= 1
    return [a, b]
```

#### 💻 Implementation

```cpp
// Greedy constructive approach

class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        int a = 1, b = n - 1;
        // Adjust until both numbers are valid
        while (!isNoZero(a) || !isNoZero(b)) {
            a++;
            b--;
        }
        return {a, b};
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Instead of trial and error, we can construct directly.
> - Start with a = n / 2, b = n - a.
> - If either contains zero, adjust slightly until both are valid.
> - Because n ≤ 10^4, the adjustment will be very fast.
> - This minimizes unnecessary scanning.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    a = n // 2
    b = n - a
    while not (isNoZero(a) and isNoZero(b)):
        a += 1
        b -= 1
    return [a, b]
```

#### 💻 Implementation

```cpp
// Optimal and elegant solution

class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }

    vector<int> getNoZeroIntegers(int n) {
        // Start with a balanced split
        int a = n / 2;
        int b = n - a;

        // Adjust until valid
        while (!isNoZero(a) || !isNoZero(b)) {
            a++;
            b--;
        }
        return {a, b};
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                        |
| -------------- | --------------- | ---------------- | ------------------------------- | --------------------------- |
| 🥉 Brute Force | O(n \* d)       | O(1)             | Very easy to implement          | Inefficient for larger `n`  |
| 🥈 Greedy      | O(k \* d)       | O(1)             | Faster, adjusts incrementally   | Still needs multiple checks |
| 🥇 Optimal ⭐  | O(k \* d)       | O(1)             | Elegant, starts near the middle | Slightly trickier logic     |

---

<div align="center">

**🎯 Problem 1317 Completed!**

_Happy Coding! 🚀_

</div>
