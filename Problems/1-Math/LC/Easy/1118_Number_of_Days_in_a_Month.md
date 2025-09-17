<div align="center">

# 🧠 [1118. Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201118-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-days-in-a-month/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                        |
| ------------------- | ---------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                  |
| **Acceptance Rate** | `59.2%`                                                                      |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/number-of-days-in-a-month/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)           |

## Description

<!-- description:start -->

<p>Given a year <code>year</code> and a month <code>month</code>, return <em>the number of days of that month</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> year = 1992, month = 7
<strong>Output:</strong> 31
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> year = 2000, month = 2
<strong>Output:</strong> 29
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> year = 1900, month = 2
<strong>Output:</strong> 28
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1583 &lt;= year &lt;= 2100</code></li>
	<li><code>1 &lt;= month &lt;= 12</code></li>
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

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Hardcoded Mapping)

#### 📝 Intuition

> - We know the number of days for most months:
>   - 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
>   - 30 days: Apr, Jun, Sep, Nov
>   - Feb: 28 (29 if leap year).
> - Use a hardcoded array of days per month and adjust February for leap years.

#### 🔍 Algorithm

```pseudo
function bruteForce(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and isLeap(year):
        return 29
    return days[month-1]
```

#### 💻 Implementation

```cpp
// Brute force approach using static array

class Solution {
public:
    // Check leap year
    bool isLeap(int year) {
        // Leap year if divisible by 400 OR divisible by 4 but not by 100
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    int daysInMonth(int year, int month) {
        // Hardcoded days for each month
        vector<int> days = {31,28,31,30,31,30,31,31,30,31,30,31};
        if (month == 2 && isLeap(year)) return 29; // Adjust February
        return days[month - 1];
    }
};
```

### 🥈 Approach 2: Optimized Solution (Switch-Case)

#### 📝 Intuition

> - Instead of storing an array, use switch-case or if-else logic.
> - Check leap year only if month == 2.
> - This avoids storing extra arrays, directly maps month → days.

#### 🔍 Algorithm

```pseudo
function optimized(year, month):
    if month in {1,3,5,7,8,10,12}: return 31
    if month in {4,6,9,11}: return 30
    if month == 2:
        if isLeap(year): return 29
        else return 28
```

#### 💻 Implementation

```cpp
// Optimized approach using switch-case

class Solution {
public:
    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    int daysInMonth(int year, int month) {
        switch (month) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                return 31;
            case 4: case 6: case 9: case 11:
                return 30;
            case 2:
                return isLeap(year) ? 29 : 28;
        }
        return -1; // invalid input
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Formula-based for February)

#### 📝 Intuition

> - All months except February are fixed.
> - For February, directly compute with leap year formula:
>   - Leap year if divisible by 4 and not by 100, or divisible by 400.
> - This is essentially the same as Approach 2 but written more compactly and clearly.

#### 🔍 Algorithm

```pseudo
function optimal(year, month):
    if month == 2:
        return 28 + isLeap(year)
    if month in {4,6,9,11}: return 30
    else: return 31
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    int daysInMonth(int year, int month) {
        if (month == 2) return 28 + isLeap(year); // February case
        if (month == 4 || month == 6 || month == 9 || month == 11) return 30;
        return 31; // All other months
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                  | Cons                     |
| -------------- | --------------- | ---------------- | ------------------------------------- | ------------------------ |
| 🥉 Brute Force | O(1)            | O(12)            | Very clear using lookup table         | Slightly more memory     |
| 🥈 Optimized   | O(1)            | O(1)             | Direct logic, no storage              | Slightly more verbose    |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Clean, elegant, minimal lines of code | Requires leap year check |

---

<div align="center">

**🎯 Problem 1118 Completed!**

_Happy Coding! 🚀_

</div>
