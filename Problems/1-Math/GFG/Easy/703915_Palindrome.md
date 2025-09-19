<div align="center">

# 🧠 [Palindrome](https://www.geeksforgeeks.org/problems/palindrome0746/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/palindrome0746/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703915`                                                                                                                                                                                                                                                                                        |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                                                     |
| **Accuracy**     | `56.28%`                                                                                                                                                                                                                                                                                        |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/palindrome0746/1)                                                                                                                                                                                                                |
| **Topic Tags**   | ![palindrome](https://img.shields.io/badge/-palindrome-blue?style=flat-square)                                                                                                                                                                                                                  |
| **Company Tags** | ![Zoho](https://img.shields.io/badge/-Zoho-orange?style=flat-square) ![Samsung](https://img.shields.io/badge/-Samsung-orange?style=flat-square) ![Oracle](https://img.shields.io/badge/-Oracle-orange?style=flat-square) ![Adobe](https://img.shields.io/badge/-Adobe-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, determine whether it is a palindrome.</p>

<blockquote>
<p>A number is considered a palindrome if it reads the same backward as forward. For example: "MADAM", "MOM", or 1221.</p>
</blockquote>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 555
<strong>Output:</strong> true
<strong>Explanation:</strong> The number 555 reads the same backward as forward.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 123
<strong>Output:</strong> false
<strong>Explanation:</strong> The number 123 reads differently backward (321).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1221
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 ≤ n ≤ 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(d), where d is the number of digits in n<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/cpp-program-to-check-whether-a-number-is-palindrome-or-not/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Convert to String)

#### 📝 Intuition

> - Convert the number to a string.
> - Compare the string with its reverse.
> - If they are equal, the number is a palindrome.
> - This is simple but uses extra space for the string.

#### 🔍 Algorithm

```pseudo
function isPalindrome(n):
    s = string representation of n
    return s == reverse(s)
```

#### 💻 Implementation

```cpp
// Brute force: convert number to string

class Solution {
public:
    bool isPalindrome(int n) {
        string s = to_string(n);      // Convert number to string
        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end()); // Reverse string
        return s == rev_s;             // Compare original and reversed
    }
};
```

### 🥈 Approach 2: Optimized Solution (Digit Comparison)

#### 📝 Intuition

> - Extract digits one by one using math.
> - Compare digits from front and back until the middle.
> - Stop early if any mismatch is found.
> - No string conversion is needed; uses O(d) time and O(1) space.

#### 🔍 Algorithm

```pseudo
function isPalindrome(n):
    digits = extract digits of n into array
    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return false
        i += 1
        j -= 1
    return true
```

#### 💻 Implementation

```cpp
// Optimized approach: digit array comparison

class Solution {
public:
    bool isPalindrome(int n) {
        vector<int> digits;
        int temp = n;
        // Extract digits (right to left)
        while (temp > 0) {
            digits.push_back(temp % 10);
            temp /= 10;
        }

        int i = 0, j = digits.size() - 1;
        while (i < j) {
            if (digits[i] != digits[j]) return false; // Mismatch found
            i++;
            j--;
        }
        return true;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Reverse Half Number)

#### 📝 Intuition

> - Reverse only the second half of the number.
> - Compare the reversed half with the first half.
> - Handles O(1) extra space and is elegant.
> - This is the standard approach for numeric palindrome problems.

#### 🔍 Algorithm

```pseudo
function isPalindrome(n):
    if n < 0: return false
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n = n // 10
    return n == reversed_half or n == reversed_half // 10
```

#### 💻 Implementation

```cpp
// Optimal approach: reverse half the number

class Solution {
public:
    bool isPalindrome(int n) {
        if (n < 0) return false; // Negative numbers are not palindromes

        int reversed_half = 0;
        int original = n;
        while (n > reversed_half) {
            reversed_half = reversed_half * 10 + n % 10; // Add last digit to reversed_half
            n /= 10; // Remove last digit from n
        }

        // If even number of digits: n == reversed_half
        // If odd number of digits: n == reversed_half / 10
        return n == reversed_half || n == reversed_half / 10;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                     | Cons                                 |
| -------------- | --------------- | ---------------- | ---------------------------------------- | ------------------------------------ |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, easy to implement           | Extra space for string               |
| 🥈 Optimized   | O(d)            | O(d)             | No string conversion, direct digit check | Stores digit array                   |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Elegant, uses constant extra space       | Slightly tricky logic for odd digits |

---

<div align="center">

**🎯 Problem 703915 Completed!**

_Happy Coding! 🚀_

</div>
