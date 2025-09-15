<div align="center">

# 🧠 [507. Perfect Number](https://leetcode.com/problems/perfect-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20507-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/perfect-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `45.7%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/perfect-number/)  |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank"><strong>perfect number</strong></a> is a <strong>positive integer</strong> that is equal to the sum of its <strong>positive divisors</strong>, excluding the number itself. A <strong>divisor</strong> of an integer <code>x</code> is an integer that can divide <code>x</code> evenly.</p>

<p>Given an integer <code>n</code>, return <code>true</code><em> if </em><code>n</code><em> is a perfect number, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 28
<strong>Output:</strong> true
<strong>Explanation:</strong> 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
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

| Problem                                                                       | Difficulty  | Relationship  |
| ----------------------------------------------------------------------------- | ----------- | ------------- |
| [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | 🟢 **Easy** | Similar logic |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Grammarly** ⭐ 76.5%

### 📈 Regular Frequency (40-59%)

- **Accenture** 📈 48.3%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - A perfect number = sum of its proper divisors equals the number itself.
> - Check all numbers from 1 to num-1.
> - Add up those that divide num.
> - Compare with num.
> - This works but is too slow for large num (up to 10^8).

#### 🔍 Algorithm

```pseudo
function bruteForce(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num
```

#### 💻 Implementation

```cpp
// Brute force approach (inefficient for large num)

class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false; // Perfect numbers are > 1
        int sum = 0;
        // Check all divisors less than num
        for (int i = 1; i < num; i++) {
            if (num % i == 0) sum += i;
        }
        return sum == num;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - We don’t need to check all numbers up to num-1.
> - A divisor d always comes with a pair num/d.
> - We only need to iterate up to sqrt(num).
> - For each divisor i, add both i and num/i.
> - Don’t forget to exclude the number itself.
> - Much faster than brute force.

#### 🔍 Algorithm

```pseudo
function optimized(num):
    if num <= 1: return false
    sum = 1  // 1 is always a divisor
    for i in range(2, sqrt(num)):
        if num % i == 0:
            sum += i
            if i != num/i:
                sum += num/i
    return sum == num
```

#### 💻 Implementation

```cpp
/// Optimized divisor check using sqrt

class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1) return false;

        int sum = 1; // 1 is always a divisor
        // Only check up to sqrt(num)
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                sum += i;
                if (i != num / i) sum += num / i; // Add divisor pair
            }
        }
        return sum == num;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - It’s known from number theory that all even perfect numbers have the form:
> - 2^(p-1) \* (2^p - 1)
> - where (2^p - 1) is a Mersenne prime.
> - Within the problem’s constraint (num ≤ 10^8), only a few perfect numbers ex- ist:
> - {6, 28, 496, 8128, 33550336}.
> - So we can just check if num is in this set.
> - This is the fastest solution (O(1)).

#### 🔍 Algorithm

```pseudo
function optimal(num):
    perfect_set = {6, 28, 496, 8128, 33550336}
    return num in perfect_set
```

#### 💻 Implementation

```cpp
// Most optimal solution using known perfect numbers

class Solution {
public:
    bool checkPerfectNumber(int num) {
        // Precomputed perfect numbers under 1e8
        static unordered_set<int> perfects = {6, 28, 496, 8128, 33550336};
        return perfects.count(num) > 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                             | Cons                            |
| -------------- | --------------- | ---------------- | -------------------------------- | ------------------------------- |
| 🥉 Brute Force | O(num)          | O(1)             | Very easy to understand          | Too slow for `num` up to 10^8   |
| 🥈 Optimized   | O(√num)         | O(1)             | Efficient, works for all inputs  | Still not constant time         |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Instant lookup, fastest solution | Relies on precomputed knowledge |

---

<div align="center">

**🎯 Problem 507 Completed!**

_Happy Coding! 🚀_

</div>
