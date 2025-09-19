<div align="center">

# 🧠 [Prime Factors](https://www.geeksforgeeks.org/problems/prime-factors5052/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/prime-factors5052/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `705041`                                                                                                                                                                                                                                                                                                                    |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                                                 |
| **Accuracy**     | `30.47%`                                                                                                                                                                                                                                                                                                                    |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/prime-factors5052/1)                                                                                                                                                                                                                                         |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Prime Number](https://img.shields.io/badge/-Prime%20Number-blue?style=flat-square) ![sieve](https://img.shields.io/badge/-sieve-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a number <strong>n</strong>, find its <strong>unique</strong> prime factors in <strong>increasing order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> [2, 5]
<strong>Explanation:</strong> Unique prime factors of 100 are 2 and 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 60
<strong>Output:</strong> [2, 3, 5]
<strong>Explanation:</strong> Prime factors of 60 are 2, 2, 3, 5. Unique prime factors are 2, 3 and 5.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task:</strong></p>

<p>You don't need to read input or print anything. Complete the function that takes an integer <strong>n</strong> and returns a list of its unique prime factors in increasing order.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ n ≤ 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(√n)<br>
<strong>Expected Auxiliary Space:</strong> O(log n)</p>

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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/prime-factor/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check every number)

#### 📝 Intuition

> - For every number i from 2 to n:
>   - Check if i is a prime.
>   - If yes and i divides n, include it in the result.
> - This is simple but not efficient since we check primality for many numbers.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    result = []
    for i in 2..n:
        if isPrime(i) and n % i == 0:
            result.push(i)
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    // Prime check helper
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    vector<int> solutionBruteForce(int n) {
        vector<int> res;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i) && n % i == 0) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Optimized Trial Division)

#### 📝 Intuition

> - Instead of checking all numbers, factorize n directly.
> - Divide by 2 until n is no longer divisible by 2.
> - Repeat for odd numbers from 3 up to √n.
> - If after the loop n > 1, then n itself is a prime factor.
> - Store unique factors in order.
> - This improves efficiency to O(√n).

#### 🔍 Algorithm

```pseudo
function optimized(n):
    result = []
    if n % 2 == 0:
        result.push(2)
        while n % 2 == 0:
            n /= 2
    for i in 3..√n step 2:
        if n % i == 0:
            result.push(i)
            while n % i == 0:
                n /= i
    if n > 1:
        result.push(n)
    return result
```

#### 💻 Implementation

```cpp
// Optimized trial division approach

class Solution {
public:
    vector<int> solutionOptimized(int n) {
        vector<int> res;

        // Check factor 2 separately
        if (n % 2 == 0) {
            res.push_back(2);
            while (n % 2 == 0) n /= 2;
        }

        // Check odd factors
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                res.push_back(i);
                while (n % i == 0) n /= i;
            }
        }

        // If n > 1, it's a prime factor
        if (n > 1) res.push_back(n);

        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Sieve Preprocessing)

#### 📝 Intuition

> - Precompute smallest prime factors (SPF) for all numbers up to 10^6 using a sieve.
> - Then factorize n quickly by dividing it using SPF.
> - Collect unique factors in ascending order.
> - This reduces multiple queries to O(log n) after preprocessing.t

#### 🔍 Algorithm

```pseudo
function sieve(limit):
    spf = array[limit+1]
    for i in 2..limit: spf[i] = i
    for i in 2..√limit:
        if spf[i] == i:
            for j in i*i..limit step i:
                if spf[j] == j:
                    spf[j] = i
    return spf

function optimal(n, spf):
    result = set()
    while n > 1:
        result.add(spf[n])
        n /= spf[n]
    return sorted(result)
```

#### 💻 Implementation

```cpp
// Most optimal with Sieve of Eratosthenes (SPF)

class Solution {
public:
    const int MAXN = 1000000;
    vector<int> spf; // Smallest Prime Factor

    Solution() {
        // Precompute SPF using sieve
        spf.resize(MAXN + 1);
        for (int i = 0; i <= MAXN; i++) spf[i] = i;
        for (int i = 2; i * i <= MAXN; i++) {
            if (spf[i] == i) { // i is prime
                for (int j = i * i; j <= MAXN; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
    }

    vector<int> solutionOptimal(int n) {
        vector<int> res;
        unordered_set<int> seen; // To ensure uniqueness

        while (n > 1) {
            int primeFactor = spf[n];
            if (!seen.count(primeFactor)) {
                res.push_back(primeFactor);
                seen.insert(primeFactor);
            }
            n /= primeFactor;
        }

        sort(res.begin(), res.end()); // Ensure increasing order
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity                                     | Space Complexity | Pros                                             | Cons                                |
| -------------- | --------------------------------------------------- | ---------------- | ------------------------------------------------ | ----------------------------------- |
| 🥉 Brute Force | O(n√n)                                              | O(1)             | Very simple, checks directly                     | Very slow for large `n`             |
| 🥈 Optimized   | O(√n)                                               | O(1)             | Efficient for single queries                     | Still slower for many queries       |
| 🥇 Optimal ⭐  | O(log n) (per query) + O(N log log N) preprocessing | O(N)             | Super fast after sieve, handles multiple queries | Preprocessing required, more memory |

---

<div align="center">

**🎯 Problem 705041 Completed!**

_Happy Coding! 🚀_

</div>
