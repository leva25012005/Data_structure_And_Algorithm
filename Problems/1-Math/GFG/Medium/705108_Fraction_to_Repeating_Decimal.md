<div align="center">

# 🧠 [Fraction to Repeating Decimal](https://www.geeksforgeeks.org/problems/a-simple-fraction0921/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/a-simple-fraction0921/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `705108`                                                                                                                                                                                                                                                                                                                        |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                                   |
| **Accuracy**     | `23.12%`                                                                                                                                                                                                                                                                                                                        |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/a-simple-fraction0921/1)                                                                                                                                                                                                                                         |
| **Topic Tags**   | ![Hash](https://img.shields.io/badge/-Hash-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square)                                                                                                                                                                         |

## Description

<!-- description:start -->

<p>Given two integers <strong>a</strong> and <strong>b</strong>, the task is to convert the fraction <strong>a/b</strong> into decimal format. If the fractional part is repeating, enclose the repeating part in parentheses.</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> a = 50, b = 22
<strong>Output:</strong> "2.(27)"
<strong>Explanation:</strong> 50 / 22 = 2.272727... Since the fractional part (27) is repeating, it is enclosed in parentheses.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ a, b ≤ 2000</code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(max(log10(a), log10(b)))<br>
<strong>Expected Auxiliary Space:</strong> O(max(log10(a), log10(b)))</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `19-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `19-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-recurring-sequence-fraction/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/represent-the-fraction-of-two-numbers-in-the-string-format/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulate division)

#### 📝 Intuition

> - Perform long division manually: divide a by b digit by digit.
> - Keep track of the remainders.
> - If a remainder repeats, the fractional part starts repeating.
> - This approach follows the logic of long division exactly.

#### 🔍 Algorithm

```pseudo
function fractionToDecimal(a, b):
    integer_part = a / b
    remainder = a % b
    if remainder == 0:
        return integer_part as string

    result = integer_part + "."
    map = empty map to store remainder positions
    while remainder != 0:
        if remainder in map:
            insert '(' at map[remainder]
            append ')'
            break
        map[remainder] = current length of result
        remainder *= 10
        result += remainder / b
        remainder %= b
    return result
```

#### 💻 Implementation

```cpp
// Brute force: simulate long division

class Solution {
public:
    string fractionToDecimal(int a, int b) {
        string res;

        // Step 1: integer part
        int integer_part = a / b;
        res += to_string(integer_part);

        long long remainder = a % b;
        if (remainder == 0) return res; // No fractional part

        res += ".";

        // Step 2: store remainder positions
        unordered_map<long long, int> mp;

        while (remainder != 0) {
            if (mp.find(remainder) != mp.end()) {
                // repeating detected
                res.insert(mp[remainder], "(");
                res += ")";
                break;
            }
            mp[remainder] = res.size();
            remainder *= 10;
            res += to_string(remainder / b);
            remainder %= b;
        }

        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Mapping)

#### 📝 Intuition

> - Same logic as brute force but optimized for clarity and using long long to avoid overflow.
> - Track positions of remainders efficiently.
> - Elegant handling of repeating parts with string insertion.

#### 🔍 Algorithm

```pseudo
function optimizedFraction(a, b):
    result = integer part
    remainder = a % b
    map = remainder -> position in result
    while remainder != 0:
        if remainder in map:
            insert '(' at map[remainder], append ')'
            break
        map[remainder] = current length
        multiply remainder by 10, append quotient
        update remainder
    return result
```

#### 💻 Implementation

```cpp
// Optimized with long long to avoid overflow

class Solution {
public:
    string fractionToDecimal(int a, int b) {
        string res;

        // Convert to long long to avoid overflow
        long long numerator = a, denominator = b;
        long long integer_part = numerator / denominator;
        res += to_string(integer_part);

        long long remainder = numerator % denominator;
        if (remainder == 0) return res;

        res += ".";
        unordered_map<long long, int> mp;

        while (remainder != 0) {
            if (mp.count(remainder)) {
                res.insert(mp[remainder], "(");
                res += ")";
                break;
            }
            mp[remainder] = res.size();
            remainder *= 10;
            res += to_string(remainder / denominator);
            remainder %= denominator;
        }

        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Handle negative numbers and large integers.
> - Use long long for safe multiplication.
> - Detect repeating remainder using a map.
> - Elegant, minimal code with correct formatting.

#### 🔍 Algorithm

```pseudo
function optimalFraction(a, b):
    handle sign
    append integer part
    remainder = numerator % denominator
    map = remainder -> position
    while remainder != 0:
        if remainder seen: insert parentheses
        else: multiply remainder by 10, append quotient
    return result
```

#### 💻 Implementation

```cpp
// Optimal solution: handle negatives and repeating decimals

class Solution {
public:
    string fractionToDecimal(int a, int b) {
        if (a == 0) return "0";

        string res;
        // handle negative
        if ((a < 0) ^ (b < 0)) res += "-";

        long long numerator = abs((long long)a);
        long long denominator = abs((long long)b);

        // integer part
        res += to_string(numerator / denominator);
        long long remainder = numerator % denominator;
        if (remainder == 0) return res;

        res += ".";
        unordered_map<long long, int> mp;

        while (remainder != 0) {
            if (mp.count(remainder)) {
                res.insert(mp[remainder], "(");
                res += ")";
                break;
            }
            mp[remainder] = res.size();
            remainder *= 10;
            res += to_string(remainder / denominator);
            remainder %= denominator;
        }

        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                     | Cons                          |
| -------------- | --------------- | ---------------- | ---------------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(n)            | O(n)             | Follows long division step by step       | Handles only positive numbers |
| 🥈 Optimized   | O(n)            | O(n)             | Uses map for repeating remainder         | Slightly more code            |
| 🥇 Optimal ⭐  | O(n)            | O(n)             | Handles negatives, large integers, clean | Uses long long and map        |

---

<div align="center">

**🎯 Problem 705108 Completed!**

_Happy Coding! 🚀_

</div>
