<div align="center">

# 🧠 [3560. Find Minimum Log Transportation Cost](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203560-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-minimum-log-transportation-cost/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                             |
| **Acceptance Rate** | `41.5%`                                                                                 |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/find-minimum-log-transportation-cost/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                      |

## Description

<!-- description:start -->

<p>You are given integers <code>n</code>, <code>m</code>, and <code>k</code>.</p>

<p>There are two logs of lengths <code>n</code> and <code>m</code> units, which need to be transported in three trucks where each truck can carry one log with length <strong>at most</strong> <code>k</code> units.</p>

<p>You may cut the logs into smaller pieces, where the cost of cutting a log of length <code>x</code> into logs of length <code>len1</code> and <code>len2</code> is <code>cost = len1 * len2</code> such that <code>len1 + len2 = x</code>.</p>

<p>Return the <strong>minimum total cost</strong> to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6, m = 5, k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 = 5. 
Now the three logs of length 1, 5, and 5 can fit in one truck each.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, m = 4, k = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> The two logs can fit in the trucks already, hence we don't need to cut the logs.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>2 &lt;= k &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= n, m &lt;= 2 * k</code></li>
    <li>The input is generated such that it is always possible to transport the logs.</li>
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

### 🥉 Approach 1: Brute Force (Try All Cuts)

#### 📝 Intuition

> - We have 2 logs (length n and m) and 3 trucks, each can carry at most k.
> - Either:
>   - No cuts are needed if both logs ≤ k → cost = 0.
>   - Otherwise, at least one cut is needed.
> - Brute force idea:
>   - Try all possible cut positions for log n and log m.
>   - Check if resulting pieces fit into 3 trucks.
>   - Track minimum cost.
> - Not efficient for large numbers, but helps understand the problem.

#### 🔍 Algorithm

```pseudo
function bruteForce(n, m, k):
    if n <= k and m <= k:
        return 0

    minCost = INF

    for cut in 1..n-1:
        cost = cut * (n-cut)
        pieces = [cut, n-cut, m]
        if max(pieces) <= k:
            minCost = min(minCost, cost)

    for cut in 1..m-1:
        cost = cut * (m-cut)
        pieces = [cut, m-cut, n]
        if max(pieces) <= k:
            minCost = min(minCost, cost)

    return minCost
```

#### 💻 Implementation

```cpp
// Brute force approach (check all possible cuts)

class Solution {
public:
    int minCost(int n, int m, int k) {
        // Case 1: no cuts needed
        if (n <= k && m <= k) return 0;

        int ans = INT_MAX;

        // Try cutting the first log
        for (int cut = 1; cut < n; cut++) {
            int cost = cut * (n - cut);
            vector<int> pieces = {cut, n - cut, m};
            if (*max_element(pieces.begin(), pieces.end()) <= k) {
                ans = min(ans, cost);
            }
        }

        // Try cutting the second log
        for (int cut = 1; cut < m; cut++) {
            int cost = cut * (m - cut);
            vector<int> pieces = {cut, m - cut, n};
            if (*max_element(pieces.begin(), pieces.end()) <= k) {
                ans = min(ans, cost);
            }
        }

        return ans;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Mathematical Insight)

#### 📝 Intuition

> - We don’t need to try all cuts. Observations:
>   - At most one cut is needed since we only need 3 logs total.
>   - Cutting one log of length x → pieces len1, len2.
>   - Valid if max(len1, len2, otherLog) ≤ k.
>   - To minimize len1 \_ len2, the optimal cut is usually as unbalanced as possible (close to 1 and x-1).
> - So instead of brute forcing, we only check:
>   - Cutting log n → best cut is min(1\_(n-1), (n-k)*(2*k-n)) when feasible.
>   - Cutting log m similarly.

#### 🔍 Algorithm

```pseudo
function optimized(n, m, k):
    if n <= k and m <= k: return 0
    ans = INF

    // Try cutting n into two valid parts
    if m <= k:
        for cut in {1, n-1}:
            if max(cut, n-cut) <= k:
                ans = min(ans, cut * (n-cut))

    // Try cutting m into two valid parts
    if n <= k:
        for cut in {1, m-1}:
            if max(cut, m-cut) <= k:
                ans = min(ans, cut * (m-cut))

    return ans
```

#### 💻 Implementation

```cpp
// Optimized approach using greedy cut checks

class Solution {
public:
    int minCost(int n, int m, int k) {
        if (n <= k && m <= k) return 0;

        int ans = INT_MAX;

        // Try cutting log n
        if (m <= k) {
            // Only extreme cuts are candidates: near 1 and n-1
            int cut1 = 1, cut2 = n - 1;
            if (max(cut1, cut2) <= k) ans = min(ans, cut1 * cut2);
        }

        // Try cutting log m
        if (n <= k) {
            int cut1 = 1, cut2 = m - 1;
            if (max(cut1, cut2) <= k) ans = min(ans, cut1 * cut2);
        }

        return ans;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - Even simpler:
>   - If both logs ≤ k → cost = 0.
>   - Otherwise, exactly one log must be cut.
>   - For a log of length x, the only feasible cut is (x-k, k) (so that the bigger piece fits in a truck).
>   - Cost = (x-k) \* k.
> - So final answer =
>   - 0 if no cuts needed
>   - min((n-k)*k if n>k, (m-k)*k if m>k)

#### 🔍 Algorithm

```pseudo
// Write your pseudocode here
```

#### 💻 Implementation

```cpp
// Most optimal approach: direct math formula

class Solution {
public:
    int minCost(int n, int m, int k) {
        // Case 1: no cuts needed
        if (n <= k && m <= k) return 0;

        int ans = INT_MAX;

        // Case 2: need to cut log n
        if (n > k) {
            ans = min(ans, (n - k) * k);
        }

        // Case 3: need to cut log m
        if (m > k) {
            ans = min(ans, (m - k) * k);
        }

        return ans;
    }
};

```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                  | Cons                       |
| -------------- | --------------- | ---------------- | ------------------------------------- | -------------------------- |
| 🥉 Brute Force | O(n+m)          | O(1)             | Very clear, checks all cuts           | Too slow for large `n,m`   |
| 🥈 Optimized   | O(1)            | O(1)             | Uses greedy extreme cuts              | Needs reasoning about cuts |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Direct formula, elegant and efficient | Requires full insight      |

---

<div align="center">

**🎯 Problem 3560 Completed!**

_Happy Coding! 🚀_

</div>
