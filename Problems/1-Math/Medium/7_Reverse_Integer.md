<div align="center">

# 🧠 [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%207-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/reverse-integer/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟡 **Medium**                                                      |
| **Acceptance Rate** | `30.7%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/reverse-integer/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                                 | Difficulty    | Relationship    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                                                                       | 🟡 **Medium** | Similar logic   |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                                                                             | 🟢 **Easy**   | Related concept |
| [A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/)                                                     | 🟢 **Easy**   | Related concept |
| [Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Tech Mahindra** 🔥 88.9%
- **LTI** 🔥 88.8%
- **Wipro** 🔥 82.8%

### ⭐ Medium Frequency (60-79%)

- **Accenture** ⭐ 75.0%
- **Adobe** ⭐ 74.3%
- **Bloomberg** ⭐ 72.7%
- **Apple** ⭐ 71.6%
- **Deloitte** ⭐ 69.7%
- **Intel** ⭐ 69.6%
- **Cognizant** ⭐ 66.5%
- **Amazon** ⭐ 65.3%
- **Microsoft** ⭐ 62.5%
- **Infosys** ⭐ 62.1%

### 📈 Regular Frequency (40-59%)

- **tcs** 📈 59.9%
- **Qualcomm** 📈 56.6%
- **EPAM Systems** 📈 56.5%
- **Uber** 📈 53.3%
- **Yahoo** 📈 51.6%
- **Meta** 📈 49.4%
- **Nvidia** 📈 47.7%
- **Samsung** 📈 44.4%

### 📊 Low Frequency Companies

- **Yandex** 📊 35.9%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert the integer into a string.
> - Handle the sign separately.
> - Reverse the digits in string form and convert back to integer.
> - If the result exceeds 32-bit signed integer range → return 0.
> - This approach is straightforward but relies on string conversion.

#### 🔍 Algorithm

```pseudo
function bruteForce(x):
    if x < 0:
        sign = -1
    else:
        sign = +1
    s = string(abs(x))
    reverse(s)
    result = int(s) * sign
    if result < -2^31 or result > 2^31-1:
        return 0
    return result
```

#### 💻 Implementation

```cpp
// Brute force solution using string conversion

class Solution {
public:
    int reverse(int x) {
        // Handle sign
        int sign = (x < 0) ? -1 : 1;
        string s = to_string(abs(x));

        // Reverse the string
        std::reverse(s.begin(), s.end());

        // Convert back to integer (long long to detect overflow)
        long long res = stoll(s) * sign;

        // Check overflow
        if (res < INT_MIN || res > INT_MAX) return 0;
        return (int)res;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Avoid strings.
> - Pop digits from the original number using % 10.
> - Push digits into the reversed number using res = res \* 10 + digit.
> - Check for overflow before pushing.
> - This avoids string overhead and is more efficient.

#### 🔍 Algorithm

```pseudo
function optimized(x):
    res = 0
    while x != 0:
        digit = x % 10
        x = x / 10
        if res > INT_MAX/10 or res < INT_MIN/10:
            return 0
        res = res * 10 + digit
    return res
```

#### 💻 Implementation

```cpp
// Optimized approach using math

class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int digit = x % 10; // Get last digit
            x /= 10;            // Remove last digit

            // Check for overflow before updating res
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && digit > 7)) return 0;
            if (res < INT_MIN / 10 || (res == INT_MIN / 10 && digit < -8)) return 0;

            res = res * 10 + digit;
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Early Overflow Detection)

#### 📝 Intuition

> The optimized approach is already quite efficient, but we can make it more elegant by:
>
> - Using the same math approach.
> - Explicitly checking overflow before multiplying by 10 and adding digit.
> - This ensures no risk of undefined behavior.
> - This is the cleanest and safest version.

#### 🔍 Algorithm

```pseudo
function optimal(x):
    res = 0
    while x != 0:
        digit = x % 10
        x = x / 10
        if res > (INT_MAX - digit) / 10: return 0
        if res < (INT_MIN - digit) / 10: return 0
        res = res * 10 + digit
    return res
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // Early check for overflow
            if (res > (INT_MAX - digit) / 10) return 0;
            if (res < (INT_MIN - digit) / 10) return 0;

            res = res * 10 + digit;
        }
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                           |
| -------------- | --------------- | ---------------- | ----------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(d)            | O(d)             | Very easy, uses built-in string ops | Slower, not pure math          |
| 🥈 Optimized   | O(d)            | O(1)             | Efficient math-only approach        | Needs explicit overflow checks |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Elegant, safest overflow handling   | Slightly trickier logic        |

---

<div align="center">

**🎯 Problem 7 Completed!**

_Happy Coding! 🚀_

</div>
