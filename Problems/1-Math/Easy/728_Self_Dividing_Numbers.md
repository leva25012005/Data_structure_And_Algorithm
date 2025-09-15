<div align="center">

# 🧠 [728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20728-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/self-dividing-numbers/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                              |
| **Acceptance Rate** | `79.8%`                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/self-dividing-numbers/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)       |

## Description

<!-- description:start -->

<p>A <strong>self-dividing number</strong> is a number that is divisible by every digit it contains.</p>

<ul>
	<li>For example, <code>128</code> is <strong>a self-dividing number</strong> because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.</li>
</ul>

<p>A <strong>self-dividing number</strong> is not allowed to contain the digit zero.</p>

<p>Given two integers <code>left</code> and <code>right</code>, return <em>a list of all the <strong>self-dividing numbers</strong> in the range</em> <code>[left, right]</code> (both <strong>inclusive</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> left = 1, right = 22
<strong>Output:</strong> [1,2,3,4,5,6,7,8,9,11,12,15,22]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> left = 47, right = 85
<strong>Output:</strong> [48,55,66,77]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                       | Difficulty  | Relationship    |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Perfect Number](https://leetcode.com/problems/perfect-number/)                                                                               | 🟢 **Easy** | Similar logic   |
| [Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) | 🟢 **Easy** | Related concept |
| [Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)                                 | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Epic Systems** 🔥 89.3%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check Each Digit with String Conversion)

#### 📝 Intuition

> - Convert each number to string.
> - For each digit:
> - If digit is 0 → not valid.
> - Else check if num % digit == 0.
> - If all digits satisfy the condition → it’s a self-dividing number.
> - This is simple but string conversion adds extra overhead.

#### 🔍 Algorithm

```pseudo
function bruteForce(left, right):
    result = []
    for num in range(left, right+1):
        s = str(num)
        valid = true
        for ch in s:
            d = int(ch)
            if d == 0 or num % d != 0:
                valid = false
                break
        if valid:
            result.append(num)
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach using string conversion

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for (int num = left; num <= right; num++) {
            string s = to_string(num);
            bool valid = true;
            for (char c : s) {
                int d = c - '0';
                if (d == 0 || num % d != 0) { // Fail condition
                    valid = false;
                    break;
                }
            }
            if (valid) ans.push_back(num);
        }
        return ans;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Instead of converting to string, extract digits mathematically.
> - Check divisibility for each digit.
> - Skip numbers that contain digit 0.
> - This avoids string operations, slightly more efficient.

#### 🔍 Algorithm

```pseudo
function optimized(left, right):
    result = []
    for num in [left..right]:
        temp = num
        valid = true
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                valid = false
                break
            temp = temp // 10
        if valid:
            result.append(num)
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach with math-based digit extraction

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for (int num = left; num <= right; num++) {
            int temp = num;
            bool valid = true;
            while (temp > 0) {
                int d = temp % 10;  // Get last digit
                if (d == 0 || num % d != 0) { // Invalid if digit is 0 or not divisible
                    valid = false;
                    break;
                }
                temp /= 10; // Remove last digit
            }
            if (valid) ans.push_back(num);
        }
        return ans;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Helper Function + Early Break)

#### 📝 Intuition

> - Encapsulate the digit-checking logic into a helper function isSelfDividing(num).
> - Iterate through the range [left..right], add only valid numbers.
> - Using early breaks inside the helper function improves readability and avoids redundant checks.
> - Still O(d \* (right-left)) but clean and elegant.

#### 🔍 Algorithm

```pseudo
function isSelfDividing(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            return false
        temp = temp // 10
    return true

function optimal(left, right):
    result = []
    for num in [left..right]:
        if isSelfDividing(num):
            result.append(num)
    return result
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution with helper function

class Solution {
public:
    // Check if a number is self-dividing
    bool isSelfDividing(int num) {
        int temp = num;
        while (temp > 0) {
            int d = temp % 10;
            if (d == 0 || num % d != 0) return false; // Fail condition
            temp /= 10;
        }
        return true;
    }

    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for (int num = left; num <= right; num++) {
            if (isSelfDividing(num)) ans.push_back(num);
        }
        return ans;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity      | Space Complexity | Pros                              | Cons                              |
| -------------- | -------------------- | ---------------- | --------------------------------- | --------------------------------- |
| 🥉 Brute Force | O((right-left) \* d) | O(d)             | Easy to implement with strings    | Slightly slower due to string ops |
| 🥈 Optimized   | O((right-left) \* d) | O(1)             | Faster (pure math, no string ops) | Code a bit longer                 |
| 🥇 Optimal ⭐  | O((right-left) \* d) | O(1)             | Clean, reusable helper function   | Same complexity, but elegant      |

- Here d = number of digits (≤ 5 since right ≤ 10^4).

<div align="center">

**🎯 Problem 728 Completed!**

_Happy Coding! 🚀_

</div>
