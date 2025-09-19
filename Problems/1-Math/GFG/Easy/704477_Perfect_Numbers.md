<div align="center">

# 🧠 [Perfect Numbers](https://www.geeksforgeeks.org/problems/perfect-numbers3207/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/perfect-numbers3207/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704477`                                                                                                                                                          |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                       |
| **Accuracy**     | `17.21%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/perfect-numbers3207/1)                                                                             |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Wipro](https://img.shields.io/badge/-Wipro-orange?style=flat-square)                                                                                            |

## Description

<!-- description:start -->

<p>Given a number <strong>n</strong>, check if it is a <strong>perfect number</strong>.</p>

<p>A number is called <strong>perfect</strong> if the <strong>sum</strong> of all its factors excluding the number itself is equal to the number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> Factors of 6 are 1, 2, 3, 6. Excluding 6, their sum is 1 + 2 + 3 = 6, which equals n. So, it is a Perfect Number.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Factors of 10 are 1, 2, 5, 10. Excluding 10, their sum is 1 + 2 + 5 = 8 ≠ n. So, it is not a Perfect Number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 15
<strong>Output:</strong> false
<strong>Explanation:</strong> Factors of 15 are 1, 3, 5, 15. Excluding 15, their sum is 1 + 3 + 5 = 9 ≠ n. So, it is not a Perfect Number.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(sqrt(n))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<!-- description:end -->

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/perfect-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Sum All Factors)

#### 📝 Intuition

> - Iterate through all numbers from 1 to n-1.
> - Sum all divisors that divide n.
> - Check if the sum equals n.
> - This is simple but slow for large n.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    sum = 0
    for i in 1..n-1:
        if n % i == 0:
            sum += i
    return sum == n
```

#### 💻 Implementation

```cpp
// Brute force: O(n) time

class Solution {
public:
    bool checkPerfectNumber(int n) {
        int sum = 0;
        // Iterate over all numbers less than n
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i; // Add factor
            }
        }
        return sum == n; // Check if sum equals n
    }
};
```

### 🥈 Approach 2: Optimized Solution (Using sqrt(n))

#### 📝 Intuition

> - A factor i of n less than sqrt(n) has a corresponding factor n / i.
> - Iterate from 1 to sqrt(n), sum both i and n/i if i divides n.
> - Exclude n itself from the sum.
> - This reduces time complexity from O(n) to O(sqrt(n)).

#### 🔍 Algorithm

```pseudo
function optimized(n):
    if n <= 1: return false
    sum = 1
    for i in 2..sqrt(n):
        if n % i == 0:
            sum += i
            if i != n / i:
                sum += n / i
    return sum == n
```

#### 💻 Implementation

```cpp
// Optimized: O(sqrt(n)) time

class Solution {
public:
    bool checkPerfectNumber(int n) {
        if (n <= 1) return false; // 1 is not perfect
        int sum = 1; // 1 is always a factor

        // Iterate up to sqrt(n)
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                sum += i; // Add factor i
                if (i != n / i) sum += n / i; // Add corresponding factor n/i
            }
        }
        return sum == n; // Check if sum equals n
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Using Known Perfect Numbers)

#### 📝 Intuition

> - There are only a few known perfect numbers under 10^9: 6, 28, 496, 8128, 33550336.
> - Instead of computation, just check if n is in this set.
> - O(1) time and O(1) space.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    known_perfect_numbers = [6, 28, 496, 8128, 33550336]
    return n in known_perfect_numbers
```

#### 💻 Implementation

```cpp
// Most optimal: O(1) time and space

class Solution {
public:
    bool checkPerfectNumber(int n) {
        // List of all perfect numbers <= 10^9
        int perfectNumbers[] = {6, 28, 496, 8128, 33550336};
        for (int x : perfectNumbers) {
            if (n == x) return true;
        }
        return false;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                        |
| -------------- | --------------- | ---------------- | ------------------------------- | --------------------------- |
| 🥉 Brute Force | O(n)            | O(1)             | Very simple, easy to understand | Too slow for large n        |
| 🥈 Optimized   | O(sqrt(n))      | O(1)             | Fast enough, works for n ≤ 10^9 | Slightly more complex logic |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Instant result, elegant         | Only works for n ≤ 10^9     |

---

<div align="center">

**🎯 Problem 704477 Completed!**

_Happy Coding! 🚀_

</div>
