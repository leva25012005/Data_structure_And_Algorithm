<div align="center">

# 🧠 [1780. Check if Number is a Sum of Powers of Three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201780-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                                  |
| **Acceptance Rate** | `79.3%`                                                                                        |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                             |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <code>true</code> <em>if it is possible to represent </em><code>n</code><em> as the sum of distinct powers of three.</em> Otherwise, return <code>false</code>.</p>

<p>An integer <code>y</code> is a power of three if there exists an integer <code>x</code> such that <code>y == 3<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> true
<strong>Explanation:</strong> 12 = 3<sup>1</sup> + 3<sup>2</sup>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 91
<strong>Output:</strong> true
<strong>Explanation:</strong> 91 = 3<sup>0</sup> + 3<sup>2</sup> + 3<sup>4</sup>
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 21
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>7</sup></code></li>
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

## 🔗 Related Problems

| Problem                                                         | Difficulty  | Relationship  |
| --------------------------------------------------------------- | ----------- | ------------- |
| [Power of Three](https://leetcode.com/problems/power-of-three/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Subset Enumeration)

#### 📝 Intuition

> - Generate all possible subsets of powers of 3 that are ≤ n.
> - Check if any subset sums to exactly n.
> - This is brute force and not efficient for larger n, but works conceptually

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    powers = generate all powers of 3 ≤ n
    for each subset of powers:
        if sum(subset) == n:
            return true
    return false
```

#### 💻 Implementation

```cpp
// Brute force approach (Exponential time, not feasible for large n)

class Solution {
public:
    bool checkPowersOfThree(int n) {
        vector<int> powers;
        // Generate all powers of 3 ≤ n
        for (long long p = 1; p <= n; p *= 3) {
            powers.push_back(p);
        }

        int m = powers.size();
        // Try all subsets (2^m possibilities)
        for (int mask = 0; mask < (1 << m); mask++) {
            long long sum = 0;
            for (int i = 0; i < m; i++) {
                if (mask & (1 << i)) sum += powers[i];
            }
            if (sum == n) return true;
        }
        return false;
    }
};
```

### 🥈 Approach 2: Optimized Solution - Greedy (Subtract Largest Power)

#### 📝 Intuition

> - Similar to "coin change" greedy strategy.
> - Start from the largest power of 3 ≤ n.
> - Subtract it from n if possible, then continue with smaller powers.
> - If we can reduce n to 0, return true.
> - Works because we must use each power of 3 at most once.

🔍 Algorithm

#### 🔍 Algorithm

```pseudo
function greedy(n):
    while n > 0:
        find largest power of 3 ≤ n
        subtract it from n
    return true if n == 0 else false
```

#### 💻 Implementation

```cpp
// Optimized approach with better complexity

class Solution {
public:
    bool checkPowersOfThree(int n) {
        // Generate all powers of 3 up to n
        vector<int> powers;
        for (long long p = 1; p <= n; p *= 3) {
            powers.push_back(p);
        }

        // Start from largest power and subtract
        for (int i = powers.size() - 1; i >= 0; i--) {
            if (n >= powers[i]) {
                n -= powers[i];
            }
        }
        return n == 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Base-3 Representation)

#### 📝 Intuition

> - Every integer can be expressed in base 3.
> - If a number can be represented as a sum of distinct powers of 3, then its base-3 representation contains only digits 0 or 1 (never 2).
> - So we just need to check the ternary representation of n.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    while n > 0:
        if n % 3 == 2: return false
        n = n / 3
    return true
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool checkPowersOfThree(int n) {
        // Check ternary representation
        while (n > 0) {
            if (n % 3 == 2) return false; // If digit "2" appears -> not possible
            n /= 3;
        }
        return true;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity     | Space Complexity | Pros                                    | Cons                                 |
| -------------- | ------------------- | ---------------- | --------------------------------------- | ------------------------------------ |
| 🥉 Brute Force | O(2^log₃n \* log₃n) | O(log₃n)         | Very intuitive, tries all possibilities | Exponential → infeasible for n large |
| 🥈 Greedy      | O(log₃n)            | O(log₃n)         | Simple, works well                      | Less elegant than base-3 check       |
| 🥇 Optimal ⭐  | O(log₃n)            | O(1)             | Fastest, elegant base-3 trick           | Requires insight into base-3         |

---

<div align="center">

**🎯 Problem 1780 Completed!**

_Happy Coding! 🚀_

</div>
