<div align="center">

# 🧠 [492. Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%20492-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/construct-the-rectangle/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `61.3%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/construct-the-rectangle/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## Description

<!-- description:start -->

<p>A web developer needs to know how to design a web page&#39;s size. So, given a specific rectangular web page&rsquo;s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:</p>

<ol>
	<li>The area of the rectangular web page you designed must equal to the given target area.</li>
	<li>The width <code>W</code> should not be larger than the length <code>L</code>, which means <code>L &gt;= W</code>.</li>
	<li>The difference between length <code>L</code> and width <code>W</code> should be as small as possible.</li>
</ol>

<p>Return <em>an array <code>[L, W]</code> where <code>L</code> and <code>W</code> are the length and width of the&nbsp;web page you designed in sequence.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> area = 4
<strong>Output:</strong> [2,2]
<strong>Explanation:</strong> The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> area = 37
<strong>Output:</strong> [37,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> area = 122122
<strong>Output:</strong> [427,286]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= area &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `16-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `16-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Try all possible pairs (L, W) such that L \* W == area.
> - Keep only the ones where L >= W.
> - Among them, choose the pair with the smallest difference L - W.
> - This works but is inefficient because we might check up to area candidates.

#### 🔍 Algorithm

```pseudo
function bruteForce(area):
    bestL = area
    bestW = 1
    for w in 1..area:
        if area % w == 0:
            l = area / w
            if l >= w and (l - w) < (bestL - bestW):
                bestL = l
                bestW = w
    return [bestL, bestW]
```

#### 💻 Implementation

```cpp
// Brute Force Approach

class Solution {
public:
    vector<int> constructRectangleBrute(int area) {
        int bestL = area;  // start with max possible L
        int bestW = 1;     // start with min possible W

        // Try all possible widths
        for (int w = 1; w <= area; w++) {
            if (area % w == 0) {        // must divide evenly
                int l = area / w;       // compute length
                if (l >= w) {           // must satisfy L >= W
                    // Check if difference is smaller
                    if ((l - w) < (bestL - bestW)) {
                        bestL = l;
                        bestW = w;
                    }
                }
            }
        }
        return {bestL, bestW};
    }
};
```

### 🥇 Approach 2: Optimal Solution ⭐

#### 📝 Intuition

> - To minimize L - W, we want W to be as close as possible to sqrt(area).
> - So instead of checking from 1 upwards, we can start directly from floor(sqrt(area)) and go downwards until we find a divisor.
> - The first divisor found guarantees minimal difference.
> - This is the most efficient approach.

#### 🔍 Algorithm

```pseudo
function optimal(area):
    w = floor(sqrt(area))
    while area % w != 0:
        w -= 1
    l = area / w
    return [l, w]
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    vector<int> constructRectangleOptimal(int area) {
        int w = (int)sqrt(area);  // start from sqrt(area)

        // Move down until we find a divisor
        while (area % w != 0) {
            w--;
        }

        int l = area / w;  // compute corresponding length
        return {l, w};     // L >= W is guaranteed
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity       | Space Complexity | Pros                            | Cons                           |
| -------------- | --------------------- | ---------------- | ------------------------------- | ------------------------------ |
| 🥉 Brute Force | O(area)               | O(1)             | Very simple, follows definition | Too slow for large area (10^7) |
| 🥇 Optimal ⭐  | O(√area) (early stop) | O(1)             | Fastest, elegant, minimal loops | Requires math insight          |

---

<div align="center">

**🎯 Problem 492 Completed!**

_Happy Coding! 🚀_

</div>
````
