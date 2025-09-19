<div align="center">

# 🧠 [Sieve of Eratosthenes](https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704146`                                                                                                                                                                                                                                       |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                  |
| **Accuracy**     | `47.43%`                                                                                                                                                                                                                                       |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1)                                                                                                                                                    |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![sieve](https://img.shields.io/badge/-sieve-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)         |
| **Company Tags** | ![VMWare](https://img.shields.io/badge/-VMWare-orange?style=flat-square) ![MAQ Software](https://img.shields.io/badge/-MAQ%20Software-orange?style=flat-square) ![SAP Labs](https://img.shields.io/badge/-SAP%20Labs-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <strong>n</strong>, calculate and return all prime numbers less than or equal to <strong>n</strong> using the <strong>Sieve of Eratosthenes</strong> algorithm.</p>

<p><strong>Definition:</strong> A <strong>prime number</strong> is a natural number greater than 1 that has no positive divisors other than 1 and itself.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> [2, 3, 5, 7]
<strong>Explanation:</strong> Prime numbers less than or equal to 10 are 2, 3, 5, and 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 35
<strong>Output:</strong> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
<strong>Explanation:</strong> Prime numbers less than or equal to 35 are 
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, and 31.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 10<sup>4</sup></code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(n log log n)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Trial Division)

#### 📝 Intuition

> - For each number i from 2 to n, check if it is prime by testing divisibility up to sqrt(i).
> - Collect all primes in a list.
> - This is straightforward but slower (O(n√n))

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    primes = []
    for i in 2..n:
        if isPrime(i):   // check divisibility
            primes.append(i)
    return primes
```

#### 💻 Implementation

```cpp
// Brute force solution: O(n * sqrt(n))

class Solution {
public:
    // Check if a number is prime
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    vector<int> primesBruteForce(int n) {
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) primes.push_back(i);
        }
        return primes;
    }
};
```

### 🥈 Approach 2: Optimized Solution with Early Sieve (Mark Multiples)

#### 📝 Intuition

> - Instead of checking each number separately, mark multiples of each prime.
> - For every prime p, mark all multiples 2p, 3p, … as non-prime.
> - This reduces redundant checks, but still runs in ~O(n log n).

#### 🔍 Algorithm

```pseudo
function earlySieve(n):
    create array isPrime[0..n] = true
    isPrime[0] = isPrime[1] = false
    for i = 2..n:
        if isPrime[i]:
            mark multiples of i as not prime
    collect all numbers where isPrime[i] = true
```

#### 💻 Implementation

```cpp
// Early sieve (O(n log n))

class Solution {
public:
    vector<int> primesEarlySieve(int n) {
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;

        // Mark multiples of each number
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                for (int j = 2 * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // Collect primes
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) primes.push_back(i);
        }
        return primes;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Sieve of Eratosthenes)

#### 📝 Intuition

> - The optimized sieve marks multiples starting from i² (since smaller multiples are already marked by smaller primes).
> - This reduces time complexity to O(n log log n).
> - Space is O(n) for the boolean array.

#### 🔍 Algorithm

```pseudo
function sieveOfEratosthenes(n):
    create array isPrime[0..n] = true
    isPrime[0] = isPrime[1] = false
    for i = 2..sqrt(n):
        if isPrime[i]:
            for j = i*i..n step i:
                isPrime[j] = false
    collect all numbers where isPrime[i] = true
```

#### 💻 Implementation

```cpp
// Optimal Sieve of Eratosthenes: O(n log log n)

class Solution {
public:
    vector<int> sieveOfEratosthenes(int n) {
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;

        // Only need to check up to sqrt(n)
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                // Start from i*i
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // Collect primes
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) primes.push_back(i);
        }
        return primes;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                            |
| -------------- | --------------- | ---------------- | ----------------------------------- | ------------------------------- |
| 🥉 Brute Force | O(n√n)          | O(1)             | Very simple to implement            | Too slow for n up to 10⁴        |
| 🥈 Early Sieve | O(n log n)      | O(n)             | Faster than brute force             | Still marks redundant multiples |
| 🥇 Optimal ⭐  | O(n log log n)  | O(n)             | Best performance, classic algorithm | Slightly more complex           |

---

<div align="center">

**🎯 Problem 704146 Completed!**

_Happy Coding! 🚀_

</div>
