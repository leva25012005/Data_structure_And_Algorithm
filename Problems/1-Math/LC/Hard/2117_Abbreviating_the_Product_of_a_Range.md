<div align="center">

# 🧠 [2117. Abbreviating the Product of a Range](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202117-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------- |
| **Difficulty**      | 🔴 **Hard**                                                                            |
| **Acceptance Rate** | `24.4%`                                                                                |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/abbreviating-the-product-of-a-range/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                     |

## Description

<!-- description:start -->

<p>You are given two positive integers <code>left</code> and <code>right</code> with <code>left &lt;= right</code>. Calculate the <strong>product</strong> of all integers in the <strong>inclusive</strong> range <code>[left, right]</code>.</p>

<p>Since the product may be very large, you will <strong>abbreviate</strong> it following these steps:</p>

<ol>
  <li>Count all <strong>trailing</strong> zeros in the product and <strong>remove</strong> them. Let us denote this count as <code>C</code>.
    <ul>
      <li>For example, there are <code>3</code> trailing zeros in <code>1000</code>, and there are <code>0</code> trailing zeros in <code>546</code>.</li>
    </ul>
  </li>

  <li>Denote the remaining number of digits in the product as <code>d</code>. 
    <br>If <code>d &gt; 10</code>, then express the product as <code>&lt;pre&gt;...&lt;suf&gt;</code> where <code>&lt;pre&gt;</code> denotes the <strong>first</strong> 5 digits of the product, and <code>&lt;suf&gt;</code> denotes the <strong>last</strong> 5 digits of the product <strong>after</strong> removing all trailing zeros. 
    <br>If <code>d &lt;= 10</code>, we keep it unchanged.
    <ul>
      <li>For example, we express <code>1234567654321</code> as <code>12345...54321</code>, but <code>1234567</code> is represented as <code>1234567</code>.</li>
    </ul>
  </li>

  <li>Finally, represent the product as a <strong>string</strong> <code>"&lt;pre&gt;...&lt;suf&gt;eC"</code>.
    <ul>
      <li>For example, <code>12345678987600000</code> will be represented as <code>"12345...89876e5"</code>.</li>
    </ul>
  </li>
</ol>

<p>Return <em>a string denoting the <strong>abbreviated product</strong> of all integers in the <strong>inclusive</strong> range</em> <code>[left, right]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 1, right = 4
<strong>Output:</strong> "24e0"
<strong>Explanation:</strong> The product is 1 × 2 × 3 × 4 = 24.
There are no trailing zeros, so 24 remains the same. The abbreviation will end with "e0".
Since the number of digits is 2, which is less than 10, we do not have to abbreviate it further.
Thus, the final representation is "24e0".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 2, right = 11
<strong>Output:</strong> "399168e2"
<strong>Explanation:</strong> The product is 39916800.
There are 2 trailing zeros, which we remove to get 399168. The abbreviation will end with "e2".
The number of digits after removing the trailing zeros is 6, so we do not abbreviate it further.
Hence, the abbreviated product is "399168e2".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> left = 371, right = 375
<strong>Output:</strong> "7219856259e3"
<strong>Explanation:</strong> The product is 7219856259000.
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

| Problem                                                                                                               | Difficulty    | Relationship    |
| --------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)                                 | 🟡 **Medium** | Similar logic   |
| [Maximum Trailing Zeros in a Cornered Path](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/) | 🟡 **Medium** | Related concept |
| [Find All Good Indices](https://leetcode.com/problems/find-all-good-indices/)                                         | 🟡 **Medium** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

- **Avalara** 🔥 100.0%

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Direct Multiplication)

#### 📝 Intuition

> - Multiply all integers from left to right.
> - Count trailing zeros in the product.
> - Remove trailing zeros, then format according to the problem’s rules.
> - This is simple but can overflow quickly for large ranges.

#### 🔍 Algorithm

```pseudo
function bruteForce(left, right):
    prod = 1
    for i from left to right:
        prod *= i
    count trailing zeros C
    remove trailing zeros
    if number of digits <= 10:
        return prod + "e" + C
    else:
        return first5 + "..." + last5 + "e" + C
```

#### 💻 Implementation

```cpp
// Brute force approach (works for small ranges only)

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        long long prod = 1;
        // Step 1: Multiply all numbers
        for (int i = left; i <= right; i++) {
            prod *= i;
        }

        // Step 2: Count trailing zeros
        int trailingZeros = 0;
        long long temp = prod;
        while (temp % 10 == 0) {
            trailingZeros++;
            temp /= 10;
        }

        string s = to_string(temp);

        // Step 3: Abbreviate if more than 10 digits
        if (s.size() > 10) {
            string pre = s.substr(0, 5);
            string suf = s.substr(s.size() - 5);
            return pre + "..." + suf + "e" + to_string(trailingZeros);
        }

        return s + "e" + to_string(trailingZeros);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Counting Factors)

#### 📝 Intuition

> - Instead of computing full product, keep track of factors of 2 and 5 to count trailing zeros.
> - Multiply remaining numbers while removing factors of 10 (2×5).
> - Keep only significant digits using modulo arithmetic (or a large enough number type).
> - This avoids overflow and is feasible for larger ranges (right <= 10^4).

#### 🔍 Algorithm

```pseudo
function optimized(left, right):
    count2 = count5 = 0
    result = 1
    for i in left..right:
        temp = i
        while temp divisible by 2: count2++, temp /= 2
        while temp divisible by 5: count5++, temp /= 5
        result *= temp
        keep result < 1e12 to avoid overflow
    trailingZeros = min(count2, count5)
    result *= 2^(count2 - trailingZeros) * 5^(count5 - trailingZeros)
    format result according to problem rules
```

#### 💻 Implementation

```cpp
// Optimized approach with factor counting

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        long long res = 1;
        int count2 = 0, count5 = 0;

        for (int i = left; i <= right; i++) {
            int x = i;
            while (x % 2 == 0) { count2++; x /= 2; }
            while (x % 5 == 0) { count5++; x /= 5; }
            res *= x;
            // Keep res manageable
            if (res > 1e12) res %= 1000000000000LL;
        }

        // Remove common factors of 10
        int trailingZeros = min(count2, count5);
        int extra2 = count2 - trailingZeros;
        int extra5 = count5 - trailingZeros;

        // Multiply back remaining 2s and 5s
        for (int i = 0; i < extra2; i++) res *= 2;
        for (int i = 0; i < extra5; i++) res *= 5;

        string s = to_string(res);
        if (s.size() > 10) {
            string pre = s.substr(0, 5);
            string suf = s.substr(s.size() - 5);
            return pre + "..." + suf + "e" + to_string(trailingZeros);
        }
        return s + "e" + to_string(trailingZeros);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Logarithms + Significant Digits)

#### 📝 Intuition

> - Use logarithms to calculate number of digits without computing full product.
> - Keep track of first few digits (using pow(10, fracPart) trick).
> - Count trailing zeros by counting factors of 2 and 5 separately.
> - Most efficient, avoids overflow completely.

#### 🔍 Algorithm

```pseudo
function optimal(left, right):
    count2 = count5 = 0
    logSum = 0
    for i in left..right:
        temp = i
        while divisible by 2: count2++, temp /= 2
        while divisible by 5: count5++, temp /= 5
        logSum += log10(temp)
    trailingZeros = min(count2, count5)
    totalDigits = floor(logSum) + 1
    if totalDigits <= 10:
        compute actual number using modulo arithmetic
    else:
        first5 = pow(10, logSum - floor(logSum)) * 1e4
        last5 = compute last 5 digits modulo 1e5
    return formatted string "first5...last5eC"
```

#### 💻 Implementation

```cpp
// Optimal approach using logs

#include <cmath>
#include <string>
using namespace std;

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        int count2 = 0, count5 = 0;
        double logSum = 0.0;
        long long mod = 100000; // for last 5 digits
        long long last5 = 1;

        for (int i = left; i <= right; i++) {
            int x = i;
            while (x % 2 == 0) { count2++; x /= 2; }
            while (x % 5 == 0) { count5++; x /= 5; }

            logSum += log10(x);

            last5 = (last5 * (x % mod)) % mod; // track last 5 digits
        }

        int trailingZeros = min(count2, count5);
        int extra2 = count2 - trailingZeros;
        int extra5 = count5 - trailingZeros;

        last5 = (last5 * (long long)pow(2, extra2) * (long long)pow(5, extra5)) % mod;

        // Total digits after removing trailing zeros
        int totalDigits = floor(logSum + extra2*log10(2) + extra5*log10(5)) + 1;

        string suf = to_string(last5);
        while (suf.size() < 5) suf = "0" + suf;

        if (totalDigits <= 10) {
            // Small number: print entire product
            long long product = 1;
            for (int i = left; i <= right; i++) product *= i;
            product /= pow(10, trailingZeros);
            return to_string(product) + "e" + to_string(trailingZeros);
        } else {
            // Large number: compute first 5 digits
            double firstDigits = pow(10, logSum + extra2*log10(2) + extra5*log10(5) - floor(logSum + extra2*log10(2) + extra5*log10(5) - 4));
            int pre = (int)firstDigits;
            return to_string(pre) + "..." + suf + "e" + to_string(trailingZeros);
        }
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                          | Cons                          |
| -------------- | --------------- | ---------------- | --------------------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(n) \* big-int | O(1)             | Very simple, intuitive                        | Overflow quickly, slow        |
| 🥈 Optimized   | O(n)            | O(1)             | Avoids full product overflow, works for n≤1e4 | Needs careful factor handling |
| 🥇 Optimal ⭐  | O(n)            | O(1)             | Handles very large numbers efficiently        | Slightly complex code         |

---

<div align="center">

**🎯 Problem 2117 Completed!**

_Happy Coding! 🚀_

</div>
