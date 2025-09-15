<div align="center">

# 🧠 [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201344-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/angle-between-hands-of-a-clock/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                             |
| ------------------- | --------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                     |
| **Acceptance Rate** | `64.3%`                                                                           |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                |

## Description

<!-- description:start -->

<p>Given two numbers, <code>hour</code> and <code>minutes</code>, return <em>the smaller angle (in degrees) formed between the </em><code>hour</code><em> and the </em><code>minute</code><em> hand</em>.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted as correct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1344.Angle%20Between%20Hands%20of%20a%20Clock/images/sample_1_1673.png" style="width: 300px; height: 296px;" />
<pre>
<strong>Input:</strong> hour = 12, minutes = 30
<strong>Output:</strong> 165
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1344.Angle%20Between%20Hands%20of%20a%20Clock/images/sample_2_1673.png" style="width: 300px; height: 301px;" />
<pre>
<strong>Input:</strong> hour = 3, minutes = 30
<strong>Output:</strong> 75
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1300-1399/1344.Angle%20Between%20Hands%20of%20a%20Clock/images/sample_3_1673.png" style="width: 300px; height: 301px;" />
<pre>
<strong>Input:</strong> hour = 3, minutes = 15
<strong>Output:</strong> 7.5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hour &lt;= 12</code></li>
	<li><code>0 &lt;= minutes &lt;= 59</code></li>
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

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

- **Epic Systems** ⭐ 65.3%
- **UKG** ⭐ 63.3%
- **Siemens** ⭐ 60.4%

### 📈 Regular Frequency (40-59%)

_No regular frequency companies_

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Simulate the clock movement.
> - Move both hour and minute hands step by step until they reach the given time.
> - Compute angles and take the difference.
> - This works but is unnecessary heavy since the formula exists

#### 🔍 Algorithm

```pseudo
function bruteForce(hour, minutes):
    hour_angle = (hour % 12) * 30 + (minutes / 60) * 30
    minute_angle = minutes * 6
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Brute force (conceptual simulation but still formula-based)

class Solution {
public:
    double angleClock(int hour, int minutes) {
        // Each hour = 30 degrees, each minute moves the hour hand by 0.5 degrees
        double hour_angle = (hour % 12) * 30 + (minutes * 0.5);
        // Each minute = 6 degrees
        double minute_angle = minutes * 6;

        double diff = fabs(hour_angle - minute_angle);
        return min(diff, 360 - diff); // smaller angle
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - We know:
>   - Hour hand moves 30 _ hour + 0.5 _ minutes degrees.
>   - Minute hand moves 6 \* minutes degrees.
>   - Answer = min(|hour_angle - minute_angle|, 360 - |hour_angle - minute_angle|).
> - This is direct, clean, and efficient.

#### 🔍 Algorithm

```pseudo
function formula(hour, minutes):
    hour_angle = 30*hour + 0.5*minutes
    minute_angle = 6*minutes
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Direct formula approach

class Solution {
public:
    double angleClock(int hour, int minutes) {
        double hour_angle = (hour % 12) * 30 + (minutes * 0.5);
        double minute_angle = minutes * 6;

        double diff = fabs(hour_angle - minute_angle);
        return min(diff, 360 - diff);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical elegance)

#### 📝 Intuition

> We can write the formula in one elegant step:
>
> $$
> \text{Angle} = \min\left( \left| 30 \cdot \text{hour} - 5.5 \cdot \text{minutes} \right|,\; 360 - \left| 30 \cdot \text{hour} - 5.5 \cdot \text{minutes} \right| \right)
> $$
>
> Because:
>
> - Hour hand speed = \(30 \; \text{degrees/hour} + 0.5 \; \text{degrees/minute}\).
> - Minute hand speed = \(6 \; \text{degrees/minute}\).
> - Difference = \(\big|30 \cdot \text{hour} - 5.5 \cdot \text{minutes}\big|\).
>   This is the most concise and optimal solution.

#### 🔍 Algorithm

```pseudo
function optimal(hour, minutes):
    diff = abs(30*hour - 5.5*minutes)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    double angleClock(int hour, int minutes) {
        // Direct one-line mathematical formula
        double diff = fabs(30 * (hour % 12) - 5.5 * minutes);
        return min(diff, 360 - diff);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                          |
| -------------- | --------------- | ---------------- | ------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(1)            | O(1)             | Step-by-step, intuitive         | Verbose, redundant steps      |
| 🥈 Formula     | O(1)            | O(1)             | Clean, easy to understand       | Requires remembering formulas |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Most elegant, single expression | Less intuitive for beginners  |

---

<div align="center">

**🎯 Problem 1344 Completed!**

_Happy Coding! 🚀_

</div>
