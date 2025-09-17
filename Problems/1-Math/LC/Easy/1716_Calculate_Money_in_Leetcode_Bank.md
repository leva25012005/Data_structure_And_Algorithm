<div align="center">

# 🧠 [1716. Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201716-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                         |
| **Acceptance Rate** | `78.6%`                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                  |

## Description

<!-- description:start -->

<p>Hercy wants to save money for his first car. He puts money in the Leetcode&nbsp;bank <strong>every day</strong>.</p>

<p>He starts by putting in <code>$1</code> on Monday, the first day. Every day from Tuesday to Sunday, he will put in <code>$1</code> more than the day before. On every subsequent Monday, he will put in <code>$1</code> more than the <strong>previous Monday</strong>.<span style="display: none;"> </span></p>

<p>Given <code>n</code>, return <em>the total amount of money he will have in the Leetcode bank at the end of the </em><code>n<sup>th</sup></code><em> day.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 10
<strong>Explanation:</strong>&nbsp;After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 37
<strong>Explanation:</strong>&nbsp;After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 96
<strong>Explanation:</strong>&nbsp;After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
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

| Problem                                                                                                     | Difficulty  | Relationship  |
| ----------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| [Distribute Money to Maximum Children](https://leetcode.com/problems/distribute-money-to-maximum-children/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Simulate each day one by one.
> - Keep track of the current week’s starting amount (Monday’s deposit).
> - Increment daily by $1 from the previous day.
> - On each Monday, increment the starting amount by $1.
> - Simple but uses a loop for every single day.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    total = 0
    week_start = 1
    day_in_week = 0
    for i in 1..n:
        total += week_start + day_in_week
        day_in_week += 1
        if day_in_week == 7:
            week_start += 1
            day_in_week = 0
    return total
```

#### 💻 Implementation

```cpp
// Brute force simulation

class Solution {
public:
    int totalMoney(int n) {
        int total = 0;
        int week_start = 1; // Monday deposit
        int day_in_week = 0;

        for (int i = 0; i < n; i++) {
            total += week_start + day_in_week; // Add today's money
            day_in_week++;

            if (day_in_week == 7) { // End of week, next Monday
                week_start++;
                day_in_week = 0;
            }
        }
        return total;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Week and Remainder)

#### 📝 Intuition

> - Count full weeks and remaining days.
> - Each week is an arithmetic progression starting from the current Monday.
> - Sum of a week: 7 * week_start + sum(0..6) = 7*week_start + 21.
> - For remaining days: sum from week_start incremented daily.
> - Fewer iterations than simulating every single day

#### 🔍 Algorithm

```pseudo
function optimized(n):
    full_weeks = n / 7
    remaining_days = n % 7
    total = 0

    for week in 0..full_weeks-1:
        total += 7 * (1 + week) + 21

    for day in 0..remaining_days-1:
        total += (1 + full_weeks) + day

    return total
```

#### 💻 Implementation

```cpp
// Optimized by weeks and remaining days

class Solution {
public:
    int totalMoney(int n) {
        int total = 0;
        int full_weeks = n / 7;
        int remaining_days = n % 7;

        // Sum for full weeks
        for (int week = 0; week < full_weeks; week++) {
            total += 7 * (1 + week) + 21; // 21 = sum(0..6)
        }

        // Sum for remaining days
        for (int day = 0; day < remaining_days; day++) {
            total += (1 + full_weeks) + day;
        }

        return total;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Arithmetic Formula)

#### 📝 Intuition

> - Each week sum: sum\*week = 7\*week_start + 21.
> - Full weeks total: arithmetic series: sum_total_weeks = sum_week1 + sum_week2 + ....
> - Remaining days: arithmetic sum formula: sum_rem = remaining_days * first*day + remaining_days\*(remaining_days-1)/2.
> - Combine both sums for a formula-based solution without loops (or minimal loops).

#### 🔍 Algorithm

```pseudo
function optimal(n):
    full_weeks = n / 7
    remaining_days = n % 7
    sum_full_weeks = full_weeks * (7 + 7*full_weeks)/2 + 21 * full_weeks
    sum_remaining = remaining_days * (1 + full_weeks) + remaining_days*(remaining_days-1)/2
    return sum_full_weeks + sum_remaining
```

#### 💻 Implementation

```cpp
// Optimal arithmetic solution

class Solution {
public:
    int totalMoney(int n) {
        int full_weeks = n / 7;
        int remaining_days = n % 7;

        // Sum of full weeks: arithmetic series formula
        int sum_full_weeks = full_weeks * 28 + (full_weeks * (full_weeks - 1) / 2) * 7;

        // Sum of remaining days
        int sum_remaining = remaining_days * (full_weeks + 1) + (remaining_days * (remaining_days - 1)) / 2;

        return sum_full_weeks + sum_remaining;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity               | Space Complexity | Pros                              | Cons                       |
| -------------- | ----------------------------- | ---------------- | --------------------------------- | -------------------------- |
| 🥉 Brute Force | O(n)                          | O(1)             | Very intuitive                    | Iterates over every day    |
| 🥈 Optimized   | O(weeks + remainder) ≈ O(n/7) | O(1)             | Less iteration, easy to implement | Still uses small loops     |
| 🥇 Optimal ⭐  | O(1)                          | O(1)             | Formula-based, minimal operations | Slightly tricky arithmetic |

---

<div align="center">

**🎯 Problem 1716 Completed!**

_Happy Coding! 🚀_

</div>
