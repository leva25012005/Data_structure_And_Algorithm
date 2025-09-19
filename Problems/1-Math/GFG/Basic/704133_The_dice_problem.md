<div align="center">

# 🧠 [The dice problem](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704133`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `73.72%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)                                                                            |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <code>N</code>, recursively sum the digits of <code>N</code> until the result is a single digit.</p>

<pre>
If N < 10
    digSum(N) = N
Else
    digSum(N) = digSum(Sum of digits of N)
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> N = 1234
<strong>Output:</strong> 1
<strong>Explanation:</strong> The sum of digits is 1 + 2 + 3 + 4 = 10.
Since 10 is not a single digit, repeat: 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> N = 9999
<strong>Output:</strong> 9
<strong>Explanation:</strong> 9 + 9 + 9 + 9 = 36 → 3 + 6 = 9
</pre>

<p>&nbsp;</p>
<strong>Your Task:</strong>  
You don't need to read input or print anything. Your task is to complete the function <code>repeatedSumOfDigits()</code> which takes an integer <code>N</code> and returns the repeated sum of digits of <code>N</code>.

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= N &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/the-dice-problem/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursive Sum of Digits)

#### 📝 Intuition

> - Base case: if N < 10, return N.
> - Otherwise, sum all digits of N and recursively call the function.
> - Keep repeating until a single-digit number is obtained.

#### 🔍 Algorithm

```pseudo
function digSum(N):
    if N < 10:
        return N
    sum_digits = sum of digits of N
    return digSum(sum_digits)
```

#### 💻 Implementation

```cpp
// Brute force recursive solution

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        if (N < 10) return N; // Base case: single-digit

        int sum = 0;
        int n = N;
        while (n > 0) {
            sum += n % 10; // Add last digit
            n /= 10;       // Remove last digit
        }

        return repeatedSumOfDigits(sum); // Recur with sum of digits
    }
};
```

### 🥈 Approach 2: Optimized Solution (Iterative Sum of Digits)

#### 📝 Intuition

> - Instead of recursion, sum the digits iteratively until a single digit remains.
> - This avoids function call overhead.

#### 🔍 Algorithm

```pseudo
function digSumIterative(N):
    while N >= 10:
        sum_digits = sum of digits of N
        N = sum_digits
    return N
```

#### 💻 Implementation

```cpp
// Iterative approach

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        while (N >= 10) {
            int sum = 0;
            int n = N;
            while (n > 0) {
                sum += n % 10; // Add last digit
                n /= 10;       // Remove last digit
            }
            N = sum; // Update N with sum of digits
        }
        return N; // Single-digit result
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ - Mathematical Formula (Digital Root)

#### 📝 Intuition

> - There is a O(1) formula for repeated sum of digits, also called digital root:
>   - If N == 0, result is 0.
>   - Otherwise, result = 1 + (N-1) % 9.
> - This works because repeated sum of digits modulo 9 is equivalent to the number modulo 9.

#### 🔍 Algorithm

```pseudo
function digSumFormula(N):
    if N == 0: return 0
    else: return 1 + (N-1) % 9
```

#### 💻 Implementation

```cpp
// Most optimal solution using digital root formula

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        if (N == 0) return 0;          // Edge case
        return 1 + (N - 1) % 9;        // Digital root formula
    }
};
```

## 📊 Comparison of Approaches

| Approach           | Time Complexity | Space Complexity | Pros                                    | Cons                            |
| ------------------ | --------------- | ---------------- | --------------------------------------- | ------------------------------- |
| 🥉 Recursive       | O(log N)        | O(log N)         | Very intuitive                          | Recursion stack overhead        |
| 🥈 Iterative       | O(log N)        | O(1)             | No recursion, safe for large N          | Slightly more code than formula |
| 🥇 Digital Root ⭐ | O(1)            | O(1)             | Elegant, optimal, constant time & space | Needs formula knowledge         |

---

<div align="center">

**🎯 Problem 704133 Completed!**

_Happy Coding! 🚀_

</div>
