<div align="center">

# 🧠 [All divisors of a Number](https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `712172`                                                                                                                                                                                                                                               |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                            |
| **Accuracy**     | `46.73%`                                                                                                                                                                                                                                               |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1)                                                                                                                                                             |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Factorization](https://img.shields.io/badge/-Factorization-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <strong>n</strong>, print all the divisors of <strong>n</strong> in <strong>ascending order</strong>.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 1 2 4 5 10 20
<strong>Explanation:</strong> 20 is completely divisible by 1, 2, 4, 5, 10 and 20.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 21191
<strong>Output:</strong> 1 21191
<strong>Explanation:</strong> 21191 is a prime number, so it has only 2 factors: 1 and itself.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(√n)<br>
<strong>Expected Auxiliary Space:</strong> O(√n)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-all-factors-of-a-natural-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - The simplest way is to check all numbers from 1 to n.
> - If a number divides n, it’s a divisor.
> - Collect and print them in ascending order.
> - This is correct but very slow (O(n)), especially since n can be as large as 10^9.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    for i in 1..n:
        if n % i == 0:
            print i
```

#### 💻 Implementation

```cpp
// Brute force approach: O(n)

class Solution {
public:
    vector<int> divisorsBruteForce(int n) {
        vector<int> result;
        // Check all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                result.push_back(i);
            }
        }
        return result; // Already in ascending order
    }
};
```

### 🥈 Approach 2: Optimized Solution (Check up to √n)

#### 📝 Intuition

> - A divisor d always pairs with n/d.
> - So, we only need to check divisors up to √n.
> - For every i where n % i == 0:
>   - Add i
>   - Add n/i (if different)
> - Finally, sort the divisors.
> - This reduces complexity to O(√n).

#### 🔍 Algorithm

```pseudo
function optimized(n):
    divisors = []
    for i in 1..sqrt(n):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n/i)
    sort(divisors)
    return divisors
```

#### 💻 Implementation

```cpp
// Optimized approach: O(√n)

class Solution {
public:
    vector<int> divisorsOptimized(int n) {
        vector<int> result;
        // Loop only up to sqrt(n)
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                result.push_back(i);        // divisor i
                if (i != n / i) {
                    result.push_back(n / i); // paired divisor
                }
            }
        }
        sort(result.begin(), result.end()); // Ensure ascending order
        return result;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Sorted Without Extra Sort)

#### 📝 Intuition

> - To avoid sorting at the end:
>   - Store small divisors (i values) directly in one vector.
>   - Store large divisors (n/i values) in another vector.
> - After finishing the loop up to √n, append the reversed list of large divisors.
> - This gives a naturally sorted list without needing sort()

#### 🔍 Algorithm

```pseudo
function optimal(n):
    small = []
    large = []
    for i in 1..sqrt(n):
        if n % i == 0:
            small.append(i)
            if i != n/i:
                large.append(n/i)
    result = small + reverse(large)
    return result
```

#### 💻 Implementation

```cpp
// Optimal approach: O(√n), no sorting needed

class Solution {
public:
    vector<int> divisorsOptimal(int n) {
        vector<int> small, large;
        // Collect divisors
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                small.push_back(i);        // Small divisor
                if (i != n / i) {
                    large.push_back(n / i); // Paired large divisor
                }
            }
        }
        // Append reversed large divisors for ascending order
        reverse(large.begin(), large.end());
        small.insert(small.end(), large.begin(), large.end());
        return small;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                 |
| -------------- | --------------- | ---------------- | ------------------------------------ | -------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very easy to implement               | Too slow for `n=1e9` |
| 🥈 Optimized   | O(√n + log n)   | O(√n)            | Efficient, works within constraints  | Needs sorting step   |
| 🥇 Optimal ⭐  | O(√n)           | O(√n)            | No sorting required, directly sorted | Slightly more logic  |

---

<div align="center">

**🎯 Problem 712172 Completed!**

_Happy Coding! 🚀_

</div>
