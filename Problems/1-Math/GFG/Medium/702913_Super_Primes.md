<div align="center">

# 🧠 [Super Primes](https://www.geeksforgeeks.org/problems/super-primes2443/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/super-primes2443/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `702913`                                                                                                                                                    |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                               |
| **Accuracy**     | `24.9%`                                                                                                                                                     |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/super-primes2443/1)                                                                          |
| **Topic Tags**   | ![Searching](https://img.shields.io/badge/-Searching-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p><span style="font-size: 18px;">A prime number is called a <strong>Super Prime</strong> if it can be expressed as the sum of two prime numbers. The task is to find the total count of Super Primes up to a given number <strong>N</strong>.</span></p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> N = 5
<strong>Output:</strong> 1
<strong>Explanation:</strong> 5 = 2 + 3, hence 5 is the only Super Prime.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> N = 10
<strong>Output:</strong> 2
<strong>Explanation:</strong> Both 5 (2+3) and 7 (2+5) are Super Primes.
</pre>

## Your Task

You don't need to read input or print anything.  
Your task is to complete the function <strong>superPrimes()</strong> which takes the integer <strong>N</strong> as input and returns the count of Super Primes up to <strong>N</strong>.

## Constraints

<ul>
  <li><code>1 ≤ N ≤ 10<sup>5</sup></code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(N log log N)</li>
  <li><strong>Auxiliary Space:</strong> O(N)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/super-prime/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - For every number x ≤ N, check if x is prime.
> - If it is prime, check if it can be expressed as the sum of two primes (x = p1 + p2).
> - Count how many such primes exist.
> - This is straightforward but slow because it checks all pairs for every prime.

#### 🔍 Algorithm

```pseudo
function bruteForce(N):
    count = 0
    for x in 2..N:
        if isPrime(x):
            for p in 2..x-1:
                if isPrime(p) and isPrime(x-p):
                    count++
                    break
    return count
```

#### 💻 Implementation

```cpp
// Brute force solution

class Solution {
public:
    // Check primality
    bool isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int superPrimes(int N) {
        int count = 0;
        // Check each number up to N
        for (int x = 2; x <= N; x++) {
            if (isPrime(x)) {
                // Try to split into sum of two primes
                for (int p = 2; p < x; p++) {
                    if (isPrime(p) && isPrime(x - p)) {
                        count++;
                        break; // Only need one valid pair
                    }
                }
            }
        }
        return count;
    }
};
```

(

### 🥈 Approach 2: Optimized Solution (Prime Precomputation)

#### 📝 Intuition

> - Instead of checking primality repeatedly, precompute all primes up to N using Sieve of Eratosthenes.
> - For each prime x, just check if there exists a prime p such that (x - p) is also prime.
> - Much faster than brute force.

#### 🔍 Algorithm

```pseudo
function sieve(N):
    create boolean array isPrime[0..N]
    mark primes using sieve
    return isPrime

function optimized(N):
    isPrime = sieve(N)
    count = 0
    for x in 2..N:
        if isPrime[x]:
            for p in 2..x-1:
                if isPrime[p] and isPrime[x-p]:
                    count++
                    break
    return count
```

#### 💻 Implementation

```cpp
// Optimized approach with sieve + checking pairs

class Solution {
public:
    vector<bool> sieve(int N) {
        vector<bool> isPrime(N + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= N; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }

    int superPrimes(int N) {
        auto isPrime = sieve(N);
        int count = 0;

        for (int x = 2; x <= N; x++) {
            if (isPrime[x]) {
                // Check if x can be written as p + (x-p)
                for (int p = 2; p < x; p++) {
                    if (isPrime[p] && isPrime[x - p]) {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Use sieve once to precompute all primes up to N.
> - Notice: any prime > 2 can only be expressed as 2 + (prime-2) if (prime-2) is also prime.
> - So, to check if a prime x is a Super Prime: just verify isPrime[x-2].
> - This reduces complexity to O(N log log N) (for sieve) + O(N) for checking.

#### 🔍 Algorithm

```pseudo
function optimal(N):
    isPrime = sieve(N)
    count = 0
    for x in 5..N:     // since 5 is the smallest super prime
        if isPrime[x] and isPrime[x-2]:
            count++
    return count
```

#### 💻 Implementation

```cpp
// Optimal approach: O(N log log N) using sieve + direct check

class Solution {
public:
    vector<bool> sieve(int N) {
        vector<bool> isPrime(N + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= N; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }

    int superPrimes(int N) {
        auto isPrime = sieve(N);
        int count = 0;

        // Check primes >= 5
        for (int x = 5; x <= N; x++) {
            if (isPrime[x] && isPrime[x - 2]) {
                count++;
            }
        }
        return count;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity      | Space Complexity | Pros                                  | Cons                          |
| -------------- | -------------------- | ---------------- | ------------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(N² / log N) approx | O(1)             | Very simple, easy to understand       | Too slow for N = 1e5          |
| 🥈 Optimized   | O(N² / log N)        | O(N)             | Uses sieve, faster primality checking | Still quadratic in worst case |
| 🥇 Optimal ⭐  | O(N log log N)       | O(N)             | Efficient, elegant, works for large N | Requires key observation      |

---

<div align="center">

**🎯 Problem 702913 Completed!**

_Happy Coding! 🚀_

</div>
