<div align="center">

# 🧠 [2849. Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202849-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                                       |
| **Acceptance Rate** | `37.1%`                                                                                             |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                                  |

## Description

<!-- description:start -->

<p>You are given four integers <code>sx</code>, <code>sy</code>, <code>fx</code>, <code>fy</code>, and a <strong>non-negative</strong> integer <code>t</code>.</p>

<p>In an infinite 2D grid, you start at the cell <code>(sx, sy)</code>. Each second, you <strong>must</strong> move to any of its adjacent cells.</p>

<p>Return <code>true</code> <em>if you can reach cell </em><code>(fx, fy)</code> <em>after<strong> exactly</strong></em> <code>t</code> <strong><em>seconds</em></strong>, <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>A cell&#39;s <strong>adjacent cells</strong> are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2849.Determine%20if%20a%20Cell%20Is%20Reachable%20at%20a%20Given%20Time/images/example2.svg" style="width: 443px; height: 243px;" />
<pre>
<strong>Input:</strong> sx = 2, sy = 4, fx = 7, fy = 7, t = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2849.Determine%20if%20a%20Cell%20Is%20Reachable%20at%20a%20Given%20Time/images/example1.svg" style="width: 383px; height: 202px;" />
<pre>
<strong>Input:</strong> sx = 3, sy = 1, fx = 7, fy = 3, t = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sx, sy, fx, fy &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= t &lt;= 10<sup>9</sup></code></li>
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

## 🔗 Related Problems

| Problem                                                           | Difficulty  | Relationship  |
| ----------------------------------------------------------------- | ----------- | ------------- |
| [Reaching Points](https://leetcode.com/problems/reaching-points/) | 🔴 **Hard** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Not feasible for large constraints)

#### 📝 Intuition

> - Try to simulate moves step by step using BFS (or DFS).
> - At each second, move to all 8 possible neighbors.
> - Check if (fx, fy) is reached exactly at second t.
> - This is correct but impossible for large values (10^9) because the grid is infinite.

#### 🔍 Algorithm

```pseudo
function bruteForce(sx, sy, fx, fy, t):
    queue = [(sx, sy, 0)]   // position + time
    visited = set()
    while queue not empty:
        (x, y, time) = queue.pop()
        if (x, y) == (fx, fy) and time == t:
            return true
        if time < t:
            for each of 8 directions:
                push (x+dx, y+dy, time+1) if not visited
    return false
```

#### 💻 Implementation

```cpp
// Brute force BFS (works only for very small t)

class Solution {
public:
    bool canReachTarget(int sx, int sy, int fx, int fy, int t) {
        // Impossible for large t, only for demonstration
        vector<pair<int,int>> dirs = {
            {1,0},{-1,0},{0,1},{0,-1},
            {1,1},{1,-1},{-1,1},{-1,-1}
        };
        queue<tuple<int,int,int>> q;
        q.push({sx, sy, 0});
        set<pair<int,int>> visited;
        visited.insert({sx, sy});

        while (!q.empty()) {
            auto [x, y, time] = q.front(); q.pop();
            if (x == fx && y == fy && time == t) return true;
            if (time < t) {
                for (auto [dx, dy] : dirs) {
                    int nx = x + dx, ny = y + dy;
                    if (!visited.count({nx, ny})) {
                        visited.insert({nx, ny});
                        q.push({nx, ny, time + 1});
                    }
                }
            }
        }
        return false;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Math-based with BFS Insight)

#### 📝 Intuition

> - From BFS intuition, minimum steps to reach (fx, fy) is
>
> $$
> \text{minSteps} = \max\left( \lvert f_x - s_x \rvert,\; \lvert f_y - s_y \rvert \right)
> $$
>
> - minSteps=max(∣fx−sx∣,∣fy−sy∣)
> - If t == minSteps → exactly possible.
> - If t > minSteps → we can “waste” moves by going back and forth (extra steps are always possible).
> - So condition: t >= minSteps.

#### 🔍 Algorithm

```pseudo
function optimized(sx, sy, fx, fy, t):
    dx = abs(fx - sx)
    dy = abs(fy - sy)
    minSteps = max(dx, dy)
    return t >= minSteps
```

#### 💻 Implementation

```cpp
// Optimized math-based solution

class Solution {
public:
    bool canReachTarget(int sx, int sy, int fx, int fy, int t) {
        long long dx = abs(fx - sx);
        long long dy = abs(fy - sy);
        long long minSteps = max(dx, dy);
        return t >= minSteps;  // True if we have enough time
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> Same as approach 2, but written in the most elegant form.
> The check reduces to just one line:
>
> $$
> \text{return } \; t \geq \max \left( \lvert f_x - s_x \rvert,\; \lvert f_y - s_y \rvert \right)
> $$

#### 🔍 Algorithm

```pseudo
function optimal(sx, sy, fx, fy, t):
    return t >= max(abs(fx - sx), abs(fy - sy))
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    bool canReachTarget(int sx, int sy, int fx, int fy, int t) {
        return t >= max(abs(fx - sx), abs(fy - sy));
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                          | Cons                             |
| -------------- | --------------- | ---------------- | ----------------------------- | -------------------------------- |
| 🥉 Brute Force | O(8^t)          | O(t)             | Intuitive, follows definition | Impossible for large inputs      |
| 🥈 Optimized   | O(1)            | O(1)             | Uses math, efficient          | Slightly less intuitive at first |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Clean, elegant, one-liner     | None                             |

---

<div align="center">

**🎯 Problem 2849 Completed!**

_Happy Coding! 🚀_

</div>
$$
