<div align="center">

# 🧠 [Euler Totient Function](https://www.geeksforgeeks.org/problems/euler-totient-function4604/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/euler-totient-function4604/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704399`                                                                                                                                                          |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                       |
| **Accuracy**     | `32.11%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/euler-totient-function4604/1)                                                                      |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Cisco](https://img.shields.io/badge/-Cisco-orange?style=flat-square)                                                                                            |

## Description

<!-- description:start -->

<p>Find the <strong>Euler Totient Function (ETF)</strong> Φ(n) for a given integer <strong>n</strong>.</p>

<p><strong>ETF</strong> is the count of numbers in {1, 2, 3, …, n} that are relatively prime to <strong>n</strong>, i.e., the numbers whose <strong>GCD</strong> (Greatest Common Divisor) with <strong>n</strong> is 1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> 10
<strong>Explanation:</strong> From 1 to 11, the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 are relatively prime to 11.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> 8
<strong>Explanation:</strong> From 1 to 16, the numbers 1, 3, 5, 7, 9, 11, 13, 15 are relatively prime to 16.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 ≤ n ≤ 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(sqrt(n))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/eulers-totient-function/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check GCD)

#### 📝 Intuition

> - Euler’s Totient Function counts numbers from 1 to n that are coprime with n.
> - Simplest approach: iterate through all numbers from 1 to n and check gcd(i, n) == 1.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    count = 0
    for i in 1..n:
        if gcd(i, n) == 1:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach using GCD

class Solution {
public:
    // Compute GCD using Euclid's algorithm
    int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    int phiBruteForce(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (gcd(i, n) == 1) count++; // Count numbers coprime with n
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Prime Factorization)

#### 📝 Intuition

> Euler Totient Function can be calculated as:
>
> $$
> \phi(n) = n \cdot \prod_{p \mid n} \left( 1 - \frac{1}{p} \right)
> $$
>
> where $p$ runs over distinct prime factors of $n$.
>
> Factorize $n$ and apply the formula. Faster than brute force.

#### 🔍 Algorithm

```pseudo
function phiFactorization(n):
    result = n
    for i = 2 to sqrt(n):
        if i divides n:
            while i divides n:
                n /= i
            result = result * (1 - 1/i)
    if n > 1:
        result = result * (1 - 1/n)  // remaining prime factor
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach using prime factorization

class Solution {
public:
    int phiFactorization(int n) {
        long long result = n;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {         // i is a prime factor
                while (n % i == 0) n /= i; // remove all occurrences
                result = result / i * (i - 1); // apply formula
            }
        }

        if (n > 1) result = result / n * (n - 1); // remaining prime factor
        return (int)result;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Multiple Queries)

#### 📝 Intuition

> - If you need ETF for multiple numbers, precompute ETF using a modified Sieve of Eratosthenes.
> - Initialize phi[i] = i, then for each prime p, update multiples: phi[j] = phi[j] / p \* (p-1).
> - Extremely fast for 1 ≤ n ≤ 10^5 and multiple queries.

#### 🔍 Algorithm

```pseudo
function sievePhi(n):
    phi = array[0..n] initialized as phi[i] = i
    for i = 2..n:
        if phi[i] == i: // i is prime
            for j = i..n step i:
                phi[j] = phi[j] / i * (i - 1)
    return phi
```

#### 💻 Implementation

```cpp
// Optimal solution using Sieve for multiple ETF queries

class Solution {
public:
    vector<int> sievePhi(int n) {
        vector<int> phi(n + 1);
        for (int i = 0; i <= n; i++) phi[i] = i;

        for (int i = 2; i <= n; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= n; j += i) {
                    phi[j] = phi[j] / i * (i - 1);
                }
            }
        }
        return phi;
    }
};
```

## 📊 Comparison of Approaches

| Approach         | Time Complexity | Space Complexity | Pros                                    | Cons                     |
| ---------------- | --------------- | ---------------- | --------------------------------------- | ------------------------ |
| 🥉 Brute Force   | O(n log n)      | O(1)             | Very simple, easy to implement          | Slow for large n         |
| 🥈 Factorization | O(√n)           | O(1)             | Fast for single queries, constant space | Need factorization logic |
| 🥇 Sieve ⭐      | O(n log log n)  | O(n)             | Extremely fast for multiple queries     | Extra O(n) space         |

---

<div align="center">

**🎯 Problem 704399 Completed!**

_Happy Coding! 🚀_

</div>
