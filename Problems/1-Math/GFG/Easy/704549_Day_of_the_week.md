<div align="center">

# 🧠 [Day of the week](https://www.geeksforgeeks.org/problems/day-of-the-week1637/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/day-of-the-week1637/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704549`                                                                                                                                                                                                                                             |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                          |
| **Accuracy**     | `41.67%`                                                                                                                                                                                                                                             |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/day-of-the-week1637/1)                                                                                                                                                                |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                                                    |
| **Company Tags** | ![Morgan Stanley](https://img.shields.io/badge/-Morgan%20Stanley-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![Samsung](https://img.shields.io/badge/-Samsung-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Write a program that calculates the <strong>day of the week</strong> for any given date in the past or future.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> d = 28, m = 12, y = 1995
<strong>Output:</strong> Thursday
<strong>Explanation:</strong> 28 December 1995 was a Thursday.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> d = 30, m = 8, y = 2010
<strong>Output:</strong> Monday
<strong>Explanation:</strong> 30 August 2010 was a Monday.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task:</strong></p>

<p>You don't need to read input or print anything. Complete the function <strong>getDayOfWeek(d, m, y)</strong> which takes three integers <strong>d, m, y</strong> representing day, month, and year, and returns a <strong>string</strong> representing the day of the week.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ d ≤ 31</code></li>
  <li><code>1 ≤ m ≤ 12</code></li>
  <li><code>1 ≤ y ≤ 2100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-day-of-the-week-for-a-given-date/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Count Days from a Reference Date)

#### 📝 Intuition

> - Pick a reference date with known day of the week (e.g., 1 Jan 1971 = Friday).
> - Count the total number of days between the reference date and the given date.
> - Day of the week = (reference_day_index + total_days) % 7.
> - Simple to understand but requires looping over years/months, so slower.

#### 🔍 Algorithm

```pseudo
function bruteForce(d, m, y):
    reference = 1 Jan 1971 (Friday)
    days = 0
    for each year from 1971 to y-1:
        add 365 or 366 if leap year
    for each month from 1 to m-1 in year y:
        add days in that month
    add d-1
    return day_of_week[(days + 5) % 7] // 5 = index of Friday
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    string getDayOfWeek(int d, int m, int y) {
        vector<string> days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
        int monthDays[12] = {31,28,31,30,31,30,31,31,30,31,30,31};

        auto isLeap = [](int y){ return (y%4==0 && (y%100!=0 || y%400==0)); };

        // Count total days from 1 Jan 1971
        int totalDays = 0;

        // Add days for complete years
        for (int year = 1971; year < y; year++)
            totalDays += isLeap(year) ? 366 : 365;

        // Add days for complete months in current year
        for (int i = 0; i < m-1; i++) {
            totalDays += monthDays[i];
            if (i==1 && isLeap(y)) totalDays += 1; // February in leap year
        }

        // Add days in current month
        totalDays += d-1;

        return days[(totalDays + 5) % 7]; // 1 Jan 1971 was Friday (index 5)
    }
};
```

### 🥈 Approach 2: Optimized Solution - Zeller’s Congruence (Mathematical Formula)

#### 📝 Intuition

> Use Zeller’s Congruence, a formula to calculate the day of the week for any date.
>
> Works in $O(1)$ time, no loops required.
>
> For the Gregorian calendar, the formula is:
>
> $$
> h = \left( q + \left\lfloor \frac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \frac{K}{4} \right\rfloor + \left\lfloor \frac{J}{4} \right\rfloor + 5J \right) \bmod 7
> $$
>
> Where:
>
> - $q$ = day
> - $m$ = month (March = 3, …, February = 14; treat Jan & Feb as 13, 14 of previous year)
> - $K$ = year $\bmod 100$
> - $J$ = year $\div 100$
> - $h$ = 0 → Saturday, 1 → Sunday, …, 6 → Friday

#### 🔍 Algorithm

```pseudo
function zeller(d, m, y):
    if m < 3:
        m += 12
        y -= 1
    K = y % 100
    J = y / 100
    h = (d + floor(13*(m+1)/5) + K + floor(K/4) + floor(J/4) + 5*J) % 7
    return day_of_week[h]
```

#### 💻 Implementation

```cpp
// Zeller's Congruence approach

class Solution {
public:
    string getDayOfWeek(int d, int m, int y) {
        vector<string> days = {"Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"};

        if (m < 3) {
            m += 12;
            y -= 1;
        }

        int K = y % 100;
        int J = y / 100;

        int h = (d + 13*(m + 1)/5 + K + K/4 + J/4 + 5*J) % 7;
        return days[h];
    }
};
```

### 🥇 Approach 3: Optimal Solution - Tomohiko Sakamoto’s Algorithm ⭐ (Optimal O(1) without loops)

#### 📝 Intuition

> Precompute an array with offsets for months.
>
> The formula is:
>
> $$
> day\_of\_week = \left( y + \left\lfloor \frac{y}{4} \right\rfloor - \left\lfloor \frac{y}{100} \right\rfloor + \left\lfloor \frac{y}{400} \right\rfloor + t[m-1] + d \right) \bmod 7
> $$
>
> where $t[m-1]$ is the month offset array.
>
> Extremely fast, elegant, $O(1)$ time & $O(1)$ space.

#### 🔍 Algorithm

```pseudo
function sakamoto(d, m, y):
    if m < 3: y -= 1
    t = [0,3,2,5,0,3,5,1,4,6,2,4]
    return day_of_week[(y + y/4 - y/100 + y/400 + t[m-1] + d) % 7]
```

#### 💻 Implementation

**C++:**

```cpp
// Sakamoto's Algorithm: very fast, O(1) time & space

class Solution {
public:
    string getDayOfWeek(int d, int m, int y) {
        vector<string> days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
        int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};

        if (m < 3) y -= 1; // Treat Jan, Feb as months 13,14 of previous year
        int w = (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;

        return days[w];
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                      |
| -------------- | --------------- | ---------------- | ------------------------------------ | ------------------------- |
| 🥉 Brute Force | O(y)            | O(1)             | Intuitive, works with reference date | Slow for distant years    |
| 🥈 Zeller      | O(1)            | O(1)             | Simple formula, exact, no loops      | Slightly tricky formula   |
| 🥇 Sakamoto ⭐ | O(1)            | O(1)             | Elegant, fastest, minimal code       | Must remember month table |

---

<div align="center">

**🎯 Problem 704549 Completed!**

_Happy Coding! 🚀_

</div>
