<div align="center">

# 🧠 [Angle between hour and minute hand](https://www.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand0545/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand0545/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703981`                                                                                                                                                                                                                                                                                                      |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                 |
| **Accuracy**     | `15.91%`                                                                                                                                                                                                                                                                                                      |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand0545/1)                                                                                                                                                                                                      |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square)                                                                                                                                             |
| **Company Tags** | ![Paytm](https://img.shields.io/badge/-Paytm-orange?style=flat-square) ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Salesforce](https://img.shields.io/badge/-Salesforce-orange?style=flat-square) ![Infinera](https://img.shields.io/badge/-Infinera-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a string <strong>s</strong> representing time in 24-hour format <strong>"HH:MM"</strong>, compute the <strong>smallest angle</strong> (in degrees) between the hour and minute hands of an analog clock.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "06:00"
<strong>Output:</strong> 180.000
<strong>Explanation:</strong> At 06:00, the angle between the hour and minute hands is 180.000 degrees.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "03:15"
<strong>Output:</strong> 7.500
<strong>Explanation:</strong> At 03:15, 
- The hour hand is at 3 + 15/60 = 3.25 hours → 3.25 × 30 = 97.5 degrees.
- The minute hand is at 15 × 6 = 90 degrees.
- The difference is |97.5 - 90| = 7.5 degrees.
</pre>

## Constraints

<ul>
  <li><code>s.size() = 5</code></li>
  <li><code>00 ≤ HH ≤ 23</code></li>
  <li><code>00 ≤ MM ≤ 59</code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(1)</li>
  <li><strong>Auxiliary Space:</strong> O(1)</li>
</ul>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Convert the given time "HH:MM" into hours and minutes.
> - Simulate movement:
>   - The hour hand moves 30° per hour + 0.5° per minute.
>   - The minute hand moves 6° per minute.
> - Compute the absolute difference between the two hands.
> - Since the clock is circular, the answer is min(diff, 360 - diff).
> - This is the most direct solution.

#### 🔍 Algorithm

```pseudo
function bruteForce(s):
    hours = first two chars of s
    minutes = last two chars of s
    hour_angle = (hours % 12) * 30 + (minutes * 0.5)
    minute_angle = minutes * 6
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Brute force simulation approach

class Solution {
public:
    double angleClock(string s) {
        int hours = stoi(s.substr(0, 2)); // HH
        int minutes = stoi(s.substr(3, 2)); // MM

        // Hour hand = (hours % 12)*30 + minutes*0.5
        double hour_angle = (hours % 12) * 30 + minutes * 0.5;
        // Minute hand = minutes * 6
        double minute_angle = minutes * 6;

        // Absolute difference
        double diff = fabs(hour_angle - minute_angle);

        // Return the smaller angle
        return min(diff, 360.0 - diff);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Formula)

#### 📝 Intuition

> - Instead of thinking separately, derive a direct formula:
> - diff = |(30*H + 0.5*M) - (6*M)| = |30*H - 5.5\*M|
> - Normalize H % 12 since 24-hour input is given.
> - Final answer = min(diff, 360 - diff).
> - This avoids storing intermediate angles explicitly.

#### 🔍 Algorithm

```pseudo
function optimized(s):
    H, M = parse(s)
    H = H % 12
    diff = abs(30*H - 5.5*M)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Optimized direct formula approach

class Solution {
public:
    double angleClock(string s) {
        int hours = stoi(s.substr(0, 2));
        int minutes = stoi(s.substr(3, 2));

        // Normalize hour into 12-hour format
        hours %= 12;

        // Apply direct formula
        double diff = fabs(30 * hours - 5.5 * minutes);

        return min(diff, 360.0 - diff);
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Compact One-Pass)

#### 📝 Intuition

> - Parse hours and minutes once.
> - Immediately compute the angle in one compact expression:
> - result = min(|30*(H%12) - 5.5*M|, 360 - |30*(H%12) - 5.5*M|)
> - No extra variables needed, O(1) space.
> - This is the cleanest and most elegant form.

#### 🔍 Algorithm

```pseudo
function optimal(s):
    H, M = parse(s)
    H = H % 12
    diff = abs(30*H - 5.5*M)
    return min(diff, 360 - diff)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    double angleClock(string s) {
        int H = stoi(s.substr(0, 2));
        int M = stoi(s.substr(3, 2));

        double diff = fabs(30 * (H % 12) - 5.5 * M);

        return min(diff, 360.0 - diff);
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                             | Cons                    |
| -------------- | --------------- | ---------------- | -------------------------------- | ----------------------- |
| 🥉 Brute Force | O(1)            | O(1)             | Very intuitive, step by step     | More intermediate vars  |
| 🥈 Optimized   | O(1)            | O(1)             | Direct formula, less computation | Slightly less readable  |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Most elegant, compact one-liner  | Harder to read at first |

---

<div align="center">

**🎯 Problem 703981 Completed!**

_Happy Coding! 🚀_

</div>
