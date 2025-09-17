<div align="center">

# 🧠 [1185. Day of the Week](https://leetcode.com/problems/day-of-the-week/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201185-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/day-of-the-week/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| **Difficulty**      | 🟢 **Easy**                                                        |
| **Acceptance Rate** | `58.7%`                                                            |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/day-of-the-week/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a date, return the corresponding day of the week for that date.</p>

<p>The input is given as three integers representing the <code>day</code>, <code>month</code> and <code>year</code> respectively.</p>

<p>Return the answer as one of the following values&nbsp;<code>{&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> day = 31, month = 8, year = 2019
<strong>Output:</strong> &quot;Saturday&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> day = 18, month = 7, year = 1999
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> day = 15, month = 8, year = 1993
<strong>Output:</strong> &quot;Sunday&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The given dates are valid dates between the years <code>1971</code> and <code>2100</code>.</li>
</ul>

<!-- description:end -->

# ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Counting Days from Reference Date)

#### 📝 Intuition

> - Pick a known reference date (e.g., 1971-01-01 is Friday).
> - Count how many days have passed from 1971-01-01 to the given date.
> - Use modulo 7 to map into the day of the week.
> - This is straightforward but requires manual handling of leap years and month lengths.

#### 🔍 Algorithm

```pseudo
function bruteForce(day, month, year):
    ref_date = 1971-01-01, which is Friday
    days = count days from ref_date to given date
    index = (days + 5) % 7   // +5 since 1971-01-01 was Friday
    return weekday[index]
```

#### 💻 Implementation

```cpp
// Brute force by counting days from reference date

class Solution {
public:
    vector<string> week = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};

    // Check leap year
    bool isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }

    int daysInMonth(int m, int y) {
        vector<int> days = {31,28,31,30,31,30,31,31,30,31,30,31};
        if (m == 2 && isLeap(y)) return 29;
        return days[m - 1];
    }

    string dayOfTheWeek(int day, int month, int year) {
        int days = 0;

        // Count full years from 1971 to year-1
        for (int y = 1971; y < year; y++) {
            days += isLeap(y) ? 366 : 365;
        }

        // Count full months in current year
        for (int m = 1; m < month; m++) {
            days += daysInMonth(m, year);
        }

        // Add days of current month
        days += (day - 1);

        // Reference: 1971-01-01 was Friday -> index = 5
        int index = (days + 5) % 7;
        return week[index];
    }
};
```

### 🥈 Approach 2: Optimized Solution - Zeller’s Congruence (Mathematical Formula)

#### 📝 Intuition

> - There exists a direct formula (Zeller’s Congruence) to compute the day of the week.
> - No need to count all days. Just plug into the formula.
> - Formula:
>   h = (day + (13*(month+1))/5 + K + K/4 + J/4 + 5*J) % 7
>   where:
>   - h is day of week (0 = Saturday, 1 = Sunday, 2 = Monday, …).
>   - K = year % 100, J = year / 100.
>   - If month is Jan or Feb, treat it as 13th or 14th month of previous year.

#### 🔍 Algorithm

```pseudo
function zeller(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year / 100
    h = (day + (13*(month+1))/5 + K + (K/4) + (J/4) + (5*J)) % 7
    map h to weekday
```

#### 💻 Implementation

```cpp
// Zeller’s Congruence approach

class Solution {
public:
    vector<string> week = {"Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"};

    string dayOfTheWeek(int day, int month, int year) {
        if (month < 3) {
            month += 12;
            year -= 1;
        }
        int K = year % 100;
        int J = year / 100;

        int h = (day + (13 * (month + 1)) / 5 + K + (K / 4) + (J / 4) + (5 * J)) % 7;

        return week[h];
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Built-in Library)

#### 📝 Intuition

> - Modern C++ has <chrono> library to handle dates.
> - Simply construct the date and query the weekday.
> - This is the cleanest and least error-prone.

#### 🔍 Algorithm

```pseudo
function optimal(day, month, year):
    use chrono::year_month_day to build date
    use weekday to get result
    map weekday to string
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution using chrono library

#include <chrono>
using namespace std::chrono;

class Solution {
public:
    vector<string> week = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};

    string dayOfTheWeek(int day, int month, int year) {
        // Construct date
        year_month_day ymd{year/month/day};

        // Convert to sys_days and get weekday
        weekday wd = sys_days(ymd);

        // weekday: Sunday=0, Monday=1, ...
        return week[wd.c_encoding()];
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity   | Space Complexity | Pros                                       | Cons                        |
| -------------- | ----------------- | ---------------- | ------------------------------------------ | --------------------------- |
| 🥉 Brute Force | O(Y) (years loop) | O(1)             | Easy to understand, works without formulas | Slower (loop through years) |
| 🥈 Zeller’s    | O(1)              | O(1)             | Pure math formula, fast                    | Formula looks complex       |
| 🥇 Optimal ⭐  | O(1)              | O(1)             | Very clean using built-in library          | Requires C++20 `<chrono>`   |

---

<div align="center">

**🎯 Problem 1185 Completed!**

_Happy Coding! 🚀_

</div>
