<div align="center">

# 🧠 [1017. Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201017-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/convert-to-base-2/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                |
| ------------------- | -------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                        |
| **Acceptance Rate** | `61.4%`                                                              |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/convert-to-base-2/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)   |

## Description

<!-- description:start -->

<p>Given an integer <code>n</code>, return <em>a binary string representing its representation in base</em> <code>-2</code>.</p>

<p><strong>Note</strong> that the returned string should not have leading zeros unless the string is <code>&quot;0&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> &quot;110&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> + (-2)<sup>1</sup> = 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> &quot;111&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> + (-2)<sup>1</sup> + (-2)<sup>0</sup> = 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> &quot;100&quot;
<strong>Explantion:</strong> (-2)<sup>2</sup> = 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
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

| Problem                                                                         | Difficulty    | Relationship    |
| ------------------------------------------------------------------------------- | ------------- | --------------- |
| [Encode Number](https://leetcode.com/problems/encode-number/)                   | 🟡 **Medium** | Similar logic   |
| [Convert Date to Binary](https://leetcode.com/problems/convert-date-to-binary/) | 🟢 **Easy**   | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Airbnb** ⭐ 70.4%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation with Repeated Division)

#### 📝 Intuition

> - The base conversion is similar to standard base conversion.
> - Repeatedly divide the number by -2, keeping track of the remainder.
> - Special care: when remainder is negative, adjust by adding 2 and increasing the quotient.
> - Store remainders, then reverse them to form the binary string.
> - This is the straightforward simulation of base conversion.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    if n == 0: return "0"
    result = ""
    while n != 0:
        remainder = n % -2
        n = n / -2
        if remainder < 0:
            remainder += 2
            n += 1
        result.append(remainder as char)
    reverse(result)
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach: simulate base conversion

class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0) return "0";
        string res = "";
        while (n != 0) {
            int remainder = n % -2;
            n /= -2;
            if (remainder < 0) {
                remainder += 2;
                n += 1;
            }
            res.push_back(remainder + '0'); // store digit
        }
        reverse(res.begin(), res.end()); // digits are collected in reverse
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Bitwise Thinking)

#### 📝 Intuition

> - Notice that in base -2, every remainder must be 0 or 1.
> - Instead of worrying about negatives, adjust directly with (n % 2 + 2) % 2.
> - Update quotient with (n - remainder)/-2.
> - This avoids manual correction logic.
> - Cleaner and less error-prone.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    if n == 0: return "0"
    result = ""
    while n != 0:
        remainder = (n % 2 + 2) % 2
        result.append(remainder)
        n = (n - remainder) / -2
    reverse(result)
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach using modulo trick

class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0) return "0";
        string res = "";
        while (n != 0) {
            int remainder = (n % 2 + 2) % 2; // always 0 or 1
            res.push_back(remainder + '0');
            n = (n - remainder) / -2; // adjust n
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Bitwise Insight)

#### 📝 Intuition

> - Another observation: The result length is at most 32 bits since n ≤ 10^9.
> - We can repeatedly extract bits with bit operations.
> - Equivalent to: while n != 0, append (n & 1) and update n = -(n >> 1).
> - Very elegant, one-pass, no need for explicit division.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    if n == 0: return "0"
    result = ""
    while n != 0:
        bit = n & 1   // get last bit
        result.append(bit)
        n = -(n >> 1) // shift and negate
    reverse(result)
    return result
```

#### 💻 Implementation

```cpp
// Most optimal approach: bitwise method

class Solution {
public:
    string baseNeg2(int n) {
        if (n == 0) return "0";
        string res = "";
        while (n != 0) {
            int bit = n & 1;               // extract lowest bit
            res.push_back(bit + '0');
            n = -(n >> 1);                 // shift right and negate
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                         | Cons                        |
| -------------- | --------------- | ---------------- | -------------------------------------------- | --------------------------- |
| 🥉 Brute Force | O(log n)        | O(log n)         | Very intuitive, simulates manual division    | Manual remainder correction |
| 🥈 Optimized   | O(log n)        | O(log n)         | Cleaner, uses modulo trick, less error-prone | Still uses arithmetic ops   |
| 🥇 Optimal ⭐  | O(log n)        | O(log n)         | Elegant bitwise solution, very concise       | Trickier to understand      |

---

<div align="center">

**🎯 Problem 1017 Completed!**

_Happy Coding! 🚀_

</div>
