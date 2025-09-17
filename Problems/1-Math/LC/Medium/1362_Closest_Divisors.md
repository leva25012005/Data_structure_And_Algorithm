<div align="center">

# 🧠 [1362. Closest Divisors](https://leetcode.com/problems/closest-divisors/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201362-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/closest-divisors/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                       |
| **Acceptance Rate** | `61.6%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/closest-divisors/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>Given an integer <code>num</code>, find the closest two integers in absolute difference whose product equals&nbsp;<code>num + 1</code>&nbsp;or <code>num + 2</code>.</p>

<p>Return the two integers in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 8
<strong>Output:</strong> [3,3]
<strong>Explanation:</strong> For num + 1 = 9, the closest divisors are 3 &amp; 3, for num + 2 = 10, the closest divisors are 2 &amp; 5, hence 3 &amp; 3 is chosen.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 123
<strong>Output:</strong> [5,25]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 999
<strong>Output:</strong> [40,25]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10^9</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `16-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `16-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                 | Difficulty    | Relationship  |
| ----------------------------------------------------------------------------------------------------------------------- | ------------- | ------------- |
| [Distinct Prime Factors of Product of Array](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) | 🟡 **Medium** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - The most naive way is to check all possible divisors of num + 1 and num + 2 and find the pair with the smallest absolute difference.
> - This works but is very slow because checking all divisors up to num + 2 (≈ 10⁹) would be infeasible.

#### 🔍 Algorithm

```pseudo
function closestDivisors(num):
    best_pair = []
    best_diff = infinity

    for candidate in [num + 1, num + 2]:
        for d in range(1, candidate):   // check all divisors
            if candidate % d == 0:
                other = candidate / d
                if abs(d - other) < best_diff:
                    best_diff = abs(d - other)
                    best_pair = [d, other]

    return best_pair
```

#### 💻 Implementation

```cpp
// Brute force approach (not efficient for large numbers)

class Solution {
public:
    vector<int> closestDivisors(int num) {
        int bestDiff = INT_MAX;
        vector<int> bestPair;

        // Check num + 1 and num + 2
        for (int candidate : {num + 1, num + 2}) {
            for (int d = 1; d <= candidate; d++) { // brute check all divisors
                if (candidate % d == 0) {
                    int other = candidate / d;
                    if (abs(d - other) < bestDiff) {
                        bestDiff = abs(d - other);
                        bestPair = {d, other};
                    }
                }
            }
        }
        return bestPair;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Divisor Search)

#### 📝 Intuition

> - Instead of checking all divisors up to n, we only need to check up to sqrt(n), because if d is a divisor, n/d is its pair.
> - This reduces the complexity from O(n) to O(√n).

#### 🔍 Algorithm

```pseudo
function closestDivisors(num):
    best_pair = []
    best_diff = infinity

    for candidate in [num + 1, num + 2]:
        for d in range(1, sqrt(candidate)):
            if candidate % d == 0:
                other = candidate / d
                if abs(d - other) < best_diff:
                    best_diff = abs(d - other)
                    best_pair = [d, other]

    return best_pair
```

#### 💻 Implementation

```cpp
/// Optimized approach with divisor check up to sqrt(n)

class Solution {
public:
    vector<int> closestDivisors(int num) {
        int bestDiff = INT_MAX;
        vector<int> bestPair;

        // Lambda to process one candidate
        auto checkDivisors = [&](int candidate) {
            for (int d = 1; d * d <= candidate; d++) {
                if (candidate % d == 0) {
                    int other = candidate / d;
                    if (abs(d - other) < bestDiff) {
                        bestDiff = abs(d - other);
                        bestPair = {d, other};
                    }
                }
            }
        };

        // Check both num+1 and num+2
        checkDivisors(num + 1);
        checkDivisors(num + 2);

        return bestPair;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - The most efficient method:
>   - Only check divisors from sqrt(num + 2) down to 1.
>   - As soon as we find a divisor pair, it’s guaranteed to be close since divisors around the square root are the closest possible.
>   - Compare for both num+1 and num+2.
> - This avoids unnecessary checks.

#### 🔍 Algorithm

```pseudo
function closestDivisors(num):
    for candidate in [num + 1, num + 2]:
        start = floor(sqrt(candidate))
        for d in range(start, 0, -1):
            if candidate % d == 0:
                return [d, candidate/d]   // first found is the closest
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution sing sqrt and early exit

class Solution {
public:
    vector<int> closestDivisors(int num) {
        // Helper lambda: find closest divisor pair for a candidate
        auto findPair = [](int candidate) -> vector<int> {
            for (int d = sqrt(candidate); d >= 1; d--) {
                if (candidate % d == 0) {
                    return {d, candidate / d}; // closest pair found
                }
            }
            return {};
        };

        // Find best from num+1 and num+2
        vector<int> pair1 = findPair(num + 1);
        vector<int> pair2 = findPair(num + 2);

        // Choose the one with smaller difference
        if (abs(pair1[0] - pair1[1]) < abs(pair2[0] - pair2[1])) {
            return pair1;
        }
        return pair2;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity      | Space Complexity | Pros                                         | Cons                                   |
| -------------- | -------------------- | ---------------- | -------------------------------------------- | -------------------------------------- |
| 🥉 Brute Force | O(n)                 | O(1)             | Very simple                                  | Impossible for large n (up to 1e9)     |
| 🥈 Optimized   | O(√n)                | O(1)             | Works for large n                            | Still checks more divisors than needed |
| 🥇 Optimal ⭐  | O(√n) but early exit | O(1)             | Elegant, minimal checks, fastest in practice | Slightly more logic                    |

---

<div align="center">

**🎯 Problem 1362 Completed!**

_Happy Coding! 🚀_

</div>
