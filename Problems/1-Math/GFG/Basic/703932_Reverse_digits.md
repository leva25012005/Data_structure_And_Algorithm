<div align="center">

# 🧠 [Reverse digits](https://www.geeksforgeeks.org/problems/reverse-digit0316/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/reverse-digit0316/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703932`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `46.92%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/reverse-digit0316/1)                                                                               |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![MAQ Software](https://img.shields.io/badge/-MAQ%20Software-orange?style=flat-square)                                                                            |

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code>. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 122
<strong>Output:</strong> 221
<strong>Explanation:</strong> By reversing the digits of the number, it becomes 221.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 200
<strong>Output:</strong> 2
<strong>Explanation:</strong> By reversing the digits of the number, it becomes 2 (leading zeroes are removed).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 12345
<strong>Output:</strong> 54321
<strong>Explanation:</strong> By reversing the digits of the number, it becomes 54321.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(log n)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/reverse-number-program-in-cpp/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Reversal)

#### 📝 Intuition

> - Convert the number to a string.
> - Reverse the string.
> - Convert back to integer (this automatically removes leading zeros).
> - Very straightforward but uses string operations.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    s = to_string(n)
    reverse(s)
    return stoi(s)  // converts back to int, removing leading zeros
```

#### 💻 Implementation

```cpp
// Brute force approach using string reversal

class Solution {
public:
    int reverseNumber(int n) {
        string s = to_string(n);        // Convert number to string
        reverse(s.begin(), s.end());    // Reverse string
        return stoi(s);                 // Convert back to integer (removes leading zeros)
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math-based Reversal)

#### 📝 Intuition

> - Instead of converting to string, we can reverse the number mathematically:
>   - Extract the last digit using % 10.
>   - Append it to the reversed number.
>   - Remove the last digit using / 10.
> - This avoids extra string operations.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    res = 0
    while n > 0:
        digit = n % 10
        res = res * 10 + digit
        n = n / 10
    return res
```

#### 💻 Implementation

```cpp
// Optimized approach using math operations

class Solution {
public:
    int reverseNumber(int n) {
        int res = 0;
        while (n > 0) {
            int digit = n % 10;         // Extract last digit
            res = res * 10 + digit;     // Append digit to result
            n /= 10;                    // Remove last digit
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Early Skip Zeros)

#### 📝 Intuition

> - Even with math reversal, if the number ends with zeros, we multiply unnecessary times at first.
> - We can skip trailing zeros right away before reversal starts.
> - Then perform normal reversal.
> - This slightly optimizes cases like 200000, reducing redundant steps.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    while n % 10 == 0:
        n /= 10   // remove trailing zeros
    res = 0
    while n > 0:
        digit = n % 10
        res = res * 10 + digit
        n /= 10
    return res
```

#### 💻 Implementation

```cpp
// Most optimal approach: skip trailing zeros first

class Solution {
public:
    int reverseNumber(int n) {
        // Step 1: Remove trailing zeros
        while (n % 10 == 0 && n > 0) {
            n /= 10;
        }

        // Step 2: Reverse digits
        int res = 0;
        while (n > 0) {
            int digit = n % 10;         // Extract last digit
            res = res * 10 + digit;     // Append digit
            n /= 10;                    // Remove last digit
        }
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                       | Cons                       |
| -------------- | --------------- | ---------------- | -------------------------- | -------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very easy to implement     | Uses extra string memory   |
| 🥈 Optimized   | O(d)            | O(1)             | No string conversion       | Still processes all digits |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Skips trailing zeros early | Slightly more logic needed |

---

<div align="center">

**🎯 Problem 703932 Completed!**

_Happy Coding! 🚀_

</div>
