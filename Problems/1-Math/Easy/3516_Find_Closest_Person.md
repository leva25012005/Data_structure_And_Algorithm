<div align="center">

# 🧠 [3516. Find Closest Person](https://leetcode.com/problems/find-closest-person/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203516-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-closest-person/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                            |
| **Acceptance Rate** | `83.3%`                                                                |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-closest-person/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)     |

## Description

<!-- description:start -->

<p>You are given three integers <code>x</code>, <code>y</code>, and <code>z</code>, representing the positions of three people on a number line:</p>

<ul>
    <li><code>x</code> is the position of Person 1.</li>
    <li><code>y</code> is the position of Person 2.</li>
    <li><code>z</code> is the position of Person 3, who does <strong>not</strong> move.</li>
</ul>

<p>Both Person 1 and Person 2 move toward Person 3 at the <strong>same</strong> speed.</p>

<p>Determine which person reaches Person 3 <strong>first</strong>:</p>

<ul>
    <li>Return 1 if Person 1 arrives first.</li>
    <li>Return 2 if Person 2 arrives first.</li>
    <li>Return 0 if both arrive at the <strong>same</strong> time.</li>
</ul>

<p>Return the result accordingly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 7, z = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
- Person 2 is at position 7 and can reach Person 3 in 3 steps.
Since Person 1 reaches Person 3 first, the output is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 5, z = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
- Person 2 is at position 5 and can reach Person 3 in 1 step.
Since Person 2 reaches Person 3 first, the output is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 1, y = 5, z = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
- Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
- Person 2 is at position 5 and can reach Person 3 in 2 steps.
Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= x, y, z &lt;= 100</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `17-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `17-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Simulate the movement step by step.
> - At each step, move Person 1 and Person 2 one unit closer to Person 3.
> - Stop when one (or both) reach Person 3.
> - This works since max distance ≤ 100 (small).

#### 🔍 Algorithm

```pseudo
function bruteForce(x, y, z):
    while true:
        if x == z and y == z: return 0
        if x == z: return 1
        if y == z: return 2
        move x one step toward z
        move y one step toward z
```

#### 💻 Implementation

```cpp
// Brute force simulation approach

class Solution {
public:
    int raceResultBruteForce(int x, int y, int z) {
        while (true) {
            // If both arrive at the same time
            if (x == z && y == z) return 0;
            // If Person 1 arrives first
            if (x == z) return 1;
            // If Person 2 arrives first
            if (y == z) return 2;

            // Move one step toward z
            x += (x < z ? 1 : -1);
            y += (y < z ? 1 : -1);
        }
    }
};
```

### 🥈 Approach 2: Optimized Solution (Distance Calculation)

#### 📝 Intuition

> - Instead of simulating, compute the distance:
>   - dist1 = abs(x - z)
>   - dist2 = abs(y - z)
> - Compare the two distances:
>   - If dist1 < dist2 → Person 1 arrives first.
>   - If dist2 < dist1 → Person 2 arrives first.
>   - If equal → Both arrive at the same time.

#### 🔍 Algorithm

```pseudo
function optimized(x, y, z):
    dist1 = abs(x - z)
    dist2 = abs(y - z)
    if dist1 < dist2: return 1
    if dist2 < dist1: return 2
    return 0
```

#### 💻 Implementation

```cpp
// Optimized approach using direct distance comparison

class Solution {
public:
    int raceResultOptimized(int x, int y, int z) {
        int dist1 = abs(x - z);
        int dist2 = abs(y - z);

        if (dist1 < dist2) return 1;
        else if (dist2 < dist1) return 2;
        else return 0;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Constant-time, clean)

#### 📝 Intuition

> - The optimized solution is already O(1).
> - The most elegant form is to directly use a ternary operator for comparison.
> - No loops, minimal code, fully constant-time.

#### 🔍 Algorithm

```pseudo
function optimal(x, y, z):
    return 1 if abs(x - z) < abs(y - z)
    return 2 if abs(y - z) < abs(x - z)
    return 0
```

#### 💻 Implementation

```cpp
/// Most optimal and elegant solution (constant-time)

class Solution {
public:
    int raceResultOptimal(int x, int y, int z) {
        int dist1 = abs(x - z), dist2 = abs(y - z);
        return (dist1 < dist2) ? 1 : (dist2 < dist1) ? 2 : 0;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                            | Cons                  |     |     |     |     |
| -------------- | --------------- | ---------------- | ------------------------------- | --------------------- | --- | --- | --- | --- |
| 🥉 Brute Force | O(d)            | O(1)             | None                            | y-z                   |
| 🥈 Optimized   | O(1)            | O(1)             | Simple math-based solution      | Slightly more verbose |     |     |     |     |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, minimal code, elegant | None                  |     |     |     |     |

---

<div align="center">

**🎯 Problem 3516 Completed!**

_Happy Coding! 🚀_

</div>
