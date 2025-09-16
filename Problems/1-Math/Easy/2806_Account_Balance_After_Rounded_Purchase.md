<div align="center">

# 🧠 [2806. Account Balance After Rounded Purchase](https://leetcode.com/problems/account-balance-after-rounded-purchase/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202806-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/account-balance-after-rounded-purchase/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                               |
| **Acceptance Rate** | `55.3%`                                                                                   |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/account-balance-after-rounded-purchase/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                        |

## Description

<!-- description:start -->

<p>Initially, you have a bank account balance of <strong>100</strong> dollars.</p>

<p>You are given an integer <code>purchaseAmount</code> representing the amount you will spend on a purchase in dollars, in other words, its price.</p>

<p>When making the purchase, first the <code>purchaseAmount</code> <strong>is rounded to the nearest multiple of 10</strong>. Let us call this value <code>roundedAmount</code>. Then, <code>roundedAmount</code> dollars are removed from your bank account.</p>

<p>Return an integer denoting your final bank account balance after this purchase.</p>

<p><strong>Notes:</strong></p>

<ul>
    <li>0 is considered to be a multiple of 10 in this problem.</li>
    <li>When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 9
<strong>Output:</strong> 90
<strong>Explanation:</strong> The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 15
<strong>Output:</strong> 80
<strong>Explanation:</strong> The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> purchaseAmount = 10
<strong>Output:</strong> 90
<strong>Explanation:</strong> 10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>0 &lt;= purchaseAmount &lt;= 100</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `DD-MM-YYYY` | First attempt, understanding the problem |
| ✅ **Solved**    | `DD-MM-YYYY` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation by checking multiples)

#### 📝 Intuition

> - Start from the given purchaseAmount.
> - Find the closest multiple of 10 by checking all multiples of 10 (0, 10, 20, …).
> - Choose the nearest one (rounding rule: if difference = 5, round upward).
> - Subtract this rounded amount from 100.
> - This works but is overkill since purchaseAmount ≤ 100.

#### 🔍 Algorithm

```pseudo
function bruteForce(purchaseAmount):
    roundedAmount = 0
    for m in [0, 10, 20, ..., 100]:
        if abs(m - purchaseAmount) is smallest:
            choose m (if tie, pick larger m)
    return 100 - roundedAmount
```

#### 💻 Implementation

```cpp
// Brute force approach by checking multiples of 10

class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        int roundedAmount = 0;
        int bestDiff = INT_MAX;

        // Try all multiples of 10 from 0 to 100
        for (int m = 0; m <= 100; m += 10) {
            int diff = abs(m - purchaseAmount);
            // If closer OR same distance but larger (round up on tie)
            if (diff < bestDiff || (diff == bestDiff && m > roundedAmount)) {
                roundedAmount = m;
                bestDiff = diff;
            }
        }
        return 100 - roundedAmount;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Every number purchaseAmount can be split into:
>   - tens = purchaseAmount / 10
>   - remainder = purchaseAmount % 10
>   - If remainder < 5, round down → roundedAmount = tens \_ 10.
> - Else, round up → roundedAmount = (tens + 1) \_ 10.
> - Subtract from 100.
> - This avoids looping through multiples of 10.

#### 🔍 Algorithm

```pseudo
function optimized(purchaseAmount):
    tens = purchaseAmount // 10
    remainder = purchaseAmount % 10
    if remainder < 5:
        roundedAmount = tens * 10
    else:
        roundedAmount = (tens + 1) * 10
    return 100 - roundedAmount
```

#### 💻 Implementation

```cpp
// Optimized approach using division and modulus

class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        int tens = purchaseAmount / 10;
        int remainder = purchaseAmount % 10;

        int roundedAmount;
        if (remainder < 5)
            roundedAmount = tens * 10;      // Round down
        else
            roundedAmount = (tens + 1) * 10; // Round up

        return 100 - roundedAmount;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Rounding to the nearest multiple of 10 can be done by:
>   - roundedAmount = ((purchaseAmount + 5) / 10) \* 10
> - Explanation: Adding 5 before integer division ensures correct rounding (ties go up).
> - Subtract directly from 100.
> - This is the cleanest and most elegant.

#### 🔍 Algorithm

```pseudo
function optimal(purchaseAmount):
    roundedAmount = ((purchaseAmount + 5) // 10) * 10
    return 100 - roundedAmount
```

#### 💻 Implementation

```cpp
// Most optimal solution with math trick

class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        int roundedAmount = ((purchaseAmount + 5) / 10) * 10; // Round to nearest multiple of 10
        return 100 - roundedAmount;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                  | Cons                             |
| -------------- | --------------- | ---------------- | ------------------------------------- | -------------------------------- |
| 🥉 Brute Force | O(11) ≈ O(1)    | O(1)             | Very explicit, simulates rounding     | Inefficient, too many checks     |
| 🥈 Optimized   | O(1)            | O(1)             | Simple math with division + remainder | Slightly more verbose            |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | One-liner, elegant, cleanest solution | Needs to know the rounding trick |

---

<div align="center">

**🎯 Problem 2806 Completed!**

_Happy Coding! 🚀_

</div>
