<div align="center">

# 🧠 [Odd or Even](https://www.geeksforgeeks.org/problems/odd-or-even3618/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/odd-or-even3618/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703724`                                                                                                                                                                                                                                                                                                                                    |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                                                                                                                |
| **Accuracy**     | `60.6%`                                                                                                                                                                                                                                                                                                                                     |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/odd-or-even3618/1)                                                                                                                                                                                                                                                           |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Bit Magic](https://img.shields.io/badge/-Bit%20Magic-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a positive integer <code>n</code>, determine whether it is odd or even. Return <code>true</code> if the number is even and <code>false</code> if the number is odd.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 15
<strong>Output:</strong> false
<strong>Explanation:</strong> The number is not divisible by 2, hence it is odd.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 44
<strong>Output:</strong> true
<strong>Explanation:</strong> The number is divisible by 2, hence it is even.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-whether-given-number-even-odd/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Division)

#### 📝 Intuition

> - The most basic way is to divide the number by 2.
> - If n % 2 == 0 → even → return true.
> - Otherwise → odd → return false.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    if n % 2 == 0:
        return true
    else:
        return false
```

#### 💻 Implementation

```cpp
// Brute force approach using modulo operator

class Solution {
public:
    bool isEven(int n) {
        // If remainder is 0, it's even
        if (n % 2 == 0) return true;
        else return false;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Return Condition Directly)

#### 📝 Intuition

> - No need for if-else.
> - Since (n % 2 == 0) itself is a boolean expression, just return it directly.
> - This reduces code size and improves readability.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    return (n % 2 == 0)
```

#### 💻 Implementation

```cpp
// Optimized approach returning condition directly

class Solution {
public:
    bool isEven(int n) {
        return (n % 2 == 0); // Direct boolean check
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Bitwise)

#### 📝 Intuition

> - A number is even if its least significant bit (LSB) is 0, and odd if its LSB is 1.
> - We can check this using bitwise operator: n & 1.
>   - If (n & 1) == 0 → even.
>   - If (n & 1) == 1 → odd.
> - This avoids modulo operation, and is very fast at the bit level.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return ((n & 1) == 0)
```

#### 💻 Implementation

```cpp
// Most optimal bitwise approach

class Solution {
public:
    bool isEven(int n) {
        // If last bit is 0 -> even
        return ((n & 1) == 0);
    }
};
```

## 📊 Comparison of Approaches

| Approach         | Time Complexity | Space Complexity | Pros                      | Cons                         |
| ---------------- | --------------- | ---------------- | ------------------------- | ---------------------------- |
| 🥉 Brute Force   | O(1)            | O(1)             | Very clear logic          | Slightly verbose             |
| 🥈 Optimized     | O(1)            | O(1)             | Clean, short code         | Still uses modulo operation  |
| 🥇 Optimal ⭐    | O(1)            | O(1)             | Fastest (bit-level check) | Less intuitive for beginners |
| Requires insight |

---

<div align="center">

**🎯 Problem 703724 Completed!**

_Happy Coding! 🚀_

</div>
