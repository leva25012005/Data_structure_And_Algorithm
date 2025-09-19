<div align="center">

# 🧠 [3 Divisors](https://www.geeksforgeeks.org/problems/3-divisors3942/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/3-divisors3942/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703970`                                                                                                                                                          |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                     |
| **Accuracy**     | `11.17%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/3-divisors3942/1)                                                                                  |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>You are given a list of <strong>q</strong> queries, and for each query, an integer <strong>n</strong> is provided.  
The task is to find how many numbers less than or equal to <strong>n</strong> have exactly <strong>3 divisors</strong>.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
q = 1
query[0] = 6

<strong>Output:</strong>
1

<strong>Explanation:</strong>
There is only one number 4 which has exactly three divisors: 1, 2 and 4, and it is ≤ 6.

</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> 
q = 2
query[0] = 6
query[1] = 10

<strong>Output:</strong>
1
2

<strong>Explanation:</strong>
For query[0], the answer is 1 (only 4).
For query[1], there are two numbers ≤ 10 with exactly three divisors: 4 and 9.

</pre>

## Constraints

<ul>
  <li><code>1 ≤ q ≤ 10³</code></li>
  <li><code>1 ≤ query[i] ≤ 10¹²</code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(q * √n * log log n)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-all-factors-of-a-natural-number-in-sorted-order/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/numbers-exactly-3-divisors/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - A number has exactly 3 divisors if and only if it is a square of a prime number.
>   - Example: 4 = 2² → divisors are {1, 2, 4}.
>   - Example: 9 = 3² → divisors are {1, 3, 9}.
> - Brute force idea:
>   - For each query n, check all numbers ≤ n.
>   - Count how many of them have exactly 3 divisors by testing divisor counts.
> - This is correct but too slow for n ≤ 10^12.

#### 🔍 Algorithm

```pseudo
function bruteForce(q, queries):
    for each n in queries:
        count = 0
        for num in 1..n:
            if divisorCount(num) == 3:
                count++
        print count
```

#### 💻 Implementation

```cpp
// Brute force approach (too slow for large n)

class Solution {
public:
    // Count divisors of x
    int countDivisors(long long x) {
        int cnt = 0;
        for (long long i = 1; i * i <= x; i++) {
            if (x % i == 0) {
                cnt++;
                if (i != x / i) cnt++;
            }
        }
        return cnt;
    }

    vector<int> solutionBruteForce(vector<long long>& queries) {
        vector<int> ans;
        for (long long n : queries) {
            int count = 0;
            for (long long i = 1; i <= n; i++) {
                if (countDivisors(i) == 3) count++;
            }
            ans.push_back(count);
        }
        return ans;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Check Prime Squares)

#### 📝 Intuition

> - Instead of checking all numbers ≤ n, only prime squares can have exactly 3 divisors.
> - So, we just need to:
>   - Find all primes up to √(max(n)).
>   - For each query n, count how many prime squares ≤ n.
> - This reduces the problem from checking up to n to checking up to √n.

#### 🔍 Algorithm

```pseudo
function optimized(q, queries):
    maxN = max(queries)
    limit = sqrt(maxN)
    primes = sieve(limit)
    primeSquares = [p^2 for each p in primes]

    for each n in queries:
        count = number of primeSquares ≤ n
        print count
```

#### 💻 Implementation

```cpp
// Optimized approach

class Solution {
public:
    // Sieve of Eratosthenes
    vector<int> sieve(int limit) {
        vector<bool> isPrime(limit + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i)
                    isPrime[j] = false;
            }
        }
        vector<int> primes;
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) primes.push_back(i);
        }
        return primes;
    }

    vector<int> solutionOptimized(vector<long long>& queries) {
        long long maxN = *max_element(queries.begin(), queries.end());
        long long limit = sqrt(maxN);

        // Step 1: Get primes up to sqrt(maxN)
        vector<int> primes = sieve(limit);

        // Step 2: Precompute prime squares
        vector<long long> primeSquares;
        for (int p : primes) {
            primeSquares.push_back(1LL * p * p);
        }

        // Step 3: Answer queries
        vector<int> ans;
        for (long long n : queries) {
            int count = upper_bound(primeSquares.begin(), primeSquares.end(), n) - primeSquares.begin();
            ans.push_back(count);
        }
        return ans;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Preprocessing + Binary Search)

#### 📝 Intuition

> - Extend approach 2 with full preprocessing:
>   - Precompute all prime squares once.
>   - For queries, just binary search how many are ≤ n.
> - Complexity becomes O(q log P) where P = number of primes ≤ 10^6 (~78k).
> - Extremely fast for q ≤ 10³ and n ≤ 10¹².

#### 🔍 Algorithm

```pseudo
function optimal(q, queries):
    precompute primeSquares up to 10^12
    for each n in queries:
        count = binarySearch(primeSquares, n)
        print count
```

#### 💻 Implementation

```cpp
// Most optimal solution with preprocessing and binary search

class Solution {
public:
    vector<long long> primeSquares;
    const long long LIMIT = 1e12;

    Solution() {
        // Precompute all prime squares up to 1e12
        int maxPrime = sqrt(LIMIT);
        vector<bool> isPrime(maxPrime + 1, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= maxPrime; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxPrime; j += i)
                    isPrime[j] = false;
            }
        }

        for (int i = 2; i <= maxPrime; i++) {
            if (isPrime[i]) primeSquares.push_back(1LL * i * i);
        }
    }

    vector<int> solutionOptimal(vector<long long>& queries) {
        vector<int> ans;
        for (long long n : queries) {
            // Count numbers <= n using binary search
            int count = upper_bound(primeSquares.begin(), primeSquares.end(), n) - primeSquares.begin();
            ans.push_back(count);
        }
        return ans;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity            | Space Complexity | Pros                           | Cons                     |
| -------------- | -------------------------- | ---------------- | ------------------------------ | ------------------------ |
| 🥉 Brute Force | O(q \* n√n)                | O(1)             | Very simple, easy to code      | Impossible for large n   |
| 🥈 Optimized   | O(√n log log √n + q log P) | O(√n)            | Efficient, uses sieve + primes | Still computes per query |
| 🥇 Optimal ⭐  | O(√n log log √n + q log P) | O(√n)            | Fastest, full preprocessing    | More code complexity     |

---

<div align="center">

**🎯 Problem 703970 Completed!**

_Happy Coding! 🚀_

</div>
