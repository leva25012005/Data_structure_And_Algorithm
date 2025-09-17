<div align="center">

# 🧠 [1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201175-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/prime-arrangements/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                 |
| ------------------- | --------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                           |
| **Acceptance Rate** | `60.0%`                                                               |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/prime-arrangements/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)    |

## Description

<!-- description:start -->

<p>Return the number of permutations of 1 to <code>n</code> so that prime numbers are at prime indices (1-indexed.)</p>

<p><em>(Recall that an integer&nbsp;is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers&nbsp;both smaller than it.)</em></p>

<p>Since the answer may be large, return the answer <strong>modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 12
<strong>Explanation:</strong> For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> 682289015
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
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

> - Generate all permutations of numbers from 1..n.
> - For each permutation, check whether prime numbers are placed at prime indices.
> - Count all valid permutations.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    all_permutations = generate all permutations of [1..n]
    count = 0
    for perm in all_permutations:
        valid = true
        for i in 1..n:
            if isPrime(i) and not isPrime(perm[i]):
                valid = false
                break
        if valid:
            count += 1
    return count % MOD
```

#### 💻 Implementation

```cpp
// Brute force approach (Not feasible for large n)

class Solution {
public:
    const int MOD = 1e9 + 7;

    // Check if a number is prime
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    int solutionBruteForce(int n) {
        // Create the array [1..n]
        vector<int> nums(n);
        iota(nums.begin(), nums.end(), 1);

        long long count = 0;

        // Generate all permutations of [1..n]
        do {
            bool valid = true;
            // Check prime index condition
            for (int i = 0; i < n; i++) {
                // (i+1) is the index (1-based)
                if (isPrime(i + 1) && !isPrime(nums[i])) {
                    valid = false; // Invalid if prime index doesn't hold a prime number
                    break;
                }
            }
            if (valid) count++;
        } while (next_permutation(nums.begin(), nums.end()));

        return count % MOD; // Answer modulo 1e9+7
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Instead of generating permutations:
>
> - Count how many prime numbers there are in [1..n]. Call it p.
> - Prime numbers must go into the p prime indices → p! ways.
> - Non-prime numbers go into the remaining (n-p) indices → (n-p)! ways.
> - Final result = p! \* (n-p)! % MOD.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    p = count primes up to n
    return factorial(p) * factorial(n-p) % MOD
```

#### 💻 Implementation

```cpp
// Optimized approach

class Solution {
public:
    const int MOD = 1e9 + 7;

    // Check if a number is prime
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    // Compute factorial % MOD
    long long factorial(int n) {
        long long res = 1;
        for (int i = 2; i <= n; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }

    int solutionOptimized(int n) {
        int p = 0;
        // Count primes from 1 to n
        for (int i = 1; i <= n; i++) {
            if (isPrime(i)) p++;
        }

        // Result = p! * (n - p)! % MOD
        return (factorial(p) * factorial(n - p)) % MOD;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> From approach 2, we already know the formula. To optimize further:
>
> - Use Sieve of Eratosthenes to count primes faster in O(n log log n).
> - Precompute factorials modulo 1e9+7 in one pass.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    primes = sieve(n)
    p = count of primes
    precompute factorial up to n
    return fact[p] * fact[n-p] % MOD
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    const int MOD = 1e9 + 7;

    int numPrimeArrangements(int n) {
        // Step 1: Count primes using Sieve of Eratosthenes
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;

        // Classic sieve
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }

        // Count how many primes up to n
        int p = count(isPrime.begin(), isPrime.end(), true);

        // Step 2: Compute factorials modulo MOD
        long long res = 1;
        // Multiply p! % MOD
        for (int i = 2; i <= p; i++) res = (res * i) % MOD;
        // Multiply (n-p)! % MOD
        for (int i = 2; i <= n - p; i++) res = (res * i) % MOD;

        return (int)res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity    | Space Complexity | Pros                                   | Cons                               |
| -------------- | ------------------ | ---------------- | -------------------------------------- | ---------------------------------- |
| 🥉 Brute Force | O(n! \* n)         | O(n)             | Very intuitive, follows the definition | Impossible for n > 8               |
| 🥈 Optimized   | O(n√n + n)         | O(1)             | Simple formula, works for large `n`    | Prime checking still O(n√n)        |
| 🥇 Optimal ⭐  | O(n log log n + n) | O(n)             | Fast, elegant, uses sieve + factorial  | Slightly more complex to implement |

---

<div align="center">

**🎯 Problem 1175 Completed!**

_Happy Coding! 🚀_

</div>
