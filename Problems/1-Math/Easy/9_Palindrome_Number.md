<div align="center">

# 🧠 [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%209-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/palindrome-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                |
| ------------------- | -------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                          |
| **Acceptance Rate** | `59.5%`                                                              |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/palindrome-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)   |

## Description

<!-- description:start -->

<p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?

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

| Problem                                                                                                                 | Difficulty    | Relationship    |
| ----------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                                         | 🟢 **Easy**   | Similar logic   |
| [Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length/)                   | 🟡 **Medium** | Related concept |
| [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/)                               | 🟡 **Medium** | Related concept |
| [ Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers/)                                    | 🟢 **Easy**   | Related concept |
| [Find the Count of Good Integers](https://leetcode.com/problems/find-the-count-of-good-integers/)                       | 🔴 **Hard**   | Related concept |
| [Find the Largest Palindrome Divisible by K](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/) | 🔴 **Hard**   | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Cognizant** 🔥 100.0%
- **Roche** 🔥 100.0%
- **Garmin** 🔥 89.2%
- **Accenture** 🔥 85.8%

### ⭐ Medium Frequency (60-79%)

- **Deloitte** ⭐ 76.9%
- **Infosys** ⭐ 76.7%
- **tcs** ⭐ 76.6%
- **HCL** ⭐ 75.5%
- **Bloomberg** ⭐ 74.5%
- **persistent systems** ⭐ 73.2%
- **Wipro** ⭐ 70.1%
- **Adobe** ⭐ 68.6%
- **Apple** ⭐ 68.0%
- **Microsoft** ⭐ 67.5%
- **Capgemini** ⭐ 67.1%
- **Amazon** ⭐ 66.9%
- **Qualcomm** ⭐ 66.9%
- **EPAM Systems** ⭐ 66.8%
- **FPT** ⭐ 66.6%
- **Yahoo** ⭐ 62.9%
- **Samsung** ⭐ 61.0%

### 📈 Regular Frequency (40-59%)

- **Intel** 📈 59.5%
- **Meta** 📈 57.0%
- **Capital One** 📈 54.8%
- **Zoho** 📈 52.5%
- **Uber** 📈 47.3%
- **IBM** 📈 44.1%
- **Visa** 📈 42.9%

### 📊 Low Frequency Companies

- **Oracle** 📊 39.7%
- **Walmart Labs** 📊 36.8%
- **J.P. Morgan** 📊 36.3%
- **Yandex** 📊 35.9%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Conversion)

#### 📝 Intuition

> - Convert the integer x into a string.
> - A palindrome means the string equals its reverse.
> - Return true if they match, else false.

#### 🔍 Algorithm

```pseudo
function bruteForce(x):
    if x < 0: return false
    s = convert x to string
    return (s == reverse(s))
```

#### 💻 Implementation

```cpp
// Brute force solution using string conversion

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false; // Negative numbers are never palindromes

        string s = to_string(x);
        string rev = s;
        reverse(rev.begin(), rev.end()); // Reverse string

        return s == rev;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Compare from Both Ends)

#### 📝 Intuition

> - Instead of fully reversing the string, just compare digits from left and right at the same time.
> - If at any point they differ → return false.
> - This avoids building a reversed copy.

#### 🔍 Algorithm

```pseudo
function optimized(x):
    if x < 0: return false
    s = convert x to string
    left = 0, right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return false
        left++, right--
    return true
```

#### 💻 Implementation

```cpp
// Optimized string approach with two pointers

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        string s = to_string(x);
        int left = 0, right = s.size() - 1;

        while (left < right) {
            if (s[left] != s[right]) return false; // Mismatch
            left++;
            right--;
        }
        return true; // All digits matched
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Math Reversal Without String)

#### 📝 Intuition

> - Avoid using extra space or string conversion.
>   - Reverse only half of the number:
>   - Compare left half and reversed right half.
> - If they match, it’s a palindrome.
> - This prevents integer overflow and saves space.

#### 🔍 Algorithm

```pseudo
function optimal(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return false

    reversedHalf = 0
    while x > reversedHalf:
        reversedHalf = reversedHalf * 10 + x % 10
        x = x // 10

    return (x == reversedHalf) or (x == reversedHalf // 10)
```

#### 💻 Implementation

```cpp
// Most optimal math-based solution without converting to string

class Solution {
public:
    bool isPalindrome(int x) {
        // Special cases: negatives and multiples of 10 (except 0)
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int reversedHalf = 0;
        // Reverse only half of the number
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        // For odd-length numbers, ignore the middle digit (reversedHalf/10)
        return (x == reversedHalf) || (x == reversedHalf / 10);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                    | Cons                          |
| -------------- | --------------- | ---------------- | --------------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple with string conversion      | Extra memory for reverse copy |
| 🥈 Optimized   | O(d)            | O(1)             | Two-pointer check, no extra string copy | Still uses string conversion  |
| 🥇 Optimal ⭐  | O(d/2)          | O(1)             | Fastest, pure math, no string at all    | Slightly harder to implement  |

---

<div align="center">

**🎯 Problem 9 Completed!**

_Happy Coding! 🚀_

</div>
