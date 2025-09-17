<div align="center">

# 🧠 [1056. Confusing Number](https://leetcode.com/problems/confusing-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201056-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/confusing-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                               |
| ------------------- | ------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                         |
| **Acceptance Rate** | `49.3%`                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/confusing-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)  |

## Description

<!-- description:start -->

<p>A <strong>confusing number</strong> is a number that when rotated <code>180</code> degrees becomes a different number with <strong>each digit valid</strong>.</p>

<p>We can rotate digits of a number by <code>180</code> degrees to form new digits.</p>

<ul>
	<li>When <code>0</code>, <code>1</code>, <code>6</code>, <code>8</code>, and <code>9</code> are rotated <code>180</code> degrees, they become <code>0</code>, <code>1</code>, <code>9</code>, <code>8</code>, and <code>6</code> respectively.</li>
	<li>When <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, and <code>7</code> are rotated <code>180</code> degrees, they become <strong>invalid</strong>.</li>
</ul>

<p>Note that after rotating a number, we can ignore leading zeros.</p>

<ul>
	<li>For example, after rotating <code>8000</code>, we have <code>0008</code> which is considered as just <code>8</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <code>true</code><em> if it is a <strong>confusing number</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_1.png" style="width: 281px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_2.png" style="width: 312px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 89
<strong>Output:</strong> true
<strong>Explanation:</strong> We get 68 after rotating 89, 68 is a valid number and 68 != 89.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1000-1099/1056.Confusing%20Number/images/1268_3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> false
<strong>Explanation:</strong> We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number
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

| Problem                                                                         | Difficulty  | Relationship    |
| ------------------------------------------------------------------------------- | ----------- | --------------- |
| [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) | 🟢 **Easy** | Similar logic   |
| [Confusing Number II](https://leetcode.com/problems/confusing-number-ii/)       | 🔴 **Hard** | Related concept |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (String + Reverse)

#### 📝 Intuition

> - Convert number to string.
> - Rotate each digit according to the mapping:
> - 0 -> 0, 1 -> 1, 6 -> 9, 8 -> 8, 9 -> 6
> - If any digit is invalid (2,3,4,5,7), return false.
> - After rotating all digits, reverse the rotated string (since rotation changes order).
> - Compare with original: return true if rotated ≠ original.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    s = string of n
    rotated = ""
    for each digit in s (from left to right):
        if digit invalid -> return false
        rotated += mapping[digit]
    rotated = reverse(rotated)
    return rotated != s
```

#### 💻 Implementation

```cpp
// Brute force approach using string manipulation

class Solution {
public:
    bool confusingNumber(int n) {
        string s = to_string(n);
        unordered_map<char, char> mp = {
            {'0','0'}, {'1','1'}, {'6','9'},
            {'8','8'}, {'9','6'}
        };

        string rotated = "";
        for (char c : s) {
            if (mp.find(c) == mp.end()) return false; // Invalid digit
            rotated += mp[c]; // Build rotated version
        }

        reverse(rotated.begin(), rotated.end()); // Reverse to simulate rotation

        return rotated != s; // Must be different to be confusing
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math-based Reverse)

#### 📝 Intuition

> - Instead of using strings, rotate digits using math.
> - Extract digits from right to left (n % 10).
> - Map them to rotated digits.
> - Construct rotated number while going through digits.
> - Compare rotated number with original.
> - This avoids string overhead.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    original = n
    rotated = 0
    while n > 0:
        digit = n % 10
        if digit not in valid_map: return false
        rotated = rotated * 10 + valid_map[digit]
        n //= 10
    return rotated != original
```

#### 💻 Implementation

```cpp
// Optimized approach using math

class Solution {
public:
    bool confusingNumber(int n) {
        int original = n;
        int rotated = 0;

        unordered_map<int, int> mp = {
            {0,0}, {1,1}, {6,9}, {8,8}, {9,6}
        };

        while (n > 0) {
            int digit = n % 10;
            if (mp.find(digit) == mp.end()) return false; // Invalid digit
            rotated = rotated * 10 + mp[digit]; // Build rotated number
            n /= 10;
        }

        return rotated != original;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct inline map)

#### 📝 Intuition

> - Same as Approach 2 but more compact.
> - Use a fixed array instead of hash map for faster lookup (O(1) with index).
> - Predefine: map[10] = {0,1,-1,-1,-1,-1,9,-1,8,6} (-1 = invalid).
> - Build rotated number directly.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    original = n
    rotated = 0
    while n > 0:
        digit = n % 10
        if map[digit] == -1: return false
        rotated = rotated * 10 + map[digit]
        n //= 10
    return rotated != original
```

#### 💻 Implementation

```cpp
// Most optimal approach using array mapping

class Solution {
public:
    bool confusingNumber(int n) {
        int original = n, rotated = 0;
        // Direct map: -1 means invalid digit
        int rotateMap[10] = {0,1,-1,-1,-1,-1,9,-1,8,6};

        while (n > 0) {
            int digit = n % 10;
            if (rotateMap[digit] == -1) return false; // Invalid
            rotated = rotated * 10 + rotateMap[digit];
            n /= 10;
        }
        return rotated != original;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                     | Cons                        |
| -------------- | --------------- | ---------------- | ---------------------------------------- | --------------------------- |
| 🥉 Brute Force | O(d)            | O(d)             | Very simple, string-based, easy to debug | Uses extra string & reverse |
| 🥈 Optimized   | O(d)            | O(1)             | Math-only, no string overhead            | Slightly more code          |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Fastest, clean lookup with array mapping | Requires predefining array  |

- Here d = number of digits in n (≤ 10 since n ≤ 1e9).

---

<div align="center">

**🎯 Problem 1056 Completed!**

_Happy Coding! 🚀_

</div>
