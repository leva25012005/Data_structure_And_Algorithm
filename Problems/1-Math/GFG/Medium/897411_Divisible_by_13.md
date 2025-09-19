<div align="center">

# 🧠 [Divisible by 13](https://www.geeksforgeeks.org/problems/divisible-by-13/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/divisible-by-13/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                              |
| ---------------- | ---------------------------------------------------------------------------------- |
| **Problem ID**   | `897411`                                                                           |
| **Difficulty**   | 🟡 **Medium**                                                                      |
| **Accuracy**     | `50.24%`                                                                           |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/divisible-by-13/1)  |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a number represented as a string <strong>s</strong> (which may be very large), check whether it is divisible by 13 or not.</p>

<p><strong>Your Task:</strong><br>
You don't need to read input or print anything. Complete the function <strong>isDivisibleBy13()</strong> which takes a string <strong>s</strong> as input and returns <strong>true</strong> if it is divisible by 13, otherwise <strong>false</strong>.</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "2911285"
<strong>Output:</strong> true
<strong>Explanation:</strong> 2911285 / 13 = 223945, which is a whole number with no remainder.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "27"
<strong>Output:</strong> false
<strong>Explanation:</strong> 27 / 13 ≈ 2.0769..., which is not a whole number (there is a remainder).
</pre>

## Constraints

<ul>
  <li><code>1 ≤  s.size() ≤ 10<sup>5</sup></code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `19-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `19-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-large-number-divisible-13-not/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Convert to Number)

#### 📝 Intuition

> - Convert the string s to an integer type and check num % 13 == 0.
> - Works for small numbers, but fails for very large numbers (up to 10^105).

#### 🔍 Algorithm

```pseudo
function bruteForce(s):
    num = convert s to integer
    return num % 13 == 0
```

#### 💻 Implementation

```cpp
// Brute force: convert string to number (fails for very large strings)

class Solution {
public:
    bool isDivisibleBy13(string s) {
        long long num = stoll(s); // Convert string to number
        return num % 13 == 0;
    }
};
```

### 🥈 Approach 2: Optimized Solution - Manual Division (Digit by Digit)

#### 📝 Intuition

> - Simulate division manually to handle very large numbers.
> - Traverse the string and maintain a remainder modulo 13.
> - For each digit, update remainder as:
> - remainder = (remainder \* 10 + digit) % 13.
> - At the end, check if remainder is 0.

#### 🔍 Algorithm

```pseudo
function manualDivision(s):
    remainder = 0
    for each character c in s:
        digit = c - '0'
        remainder = (remainder * 10 + digit) % 13
    return remainder == 0
```

#### 💻 Implementation

```cpp
// Optimized for very large numbers using modulo property

class Solution {
public:
    bool isDivisibleBy13(string s) {
        int remainder = 0;
        for (char c : s) {
            int digit = c - '0';
            remainder = (remainder * 10 + digit) % 13; // Update remainder
        }
        return remainder == 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Using Repeating Pattern for 13)

#### 📝 Intuition

> - There exists a known repeating pattern for powers of 10 modulo 13:
> - [1, 10, 9, 12, 3, 4].
> - Each digit contributes digit \* pattern[i % 6] modulo 13.
> - Sum contributions of all digits from least significant to most significant digit, then check sum % 13 == 0.
> - Elegant, O(n), O(1) space.

#### 🔍 Algorithm

```pseudo
function patternMethod(s):
    pattern = [1,10,9,12,3,4]
    sum = 0
    n = length of s
    for i in 0..n-1:
        digit = s[n-1-i] - '0'   // start from LSD
        sum += digit * pattern[i % 6]
        sum %= 13
    return sum == 0
```

#### 💻 Implementation

```cpp
// Optimal method using repeating pattern modulo 13

class Solution {
public:
    bool isDivisibleBy13(string s) {
        int pattern[6] = {1, 10, 9, 12, 3, 4};
        int sum = 0;
        int n = s.size();

        // Traverse from least significant digit
        for (int i = 0; i < n; i++) {
            int digit = s[n - 1 - i] - '0';
            sum = (sum + digit * pattern[i % 6]) % 13;
        }

        return sum == 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                             | Cons                           |
| -------------- | --------------- | ---------------- | -------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(n)            | O(1)             | Simple logic, easy to understand | Fails for very large numbers   |
| 🥈 Manual Mod  | O(n)            | O(1)             | Works for very large strings     | Slightly less “mathematical”   |
| 🥇 Pattern ⭐  | O(n)            | O(1)             | Elegant, uses modulo pattern     | Need to know repeating pattern |

---

<div align="center">

**🎯 Problem 897411 Completed!**

_Happy Coding! 🚀_

</div>
