<div align="center">

# 🧠 [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20172-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/factorial-trailing-zeroes/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                        |
| ------------------- | ---------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                |
| **Acceptance Rate** | `45.2%`                                                                      |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)           |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>the number of trailing zeroes in </em><code>n!</code>.</p>

<p>Note that <code>n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 3! = 6, no trailing zero.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> 5! = 120, one trailing zero.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you write a solution that works in logarithmic time complexity?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                 | Difficulty    | Relationship    |
| ----------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)                                               | 🔴 **Hard**   | Similar logic   |
| [Preimage Size of Factorial Zeroes Function](https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/) | 🔴 **Hard**   | Related concept |
| [Abbreviating the Product of a Range](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)               | 🔴 **Hard**   | Related concept |
| [Maximum Trailing Zeros in a Cornered Path](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/)   | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

### 📊 Low Frequency Companies

- **Google** 📊 20.8%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Compute Factorial Directly)

#### 📝 Intuition

> - Directly compute n!.
> - Convert the result to string (or divide repeatedly) and count trailing zeros.
> - Works only for very small n, because factorial grows extremely fast and will overflow.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    fact = 1
    for i in 2..n:
        fact *= i
    count = 0
    while fact % 10 == 0:
        count += 1
        fact /= 10
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach (only works for very small n due to overflow)

class Solution {
public:
    int trailingZeroesBruteForce(int n) {
        long long fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i; // factorial grows huge very fast
        }

        int count = 0;
        while (fact % 10 == 0) { // count trailing zeroes
            count++;
            fact /= 10;
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution - Factor Counting (Count Factors of 5)

#### 📝 Intuition

> - Each trailing zero comes from a factor of 10 = 2 × 5.
> - Factorials always have more 2s than 5s, so the number of 5s determines the number of zeros.
> - Count how many multiples of 5, 25, 125, … are ≤ n.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    count = 0
    while n > 0:
        n = n // 5
        count += n
    return count
```

#### 💻 Implementation

```cpp
// Optimized approach using factor of 5 counting

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;         // count factors of 5
            count += n;
        }
        return count;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Formula)

#### 📝 Intuition

> - The solution from Approach 2 is already optimal:
> - trailingZeroes(n) = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...
> - This directly gives the number of trailing zeros without computing factorial.
> - Time complexity = O(log₅ n).

#### 🔍 Algorithm

```pseudo
function optimal(n):
    result = sum of floor(n / 5^k) for all k such that 5^k <= n
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        // Keep dividing n by powers of 5
        for (long long p = 5; p <= n; p *= 5) {
            count += n / p;
        }
        return count;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                                 |
| -------------- | --------------- | ---------------- | ------------------------------------ | ------------------------------------ |
| 🥉 Brute Force | O(n)            | O(1)             | Very easy to understand              | Overflows, impossible for n > 20     |
| 🥈 Optimized   | O(log₅ n)       | O(1)             | Efficient, avoids factorial overflow | Requires mathematical observation    |
| 🥇 Optimal ⭐  | O(log₅ n)       | O(1)             | Clean, formula-based, very fast      | Same as Approach 2, but most elegant |

---

<div align="center">

**🎯 Problem 172 Completed!**

_Happy Coding! 🚀_

</div>
