<div align="center">

# 🧠 [Power of k in factorial of n](https://www.geeksforgeeks.org/problems/power-of-k-in-n-where-k-may-be-non-prime4206/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/power-of-k-in-n-where-k-may-be-non-prime4206/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `705234`                                                                                                                                                                                                                                               |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                          |
| **Accuracy**     | `51.2%`                                                                                                                                                                                                                                                |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/power-of-k-in-n-where-k-may-be-non-prime4206/1)                                                                                                                                         |
| **Topic Tags**   | ![number-theory](https://img.shields.io/badge/-number-theory-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given two positive integers <strong>n</strong> and <strong>k</strong>, determine the highest value of <strong>x</strong> such that <strong>k<sup>x</sup></strong> <strong>divides <code>n! (n factorial)</code> completely</strong> (i.e., <code>n! % (k<sup>x</sup>) == 0</code>).</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 7, k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> 7! = 5040, and 2^4 = 16 is the highest power of 2 that divides 5040.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 10, k = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> 10! = 3628800, and 9^2 = 81 is the highest power of 9 that divides 3628800.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 10<sup>5</sup></code></li>
  <li><code>2 ≤ k ≤ 10<sup>5</sup></code></li>
</ul>

## Expected Complexity

<p><strong>Expected Time Complexity:</strong> O(sqrt(k) + m * log n), where m = number of distinct prime factors in k<br>
<strong>Expected Auxiliary Space:</strong> O(m), where m = number of distinct prime factors in k</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `19-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `19-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/largest-power-k-n-factorial-k-may-not-prime/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Factorial Computation)

#### 📝 Intuition

> - Compute n! directly.
> - Keep dividing by k until it no longer divides n!.
> - This gives the highest power x.
> - ⚠️ Problem: This approach fails for large n because n! is huge (overflow).

#### 🔍 Algorithm

```pseudo
function bruteForce(n, k):
    fact = 1
    for i = 1 to n:
        fact *= i
    x = 0
    while fact % k == 0:
        fact /= k
        x += 1
    return x
```

#### 💻 Implementation

```cpp
// Brute force approach (not feasible for large n)

class Solution {
public:
    int highestPower(int n, int k) {
        long long fact = 1;
        // Compute factorial (overflow occurs for large n)
        for (int i = 1; i <= n; i++) fact *= i;

        int x = 0;
        // Divide by k until it no longer divides
        while (fact % k == 0) {
            fact /= k;
            x++;
        }
        return x;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Prime Factorization of k)

#### 📝 Intuition

> Factorize $k$ into primes:
>
> - $$
> - k = p_1^{a_1} \cdot p_2^{a_2} \cdot \dots \cdot p_m^{a_m}
> - $$
>   $$
>
> - For each prime $p_i$, calculate its exponent in $n!$ using:
>
> - $$
> - \text{count}_{p_i} = \sum_{j=1}^{\infty} \left\lfloor \frac{n}{p_i^j} \right\rfloor
> - $$
>   $$
>
> - The maximum $x$ such that $k^x \mid n!$ is:
>
> - $$
> - x = \min \left( \frac{\text{count}_{p_1}}{a_1}, \frac{\text{count}_{p*2}}{a_2}, \dots, \frac{\text{count}*{p_m}}{a_m} \right)
> - $$
>   $$
>
> - This approach avoids computing large factorials.

#### 🔍 Algorithm

```pseudo
function optimized(n, k):
    prime_factors = factorize(k) // returns {pi: ai}
    x = infinity
    for each (pi, ai) in prime_factors:
        count = 0
        p = pi
        while p <= n:
            count += n // p
            p *= pi
        x = min(x, count // ai)
    return x
```

#### 💻 Implementation

```cpp
// Optimized using prime factorization of k

class Solution {
public:
    int highestPower(int n, int k) {
        int res = INT_MAX;

        // Factorize k
        for (int i = 2; i * i <= k; i++) {
            if (k % i == 0) {
                int countK = 0;
                while (k % i == 0) {
                    k /= i;
                    countK++;
                }

                // Count exponent of i in n!
                long long countN = 0, p = i;
                while (p <= n) {
                    countN += n / p;
                    p *= i;
                }

                res = min(res, (int)(countN / countK));
            }
        }

        if (k > 1) { // k itself is prime
            long long countN = 0, p = k;
            while (p <= n) {
                countN += n / p;
                p *= k;
            }
            res = min(res, (int)countN);
        }

        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Same as Approach 2, but written cleanly:
>   - Factorize k efficiently.
>   - Compute exponents in n! directly.
>   - Take minimum over all prime factors.
> - Time complexity: O(sqrt(k) + m \* log n) where m = number of distinct primes in k.

#### 🔍 Algorithm

```pseudo
function optimal(n, k):
    factors = prime factorization of k
    result = infinity
    for each prime, exponent in factors:
        count = sum_{j=1 to ∞} floor(n / prime^j)
        result = min(result, count // exponent)
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int highestPower(int n, int k) {
        int res = INT_MAX;
        int originalK = k;

        // Step 1: Factorize k
        for (int i = 2; i * i <= originalK; i++) {
            if (k % i == 0) {
                int expK = 0;
                while (k % i == 0) {
                    k /= i;
                    expK++;
                }

                // Step 2: Count exponent of prime i in n!
                long long countN = 0, p = i;
                while (p <= n) {
                    countN += n / p;
                    p *= i;
                }

                res = min(res, (int)(countN / expK));
            }
        }

        // If k > 1, it's a prime factor itself
        if (k > 1) {
            long long countN = 0, p = k;
            while (p <= n) {
                countN += n / p;
                p *= k;
            }
            res = min(res, (int)countN);
        }

        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity         | Space Complexity | Pros                                         | Cons                                      |
| -------------- | ----------------------- | ---------------- | -------------------------------------------- | ----------------------------------------- |
| 🥉 Brute Force | O(n!)                   | O(1)             | Conceptually simple                          | Not feasible for n > 20                   |
| 🥈 Optimized   | O(sqrt(k) + m \* log n) | O(m)             | Works for large n, avoids factorial overflow | Slightly more complex                     |
| 🥇 Optimal ⭐  | O(sqrt(k) + m \* log n) | O(m)             | Elegant, efficient, handles all constraints  | Requires understanding of prime exponents |

---

<div align="center">

**🎯 Problem 705234 Completed!**

_Happy Coding! 🚀_

</div>
