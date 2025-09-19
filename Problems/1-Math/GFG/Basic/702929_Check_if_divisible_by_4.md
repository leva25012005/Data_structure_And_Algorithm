<div align="center">

# 🧠 [Check if divisible by 4](https://www.geeksforgeeks.org/problems/check-if-divisible-by-43813/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/check-if-divisible-by-43813/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `702929`                                                                                                                                                                                                                                                                                                                              |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                                                                                                          |
| **Accuracy**     | `46.91%`                                                                                                                                                                                                                                                                                                                              |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/check-if-divisible-by-43813/1)                                                                                                                                                                                                                                         |
| **Topic Tags**   | ![Strings](https://img.shields.io/badge/-Strings-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a number <code>N</code>, check whether it is divisible by <code>4</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> N = 1124
<strong>Output:</strong> 1
<strong>Explanation:</strong> The number is divisible by 4 since 1124 % 4 = 0
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> N = 7
<strong>Output:</strong> 0
<strong>Explanation:</strong> The number is not divisible by 4 since 7 % 4 = 3
</pre>

<p>&nbsp;</p>
<strong>Your Task:</strong>  
You don't need to read input or print anything. Your task is to complete the function <code>divisibleBy4()</code> which takes the number in the form of a string <code>N</code> as input and returns <code>1</code> if the number is divisible by 4, otherwise returns <code>0</code>.

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= N &lt;= 10<sup>1000</sup> + 5</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `17-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `17-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-large-number-divisible-4-not/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Convert Entire String to Integer)

#### 📝 Intuition

> - Directly convert the string N into a large integer.
> - Compute N % 4.
> - If the remainder is 0, return 1; otherwise return 0.
> - This works fine in languages with big integer support (like Python), but in C++/Java it will overflow since N can be extremely large (up to 10^1000+5).

#### 🔍 Algorithm

```pseudo
function bruteForce(N):
    num = convert string N to integer
    if num % 4 == 0: return 1
    else return 0
```

#### 💻 Implementation

```cpp
// Brute force approach - works only for small N (overflow risk)

class Solution {
public:
    int divisibleBy4(string N) {
        // Convert whole string to integer (unsafe if N is very large)
        long long num = stoll(N);
        return (num % 4 == 0) ? 1 : 0;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Check Last Two Digits)

#### 📝 Intuition

> - A number is divisible by 4 if and only if its last two digits form a number divisible by 4.
> - We don’t need the whole number, just the last two digits.
> - Example:
>   - 1124 → 24 % 4 = 0 → divisible
>   - 7 → 7 % 4 = 3 → not divisible
> - This avoids overflow and works for very large N.

#### 🔍 Algorithm

```pseudo
function optimized(N):
    if length of N == 1:
        num = int(last digit)
    else:
        num = int(last two digits)
    if num % 4 == 0: return 1
    else return 0
```

#### 💻 Implementation

```cpp
// Optimized approach - checks last two digits only

class Solution {
public:
    int divisibleBy4(string N) {
        int len = N.size();
        int num;
        if (len == 1) {
            num = N[len - 1] - '0';  // Single digit
        } else {
            num = (N[len - 2] - '0') * 10 + (N[len - 1] - '0'); // Last two digits
        }
        return (num % 4 == 0) ? 1 : 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct O(1) without Extra Conversion)

#### 📝 Intuition

> - We don’t even need to construct the last two-digit number fully.
> - Instead, compute (last_digit + 10 \* second_last_digit) % 4 directly.
> - This avoids creating any temporary integers.
> - Works in O(1) time, O(1) space.

#### 🔍 Algorithm

```pseudo
function optimal(N):
    if length of N == 1:
        d = last digit
        return (d % 4 == 0)
    else:
        d1 = last digit
        d2 = second last digit
        return ((d2*10 + d1) % 4 == 0)
```

#### 💻 Implementation

```cpp
// Most optimal solution - O(1) check using only last two digits

class Solution {
public:
    int divisibleBy4(string N) {
        int len = N.size();

        // If only one digit, just check it directly
        if (len == 1) {
            int d = N[0] - '0';
            return (d % 4 == 0) ? 1 : 0;
        }

        // Otherwise, take last two digits
        int d1 = N[len - 1] - '0';     // last digit
        int d2 = N[len - 2] - '0';     // second last digit

        int num = d2 * 10 + d1;        // form two-digit number
        return (num % 4 == 0) ? 1 : 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                    | Cons                                     |
| -------------- | --------------- | ---------------- | --------------------------------------- | ---------------------------------------- |
| 🥉 Brute Force | O(len(N))       | O(1)             | Very intuitive, simple                  | Fails for very large `N` (overflow risk) |
| 🥈 Optimized   | O(1)            | O(1)             | Works for very large `N`                | Needs minor parsing of last digits       |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, fastest, no extra conversions | None                                     |

---

<div align="center">

**🎯 Problem 702929 Completed!**

_Happy Coding! 🚀_

</div>
