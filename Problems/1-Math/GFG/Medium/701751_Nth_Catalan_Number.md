<div align="center">

# 🧠 [Nth Catalan Number](https://www.geeksforgeeks.org/problems/nth-catalan-number0817/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/nth-catalan-number0817/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `701751`                                                                                                                                                                                                                                                             |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                        |
| **Accuracy**     | `31.06%`                                                                                                                                                                                                                                                             |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/nth-catalan-number0817/1)                                                                                                                                                                             |
| **Topic Tags**   | ![Dynamic Programming](https://img.shields.io/badge/-Dynamic%20Programming-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square)                                                                                                                                                                                             |

## Description

<!-- description:start -->

<p>Given a number <strong>n</strong>, the task is to find the <strong>n<sup>th</sup> Catalan number</strong>.</p>

<p>The first few Catalan numbers for <strong>n = 0, 1, 2, 3, …</strong> are:</p>
<p><code>1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …</code></p>

<p><strong>Definition:</strong> The Catalan number for <strong>n</strong> is equal to the number of valid expressions containing <strong>n</strong> pairs of parentheses that are correctly matched.  
For example, for each <code>'('</code> there exists a matching <code>')'</code> on the right and vice versa.</p>

<p><strong>Note:</strong> Positions start from 0 as shown above.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> Possible valid expressions are:
((())), (()()), ()(()), (())(), ()()()
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 14
<strong>Explanation:</strong> There are total 14 valid combinations that can be formed using 4 pairs of parentheses.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 19</code></li>
</ul>
## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(n²)</li>
  <li><strong>Auxiliary Space:</strong> O(n)</li>
</ul>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-nth-catalan-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursive Formula)

#### 📝 Intuition

> Catalan numbers follow the recurrence:
>
> $$
> C_0 = 1, \quad
> C_{n+1} = \sum_{i=0}^{n} C_i \cdot C_{n-i}
> $$
>
> Direct recursion computes each Catalan number by splitting into subproblems.
> But this is exponential due to repeated recomputation.

#### 🔍 Algorithm

```pseudo
function catalan(n):
    if n <= 1: return 1
    res = 0
    for i in 0..n-1:
        res += catalan(i) * catalan(n-1-i)
    return res
```

#### 💻 Implementation

```cpp
// Brute force recursive solution

class Solution {
public:
    long long catalanRecursive(int n) {
        if (n <= 1) return 1; // Base cases

        long long res = 0;
        for (int i = 0; i < n; i++) {
            res += catalanRecursive(i) * catalanRecursive(n - 1 - i);
        }
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution - Dynamic Programming (Bottom-Up)

#### 📝 Intuition

> - Use the recurrence but store results to avoid recomputation.
> - Build DP table dp[0..n].
> - Each dp[k] is computed using previously computed values.

#### 🔍 Algorithm

```pseudo
function catalanDP(n):
    dp[0] = dp[1] = 1
    for i in 2..n:
        dp[i] = 0
        for j in 0..i-1:
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]
```

#### 💻 Implementation

```cpp
// DP solution with O(n^2) time

class Solution {
public:
    long long catalanDP(int n) {
        vector<long long> dp(n + 1, 0);
        dp[0] = dp[1] = 1;

        // Build dp table bottom-up
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        return dp[n];
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Closed-Form Formula)

#### 📝 Intuition

> The Catalan number also has a closed-form formula:
>
> $$
> C_n = \frac{1}{n+1} \binom{2n}{n}
> $$
>
> Compute binomial coefficient using the multiplicative formula (to avoid overflow of factorials).
> This is much faster: $O(n)$.

#### 🔍 Algorithm

```pseudo
function catalanClosedForm(n):
    result = binomial(2n, n)
    return result / (n+1)
```

#### 💻 Implementation

```cpp
// Optimal approach using binomial formula

class Solution {
public:
    // Compute binomial coefficient C(n, k)
    long long binomialCoeff(int n, int k) {
        long long res = 1;
        if (k > n - k) k = n - k; // symmetry property
        for (int i = 0; i < k; i++) {
            res *= (n - i);
            res /= (i + 1);
        }
        return res;
    }

    long long catalanClosedForm(int n) {
        long long c = binomialCoeff(2 * n, n);
        return c / (n + 1);
    }
};
```

## 📊 Comparison of Approaches

| Approach          | Time Complexity | Space Complexity | Pros                                   | Cons                            |
| ----------------- | --------------- | ---------------- | -------------------------------------- | ------------------------------- |
| 🥉 Recursive      | Exponential     | O(n)             | Very simple and intuitive              | Too slow for n > 15             |
| 🥈 DP             | O(n²)           | O(n)             | Efficient enough for n ≤ 19            | Requires O(n²) loops            |
| 🥇 Closed Form ⭐ | O(n)            | O(1)             | Fastest, elegant combinatorial formula | Requires handling large numbers |

---

<div align="center">

**🎯 Problem 701751 Completed!**

_Happy Coding! 🚀_

</div>
