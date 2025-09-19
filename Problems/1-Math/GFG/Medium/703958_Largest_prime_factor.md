<div align="center">

# 🧠 [Largest prime factor](https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703958`                                                                                                                                                                                                                                                                                                                    |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                               |
| **Accuracy**     | `27.25%`                                                                                                                                                                                                                                                                                                                    |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1)                                                                                                                                                                                                                                  |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Prime Number](https://img.shields.io/badge/-Prime%20Number-blue?style=flat-square) ![sieve](https://img.shields.io/badge/-sieve-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Yahoo](https://img.shields.io/badge/-Yahoo-orange?style=flat-square)                                                                                                                                                                                                                                                      |

## Description

<!-- description:start -->
<p>Given an integer <strong><code>n</code></strong>, the task is to find the <strong>largest prime factor</strong> of <code>n</code>.</p>
<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> The prime factorization of 5 is just 5. Therefore, the largest prime factor is 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 24
<strong>Output:</strong> 3
<strong>Explanation:</strong> The prime factorization of 24 is 2 × 2 × 2 × 3.
Among the prime factors (2, 3), the largest is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> n = 13195
<strong>Output:</strong> 29
<strong>Explanation:</strong> The prime factorization of 13195 is 5 × 7 × 13 × 29.
The largest prime factor is 29.
</pre>

## Constraints

<ul>
  <li><code>2 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(√n)</li>
  <li><strong>Auxiliary Space:</strong> O(1)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-largest-prime-factor-number/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check divisibility)

#### 📝 Intuition

> - For each number i from 2 to n, check if it divides n.
> - If yes, check if i is prime.
> - Keep track of the largest prime factor.
> - This is correct but very slow (O(n√n)).

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    maxPrime = 1
    for i = 2 to n:
        if n % i == 0 and isPrime(i):
            maxPrime = i
    return maxPrime
```

#### 💻 Implementation

```cpp
// Brute force solution (very slow for large n)

class Solution {
public:
    bool isPrime(long long x) {
        if (x < 2) return false;
        for (long long i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    long long largestPrimeFactor(long long n) {
        long long maxPrime = 1;
        for (long long i = 2; i <= n; i++) {
            if (n % i == 0 && isPrime(i)) {
                maxPrime = i; // update max prime factor
            }
        }
        return maxPrime;
    }
};
```

### 🥈 Approach 2: Optimized Solution with Trial Division

#### 📝 Intuition

> - A composite number must have a factor ≤ √n.
> - We divide n by each prime factor we find until n becomes 1.
> - The last divisor we use (or remaining n) is the largest prime factor.
> - This is much faster: O(√n).

#### 🔍 Algorithm

```pseudo
function optimized(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n /= 2
    for i = 3 to sqrt(n) step 2:
        while n % i == 0:
            maxPrime = i
            n /= i
    if n > 2:
        maxPrime = n
    return maxPrime
```

#### 💻 Implementation

```cpp
// Optimized approach using trial division up to sqrt(n)

class Solution {
public:
    long long largestPrimeFactor(long long n) {
        long long maxPrime = -1;

        // Step 1: Divide out all factors of 2
        while (n % 2 == 0) {
            maxPrime = 2;
            n /= 2;
        }

        // Step 2: Divide out odd factors
        for (long long i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                maxPrime = i;
                n /= i;
            }
        }

        // Step 3: If n > 2, then n is prime
        if (n > 2) maxPrime = n;

        return maxPrime;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Efficient Factorization)

#### 📝 Intuition

> - Same as Approach 2 but slightly optimized:
>   - Stop immediately once n becomes 1.
>   - No need to check even numbers after handling 2.
>   - Works in O(√n) with minimal operations.
> - This is the standard efficient solution.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    if n is divisible by 2:
        divide out all 2s
        maxPrime = 2
    for odd i = 3 to sqrt(n):
        while n % i == 0:
            maxPrime = i
            n /= i
    if n > 1:
        maxPrime = n
    return maxPrime
```

#### 💻 Implementation

```cpp
// Most optimal solution for largest prime factor

class Solution {
public:
    long long largestPrimeFactor(long long n) {
        long long maxPrime = -1;

        // Handle factor 2
        if (n % 2 == 0) {
            maxPrime = 2;
            while (n % 2 == 0) n /= 2;
        }

        // Handle odd factors
        for (long long i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                maxPrime = i;
                n /= i;
            }
        }

        // If remaining n is prime and > 2
        if (n > 2) maxPrime = n;

        return maxPrime;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                             | Cons                          |
| -------------- | --------------- | ---------------- | -------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(n√n)          | O(1)             | Very simple, easy to understand  | Extremely slow for large n    |
| 🥈 Optimized   | O(√n)           | O(1)             | Much faster, practical solution  | Still checks all odd numbers  |
| 🥇 Optimal ⭐  | O(√n)           | O(1)             | Standard efficient factorization | Slightly more complex to code |

---

<div align="center">

**🎯 Problem 703958 Completed!**

_Happy Coding! 🚀_

</div>
