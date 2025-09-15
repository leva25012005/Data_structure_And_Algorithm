<div align="center">

# 🧠 [2651. Calculate Delayed Arrival Time](https://leetcode.com/problems/calculate-delayed-arrival-time/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202651-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/calculate-delayed-arrival-time/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                             |
| ------------------- | --------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                       |
| **Acceptance Rate** | `76.2%`                                                                           |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/calculate-delayed-arrival-time/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                |

## Description

<!-- description:start -->

<p>You are given a positive integer <code>arrivalTime</code> denoting the arrival time of a train in hours, and another positive integer <code>delayedTime</code> denoting the amount of delay in hours.</p>

<p>Return <em>the time when the train will arrive at the station.</em></p>

<p>Note that the time in this problem is in 24-hours format.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 15, delayedTime = 5 
<strong>Output:</strong> 20 
<strong>Explanation:</strong> Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 13, delayedTime = 11
<strong>Output:</strong> 0
<strong>Explanation:</strong> Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arrivaltime &lt;&nbsp;24</code></li>
	<li><code>1 &lt;= delayedTime &lt;= 24</code></li>
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

### 🥉 Approach 1: Brute Force (Simulation with Loop)

#### 📝 Intuition

> - Start from arrivalTime.
> - Add delay hour by hour.
> - Wrap around to 0 if it reaches 24.
> - Return the final result.
> - This simulates the actual passing of hours.

#### 🔍 Algorithm

```pseudo
function bruteForce(arrivalTime, delayedTime):
    for i in 1..delayedTime:
        arrivalTime += 1
        if arrivalTime == 24:
            arrivalTime = 0
    return arrivalTime
```

#### 💻 Implementation

```cpp
// Brute force simulation approach

class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        // Add delay hour by hour
        for (int i = 0; i < delayedTime; i++) {
            arrivalTime++;
            if (arrivalTime == 24) {
                arrivalTime = 0; // Reset to 0 if it reaches 24
            }
        }
        return arrivalTime;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Direct Addition with If)

#### 📝 Intuition

> - Directly add arrivalTime + delayedTime.
> - If the result is >= 24, subtract 24 once to wrap around.
> - Faster than looping.

#### 🔍 Algorithm

```pseudo
function optimized(arrivalTime, delayedTime):
    total = arrivalTime + delayedTime
    if total >= 24:
        return total - 24
    else:
        return total
```

#### 💻 Implementation

```cpp
// Optimized approach using conditional wrap

class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int total = arrivalTime + delayedTime;
        if (total >= 24) {
            return total - 24; // Wrap around
        }
        return total;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Modulo Arithmetic)

#### 📝 Intuition

> - Use modulo % 24.
> - (arrivalTime + delayedTime) % 24 automatically handles wrapping around.
> - This is the cleanest, most elegant approach.

#### 🔍 Algorithm

```pseudo
function optimal(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24
```

#### 💻 Implementation

```cpp
// Most optimal solution using modulo arithmetic

class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        return (arrivalTime + delayedTime) % 24;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                        | Cons                         |
| -------------- | --------------- | ---------------- | --------------------------- | ---------------------------- |
| 🥉 Brute Force | O(delayedTime)  | O(1)             | Easy to understand          | Slow if delayedTime is large |
| 🥈 Optimized   | O(1)            | O(1)             | Simple conditional handling | Slightly verbose             |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, shortest solution | Requires modulo insight      |

---

<div align="center">

**🎯 Problem 2651 Completed!**

_Happy Coding! 🚀_

</div>
