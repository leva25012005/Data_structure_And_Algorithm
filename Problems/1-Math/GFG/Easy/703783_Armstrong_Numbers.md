<div align="center">

# 🧠 [Armstrong Numbers](https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703783`                                                                                                                                                          |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                       |
| **Accuracy**     | `49.88%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1)                                                                           |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![VMWare](https://img.shields.io/badge/-VMWare-orange?style=flat-square) ![Oracle](https://img.shields.io/badge/-Oracle-orange?style=flat-square)                 |

## Description

<!-- description:start -->

<p>You are given a <strong>3-digit</strong> number <code>n</code>. Determine whether it is an <strong>Armstrong number</strong> or not.</p>

<p>An <em>Armstrong number</em> of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3³ + 7³ + 1³ = 371.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 153
<strong>Output:</strong> true
<strong>Explanation:</strong> 153 is an Armstrong number since 1³ + 5³ + 3³ = 153.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 372
<strong>Output:</strong> false
<strong>Explanation:</strong> 372 is not an Armstrong number since 3³ + 7³ + 2³ = 378.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> false
<strong>Explanation:</strong> 100 is not an Armstrong number since 1³ + 0³ + 0³ = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>100 &lt;= n &lt; 1000</code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/cpp-program-to-check-armstrong-numbers/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/program-for-armstrong-numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert the number n to a string.
> - Extract each digit, cube it, and sum them.
> - Compare the sum to the original number.

#### 🔍 Algorithm

```pseudo
function isArmstrong(n):
    convert n to string s
    sum = 0
    for each digit d in s:
        sum += d^3
    return sum == n
```

#### 💻 Implementation

```cpp
// Brute force using string conversion

class Solution {
public:
    bool isArmstrong(int n) {
        string s = to_string(n); // Convert number to string
        int sum = 0;

        // Sum the cubes of digits
        for (char c : s) {
            int digit = c - '0';
            sum += digit * digit * digit;
        }

        // Check if sum equals the original number
        return sum == n;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Digit Extraction)

#### 📝 Intuition

> - Extract digits mathematically using division and modulo instead of converting to string.
> - Cube each digit and sum.
> - Compare the sum to the original number.

#### 🔍 Algorithm

```pseudo
function isArmstrong(n):
    a = n / 100           // hundreds digit
    b = (n / 10) % 10     // tens digit
    c = n % 10             // units digit
    return (a^3 + b^3 + c^3) == n
```

#### 💻 Implementation

```cpp
// Optimized using arithmetic

class Solution {
public:
    bool isArmstrong(int n) {
        int a = n / 100;       // hundreds digit
        int b = (n / 10) % 10; // tens digit
        int c = n % 10;        // units digit

        int sum = a*a*a + b*b*b + c*c*c; // sum of cubes
        return sum == n;                 // check equality
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - Since the number is always 3-digit, we can directly calculate using the formula: (hundreds digit)³ + (tens digit)³ + (units digit)³ == n
> - This uses O(1) time and O(1) space, which is exactly what the problem expects.

#### 🔍 Algorithm

```pseudo
function isArmstrong(n):
    return ((n / 100)^3 + ((n / 10) % 10)^3 + (n % 10)^3) == n
```

#### 💻 Implementation

```cpp
// Optimal constant-time solution

class Solution {
public:
    bool isArmstrong(int n) {
        return (n / 100)*(n / 100)*(n / 100) +
               ((n / 10) % 10)*((n / 10) % 10)*((n / 10) % 10) +
               (n % 10)*(n % 10)*(n % 10) == n;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                        | Cons                    |
| -------------- | --------------- | ---------------- | --------------------------- | ----------------------- |
| 🥉 Brute Force | O(1)            | O(d)             | Easy to implement, readable | Uses string conversion  |
| 🥈 Optimized   | O(1)            | O(1)             | Pure math, no extra storage | Slightly more code      |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Elegant, direct formula     | Hard-coded for 3 digits |

---

<div align="center">

**🎯 Problem 703783 Completed!**

_Happy Coding! 🚀_

</div>
