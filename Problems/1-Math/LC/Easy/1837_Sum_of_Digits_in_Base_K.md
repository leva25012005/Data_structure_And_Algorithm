<div align="center">

# 🧠 [1837. Sum of Digits in Base K](https://leetcode.com/problems/sum-of-digits-in-base-k/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201837-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/sum-of-digits-in-base-k/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `78.2%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/sum-of-digits-in-base-k/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code> (in base <code>10</code>) and a base <code>k</code>, return <em>the <strong>sum</strong> of the digits of </em><code>n</code><em> <strong>after</strong> converting </em><code>n</code><em> from base </em><code>10</code><em> to base </em><code>k</code>.</p>

<p>After converting, each digit should be interpreted as a base <code>10</code> number, and the sum should be returned in base <code>10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 34, k = 6
<strong>Output:</strong> 9
<strong>Explanation: </strong>34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10, k = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>n is already in base 10. 1 + 0 = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 10</code></li>
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

## 🔗 Related Problems

| Problem                                                                              | Difficulty  | Relationship  |
| ------------------------------------------------------------------------------------ | ----------- | ------------- |
| [ Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Manual Conversion)

#### 📝 Intuition

> - Convert n into base k manually by dividing n repeatedly by k and storing remainders.
> - Once we have the base-k representation, sum up its digits.
> - Straightforward but involves storing digits first.

#### 🔍 Algorithm

```pseudo
function bruteForce(n, k):
    digits = []
    while n > 0:
        digits.append(n % k)
        n = n / k
    sum = 0
    for d in digits:
        sum += d
    return sum
```

#### 💻 Implementation

```cpp
// Brute force approach: convert manually to base-k digits

class Solution {
public:
    int sumBase(int n, int k) {
        vector<int> digits;
        // Convert n into base-k
        while (n > 0) {
            digits.push_back(n % k);
            n /= k;
        }

        // Sum the digits
        int sum = 0;
        for (int d : digits) sum += d;
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Sum On the Fly)

#### 📝 Intuition

> - Instead of storing digits in an array, directly accumulate their sum while computing them.
> - For each step: digit = n % k, add to result, then n /= k.
> - Saves space because we don’t need an array.

#### 🔍 Algorithm

```pseudo
function optimized(n, k):
    result = 0
    while n > 0:
        result += n % k
        n = n / k
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach: accumulate sum directly

class Solution {
public:
    int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            sum += n % k; // Take remainder as a digit
            n /= k;       // Reduce n
        }
        return sum;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical)

#### 📝 Intuition

> - The optimized approach is already O(logₖ(n)), which is optimal since we must process each digit.
> - The only improvement is making it more elegant: a single loop, no extra data structures.
> - For this problem, Approach 2 and Approach 3 have the same complexity, but Approach 3 is the most concise and elegant.

#### 🔍 Algorithm

```pseudo
function optimal(n, k):
    result = 0
    while n > 0:
        result += n % k
        n //= k
    return result
```

#### 💻 Implementation

```cpp
// Most elegant solution (same complexity as optimized)

class Solution {
public:
    int sumBase(int n, int k) {
        int result = 0;
        for (; n > 0; n /= k) {
            result += n % k; // Add each base-k digit
        }
        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                       |
| -------------- | --------------- | ---------------- | ------------------------------------ | -------------------------- |
| 🥉 Brute Force | O(logₖ n)       | O(logₖ n)        | Very clear, explicitly builds digits | Uses extra space           |
| 🥈 Optimized   | O(logₖ n)       | O(1)             | Efficient, avoids extra storage      | Slightly less illustrative |
| 🥇 Optimal ⭐  | O(logₖ n)       | O(1)             | Concise, elegant, minimal code       | Same as optimized in speed |

- Here logₖ n = number of digits of n in base k (at most ~7 since n ≤ 100).

---

<div align="center">

**🎯 Problem 1837 Completed!**

_Happy Coding! 🚀_

</div>
