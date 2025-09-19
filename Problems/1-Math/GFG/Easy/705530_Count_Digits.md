<div align="center">

# 🧠 [Count Digits](https://www.geeksforgeeks.org/problems/count-digits-1606889545/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/count-digits-1606889545/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `705530`                                                                                                                            |
| **Difficulty**   | 🟢 **Easy**                                                                                                                         |
| **Accuracy**     | `50.84%`                                                                                                                            |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/count-digits-1606889545/1)                                           |
| **Topic Tags**   | ![CPP](https://img.shields.io/badge/-CPP-blue?style=flat-square) ![Java](https://img.shields.io/badge/-Java-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a natural number <strong>n</strong>, find the number of digits in it and return the result.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 2
<strong>Explanation:</strong> 12 has 2 digits.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 456
<strong>Output:</strong> 3
<strong>Explanation:</strong> 456 has 3 digits.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 10<sup>5</sup></code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(log n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-count-digits-integer-3-different-methods/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert the integer n into a string.
> - The length of the string equals the number of digits.
> - Simple, but involves string operations.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    convert n to string s
    return length(s)
```

#### 💻 Implementation

**C++:**

```cpp
// Brute force solution using string conversion

class Solution {
public:
    int countDigits(int n) {
        string s = to_string(n);   // Convert integer to string
        return s.size();           // String length = number of digits
    }
};
```

### 🥈 Approach 2: Optimized Solution (Repeated Division)

#### 📝 Intuition

> - Keep dividing n by 10 until it becomes 0.
> - Each division removes the last digit.
> - Count how many times we divide → number of digits.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    count = 0
    while n > 0:
        n = n / 10
        count += 1
    return count
```

#### 💻 Implementation

```cpp
// Optimized solution using repeated division

class Solution {
public:
    int countDigits(int n) {
        int count = 0;
        while (n > 0) {
            n /= 10;    // Remove last digit
            count++;    // Increment digit count
        }
        return count;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Logarithm)

#### 📝 Intuition

> - Use the property of logarithms: number of digits = floor(log10(n)) + 1.
> - This gives the answer in O(1) time with no loops.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return floor(log10(n)) + 1
```

#### 💻 Implementation

```cpp
// Most optimal approach using logarithm

#include <cmath>

class Solution {
public:
    int countDigits(int n) {
        return floor(log10(n)) + 1;  // Formula for digit count
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                         |
| -------------- | --------------- | ---------------- | ------------------------------- | ---------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, just string length | Uses extra memory for string |
| 🥈 Optimized   | O(d)            | O(1)             | Pure integer operations         | Slightly slower than log10   |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, mathematical elegance  | Requires `<cmath>` and care  |

---

<div align="center">

**🎯 Problem 705530 Completed!**

_Happy Coding! 🚀_

</div>
