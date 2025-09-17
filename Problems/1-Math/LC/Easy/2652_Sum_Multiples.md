<div align="center">

# 🧠 [2652. Sum Multiples](https://leetcode.com/problems/sum-multiples/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202652-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/sum-multiples/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `85.5%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/sum-multiples/)   |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, find the sum of all integers in the range <code>[1, n]</code> <strong>inclusive</strong> that are divisible by <code>3</code>, <code>5</code>, or <code>7</code>.</p>

<p>Return <em>an integer denoting the sum of all numbers in the given range satisfying&nbsp;the constraint.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 21
<strong>Explanation:</strong> Numbers in the range <code>[1, 7]</code> that are divisible by <code>3</code>, <code>5,</code> or <code>7 </code>are <code>3, 5, 6, 7</code>. The sum of these numbers is <code>21</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 40
<strong>Explanation:</strong> Numbers in the range <code>[1, 10] that are</code> divisible by <code>3</code>, <code>5,</code> or <code>7</code> are <code>3, 5, 6, 7, 9, 10</code>. The sum of these numbers is 40.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 30
<strong>Explanation:</strong> Numbers in the range <code>[1, 9]</code> that are divisible by <code>3</code>, <code>5</code>, or <code>7</code> are <code>3, 5, 6, 7, 9</code>. The sum of these numbers is <code>30</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
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

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Loop from 1 to n.
> - For each number, check if it is divisible by 3, 5, or 7.
> - If yes, add it to the result.
> - This is the simplest way, easy to implement.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    result = 0
    for i in 1..n:
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            result += i
    return result
```

#### 💻 Implementation

```cpp
// Brute force solution: O(n)

class Solution {
public:
    int sumOfMultiples(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                res += i; // Add valid numbers
            }
        }
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Instead of iterating, use the sum of multiples formula:
>
> - Sum of multiples of k up to n
>   $$
>   k + 2k + 3k + \dots + m \cdot k = k \cdot \frac{m(m+1)}{2}
>   $$
>   where $m = \lfloor \frac{n}{k} \rfloor$.
> - Apply Inclusion-Exclusion Principle
>   $$
>   S = S(3) + S(5) + S(7) - S(15) - S(21) - S(35) + S(105)
>   $$
>   to avoid double counting.

#### 🔍 Algorithm

```pseudo
function sumMultiples(k, n):
    m = n // k
    return k * m * (m+1) / 2

function optimized(n):
    return sumMultiples(3, n) + sumMultiples(5, n) + sumMultiples(7, n)
         - sumMultiples(15, n) - sumMultiples(21, n) - sumMultiples(35, n)
         + sumMultiples(105, n)
```

#### 💻 Implementation

```cpp
/// Optimized approach: O(1) using formula + inclusion-exclusion

class Solution {
public:
    // Sum of multiples of k up to n
    long long sumMultiples(int k, int n) {
        int m = n / k; // number of terms
        return 1LL * k * m * (m + 1) / 2;
    }

    int sumOfMultiples(int n) {
        long long res = 0;
        res += sumMultiples(3, n);
        res += sumMultiples(5, n);
        res += sumMultiples(7, n);
        res -= sumMultiples(15, n);
        res -= sumMultiples(21, n);
        res -= sumMultiples(35, n);
        res += sumMultiples(105, n);
        return (int)res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Generalize the formula: given a set of divisors {3,5,7}, we compute the sum of multiples using all subsets with inclusion-exclusion.
> This approach scales if the set of divisors changes (e.g., {2,3,5,7}).
> Still O(2^k) where k = number of divisors (here, only 3).

#### 🔍 Algorithm

```pseudo
function sumMultiples(k, n):
    m = n // k
    return k * m * (m+1) / 2

function optimal(n, divisors):
    result = 0
    for each non-empty subset of divisors:
        lcm_val = lcm(all numbers in subset)
        subset_sum = sumMultiples(lcm_val, n)
        if size of subset is odd: result += subset_sum
        else: result -= subset_sum
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and generalized approach with inclusion-exclusion

class Solution {
public:
    // GCD helper
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    // LCM helper
    int lcm(int a, int b) {
        return a / gcd(a, b) * b;
    }

    // Sum of multiples of k up to n
    long long sumMultiples(int k, int n) {
        int m = n / k;
        return 1LL * k * m * (m + 1) / 2;
    }

    int sumOfMultiples(int n) {
        vector<int> divisors = {3, 5, 7};
        long long res = 0;

        int m = divisors.size();
        // Iterate through all non-empty subsets of divisors
        for (int mask = 1; mask < (1 << m); mask++) {
            int lcm_val = 1;
            int bits = 0;
            for (int i = 0; i < m; i++) {
                if (mask & (1 << i)) {
                    lcm_val = lcm(lcm_val, divisors[i]);
                    bits++;
                }
            }
            long long s = sumMultiples(lcm_val, n);
            if (bits % 2 == 1) res += s; // odd subset -> add
            else res -= s;               // even subset -> subtract
        }

        return (int)res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                   | Cons                             |
| -------------- | --------------- | ---------------- | -------------------------------------- | -------------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very easy to implement                 | Slow for large n (but fine here) |
| 🥈 Optimized   | O(1)            | O(1)             | Uses arithmetic progression, very fast | Hardcoded for {3,5,7}            |
| 🥇 Optimal ⭐  | O(2^k) for k=3  | O(1)             | Generalized, works for any divisor set | More code, overhead for small k  |

---

<div align="center">

**🎯 Problem 2652 Completed!**

_Happy Coding! 🚀_

</div>
