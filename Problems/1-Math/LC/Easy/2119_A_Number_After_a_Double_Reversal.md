<div align="center">

# 🧠 [2119. A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202119-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/a-number-after-a-double-reversal/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                         |
| **Acceptance Rate** | `81.4%`                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/a-number-after-a-double-reversal/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                  |

## Description

<!-- description:start -->

<p><strong>Reversing</strong> an integer means to reverse all its digits.</p>

<ul>
	<li>For example, reversing <code>2021</code> gives <code>1202</code>. Reversing <code>12300</code> gives <code>321</code> as the <strong>leading zeros are not retained</strong>.</li>
</ul>

<p>Given an integer <code>num</code>, <strong>reverse</strong> <code>num</code> to get <code>reversed1</code>, <strong>then reverse</strong> <code>reversed1</code> to get <code>reversed2</code>. Return <code>true</code> <em>if</em> <code>reversed2</code> <em>equals</em> <code>num</code>. Otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 526
<strong>Output:</strong> true
<strong>Explanation:</strong> Reverse num to get 625, then reverse 625 to get 526, which equals num.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 1800
<strong>Output:</strong> false
<strong>Explanation:</strong> Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> Reverse num to get 0, then reverse 0 to get 0, which equals num.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>6</sup></code></li>
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

| Problem                                                           | Difficulty    | Relationship    |
| ----------------------------------------------------------------- | ------------- | --------------- |
| [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | 🟡 **Medium** | Similar logic   |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/)       | 🟢 **Easy**   | Related concept |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String Reversal Twice)

#### 📝 Intuition

> - Convert the integer num into a string.
> - Reverse it once → reversed1.
> - Reverse reversed1 again → reversed2.
> - Convert back to integer (which will remove leading zeros automatically).
> - Compare with the original number.
> - This is the most straightforward solution.

#### 🔍 Algorithm

```pseudo
function bruteForce(num):
    s1 = string(num)
    reversed1 = reverse(s1)
    reversed2 = reverse(reversed1)
    return int(reversed2) == num
```

#### 💻 Implementation

```cpp
// Brute force solution using string reversal twice

class Solution {
public:
    bool isSameAfterReversals(int num) {
        string s1 = to_string(num);

        // Reverse first time
        reverse(s1.begin(), s1.end());
        int rev1 = stoi(s1);

        // Reverse second time
        string s2 = to_string(rev1);
        reverse(s2.begin(), s2.end());
        int rev2 = stoi(s2);

        return rev2 == num;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Single Check with Math)

#### 📝 Intuition

> - When you reverse twice, leading zeros disappear in the first reversal and never come back.
> - Example: 1800 → 81 → 18 ≠ 1800.
> - Only numbers that don’t end with zero will stay the same after double reversal.
> - Exception: 0 itself is fine.
> - So the rule is:
> - If num == 0 → return true.
> - Else, return num % 10 != 0.

#### 🔍 Algorithm

```pseudo
function optimized(num):
    if num == 0: return true
    return num % 10 != 0
```

#### 💻 Implementation

```cpp
// Optimized approach using mathematical property

class Solution {
public:
    bool isSameAfterReversals(int num) {
        if (num == 0) return true;
        // If the number ends with zero, double reversal will remove trailing zero
        return num % 10 != 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (One-liner Logic)

#### 📝 Intuition

> - ame as approach 2 but even cleaner:
>   - eturn true if the number is 0 or does not end with 0.
> - his makes the code a one-liner.

#### 🔍 Algorithm

```pseudo
function optimal(num):
    return (num == 0) OR (num % 10 != 0)
```

#### 💻 Implementation

```cpp
// Most optimal solution (one-liner)

class Solution {
public:
    bool isSameAfterReversals(int num) {
        return (num == 0 || num % 10 != 0);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                      | Cons                                  |
| -------------- | --------------- | ---------------- | ----------------------------------------- | ------------------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very intuitive, follows problem literally | Uses string ops, unnecessary          |
| 🥈 Optimized   | O(1)            | O(1)             | Simple math rule, efficient               | Slightly less intuitive at first      |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Clean one-liner, best readability         | Requires insight about trailing zeros |

- Here d = number of digits (at most 10 since num ≤ 10^9).

---

<div align="center">

**🎯 Problem 2119 Completed!**

_Happy Coding! 🚀_

</div>
