<div align="center">

# 🧠 [2544. Alternating Digit Sum](https://leetcode.com/problems/alternating-digit-sum/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202544-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/alternating-digit-sum/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                              |
| **Acceptance Rate** | `68.5%`                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/alternating-digit-sum/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)       |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>n</code>. Each digit of <code>n</code> has a sign according to the following rules:</p>

<ul>
	<li>The <strong>most significant digit</strong> is assigned a <strong>positive</strong> sign.</li>
	<li>Each other digit has an opposite sign to its adjacent digits.</li>
</ul>

<p>Return <em>the sum of all digits with their corresponding sign</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 521
<strong>Output:</strong> 4
<strong>Explanation:</strong> (+5) + (-2) + (+1) = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 111
<strong>Output:</strong> 1
<strong>Explanation:</strong> (+1) + (-1) + (+1) = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 886996
<strong>Output:</strong> 0
<strong>Explanation:</strong> (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>

<!-- description:end -->

## Solutions

<!-- solution:start -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09=2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09=2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                           | Difficulty  | Relationship    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------- |
| [Add Digits](https://leetcode.com/problems/add-digits/)                                                                                           | 🟢 **Easy** | Similar logic   |
| [Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) | 🟢 **Easy** | Related concept |
| [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/)                                                 | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **eBay** 🔥 95.1%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert the number n into a string so we can easily access its digits.
> - Traverse the digits from left to right.
> - Add or subtract depending on whether the position is even or odd (starting with + at index 0).

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    convert n to string s
    result = 0
    for i in range(0, len(s)):
        digit = int(s[i])
        if i is even: result += digit
        else: result -= digit
    return result
```

#### 💻 Implementation

```cpp
// Brute force solution using string conversion

class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);  // Convert number to string
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            int digit = s[i] - '0'; // Extract digit
            if (i % 2 == 0) res += digit; // Even index -> add
            else res -= digit;           // Odd index -> subtract
        }
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Instead of converting to string, extract digits mathematically.
> - First, get the total number of digits.
> - Then traverse from most significant digit (MSD) to least significant digit (LSD), alternating signs.
> - This avoids extra string operations.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    digits = extract digits of n into array
    result = 0
    for i in 0..len(digits)-1:
        if i is even: result += digits[i]
        else: result -= digits[i]
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach using math-based digit extraction

class Solution {
public:
    int alternateDigitSum(int n) {
        vector<int> digits;
        // Extract digits from right to left
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        reverse(digits.begin(), digits.end()); // Reverse to get correct order

        int res = 0;
        for (int i = 0; i < digits.size(); i++) {
            if (i % 2 == 0) res += digits[i]; // Even index -> add
            else res -= digits[i];           // Odd index -> subtract
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (One-pass, sign flipping)

#### 📝 Intuition

> - Traverse digits directly without extra storage.
> - Keep a sign variable that flips between +1 and -1 at each step.
> - Start from the most significant digit to respect the problem’s rule.
> - Achieved by first computing the total length (digit count), then processing digits in the right order.
> - This is elegant, uses O(1) space.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    len = number of digits in n
    sign = +1
    result = 0
    for i in range(len):
        d = extract most significant remaining digit
        result += sign * d
        sign *= -1   // flip sign
    return result
```

#### 💻 Implementation

```cpp
// Most optimal approach: O(1) space with sign flipping

class Solution {
public:
    int alternateDigitSum(int n) {
        // Step 1: Convert to string just to get digit count
        string s = to_string(n);
        int len = s.size();

        int res = 0;
        int sign = 1; // Start with +1 for the most significant digit

        // Step 2: Traverse directly from MSD to LSD
        for (int i = 0; i < len; i++) {
            int digit = s[i] - '0';
            res += sign * digit;
            sign *= -1; // Flip sign after each digit
        }
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                  | Cons                       |
| -------------- | --------------- | ---------------- | ------------------------------------- | -------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, easy to implement        | Uses string conversion     |
| 🥈 Optimized   | O(d)            | O(d)             | Avoids string ops, pure math solution | Needs digit reversal       |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Cleanest, no extra storage            | Requires careful sign flip |

---

<div align="center">

**🎯 Problem 2544 Completed!**

_Happy Coding! 🚀_

</div>
