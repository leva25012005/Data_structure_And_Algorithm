<div align="center">

# 🧠 [Sum Of Digits](https://www.geeksforgeeks.org/problems/sum-of-digits1742/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/sum-of-digits1742/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Problem ID**   | `703905`                                                                             |
| **Difficulty**   | 🟢 **Easy**                                                                          |
| **Accuracy**     | `67.08%`                                                                             |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/sum-of-digits1742/1)  |
| **Topic Tags**   | ![number-theory](https://img.shields.io/badge/-number-theory-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive number <code>n</code>, find the <strong>sum of all its digits</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 687
<strong>Output:</strong> 21
<strong>Explanation:</strong> Sum of 687's digits: 6 + 8 + 7 = 21
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> Sum of 12's digits: 1 + 2 = 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(log(n))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-for-sum-of-the-digits-of-a-given-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Convert to String)

#### 📝 Intuition

> - Convert the number n to a string.
> - Traverse each character (digit) and sum them.
> - Simple and intuitive, but uses extra space for the string.

#### 🔍 Algorithm

```pseudo
function sumOfDigits(n):
    convert n to string s
    sum = 0
    for each character c in s:
        sum += int(c)
    return sum
```

#### 💻 Implementation

```cpp
// Brute force approach using string conversion

class Solution {
public:
    int sumOfDigits(int n) {
        string s = to_string(n);  // Convert number to string
        int sum = 0;
        for (char c : s) {
            sum += c - '0';       // Convert char to digit and add
        }
        return sum;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Mathematical Extraction)

#### 📝 Intuition

> - Instead of converting to a string, extract digits mathematically using % 10 and / 10.
> - Add each extracted digit to the sum.
> - No extra string space, faster.

#### 🔍 Algorithm

```pseudo
function sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10   // Extract last digit
        n = n / 10      // Remove last digit
    return sum
```

#### 💻 Implementation

```cpp
// Optimized approach using digit extraction

class Solution {
public:
    int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;  // Add last digit
            n /= 10;        // Remove last digit
        }
        return sum;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Recursion / Mathematical Insight)

#### 📝 Intuition

> - Using recursion or a simple formula, the sum can be expressed as:
> - sumOfDigits(n) = (n % 10) + sumOfDigits(n / 10)
> - Elegant and uses O(1) auxiliary space if implemented iteratively.

#### 🔍 Algorithm

```pseudo
function sumOfDigits(n):
    if n == 0: return 0
    return n % 10 + sumOfDigits(n / 10)
```

#### 💻 Implementation

```cpp
// Optimal recursive approach

class Solution {
public:
    int sumOfDigits(int n) {
        if (n == 0) return 0;         // Base case
        return (n % 10) + sumOfDigits(n / 10);  // Add last digit + sum of remaining digits
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity         | Pros                              | Cons                     |
| -------------- | --------------- | ------------------------ | --------------------------------- | ------------------------ |
| 🥉 Brute Force | O(log n)        | O(log n)                 | Very intuitive, easy to implement | Uses extra string space  |
| 🥈 Optimized   | O(log n)        | O(1)                     | No extra space, efficient         | Slightly less intuitive  |
| 🥇 Optimal ⭐  | O(log n)        | O(log n) recursion stack | Elegant and simple                | Recursive stack overhead |

---

<div align="center">

**🎯 Problem 703905 Completed!**

_Happy Coding! 🚀_

</div>
