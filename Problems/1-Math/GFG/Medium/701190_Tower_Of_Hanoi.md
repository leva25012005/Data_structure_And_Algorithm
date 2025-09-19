<div align="center">

# 🧠 [Tower Of Hanoi](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `701190`                                                                                                                                                    |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                               |
| **Accuracy**     | `35.23%`                                                                                                                                                    |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)                                                                 |
| **Topic Tags**   | ![Recursion](https://img.shields.io/badge/-Recursion-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Flipkart](https://img.shields.io/badge/-Flipkart-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>You are given <strong>n</strong> disks placed on a starting rod (<code>from</code>), with the smallest disk on top and the largest at the bottom. There are three rods: the <strong>starting rod</strong> (<code>from</code>), the <strong>target rod</strong> (<code>to</code>), and an <strong>auxiliary rod</strong> (<code>aux</code>).</p>

<p>You need to calculate the total number of <strong>moves</strong> required to transfer all <strong>n</strong> disks from the starting rod to the target rod, following these rules:</p>
<ul>
  <li>Only one disk can be moved at a time.</li>
  <li>A disk can only be placed on top of a larger disk or on an empty rod.</li>
</ul>

<p>Return the number of moves needed to complete the task.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
Steps:
1. Move disk 1 from rod 1 to rod 2
2. Move disk 2 from rod 1 to rod 3
3. Move disk 1 from rod 2 to rod 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
Steps:
1. Move disk 1 from rod 1 to rod 3
2. Move disk 2 from rod 1 to rod 2
3. Move disk 1 from rod 3 to rod 2
4. Move disk 3 from rod 1 to rod 3
5. Move disk 1 from rod 2 to rod 1
6. Move disk 2 from rod 2 to rod 3
7. Move disk 1 from rod 1 to rod 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> No disks to move, so 0 steps required.
</pre>

## Constraints

<ul>
  <li>0 ≤ n ≤ 20</li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursion)

#### 📝 Intuition

> - Tower of Hanoi is usually solved recursively.
> - To move n disks from from → to using aux:
>   - Move n-1 disks from from → aux.
>   - Move the largest disk from from → to.
>   - Move the n-1 disks from aux → to.
> - The total moves follow:
> - T(n) = 2\*T(n-1) + 1

#### 🔍 Algorithm

```pseudo
function hanoi(n, from, to, aux):
    if n == 0: return 0
    moves1 = hanoi(n-1, from, aux, to)
    moves2 = 1
    moves3 = hanoi(n-1, aux, to, from)
    return moves1 + moves2 + moves3
```

#### 💻 Implementation

```cpp
// Recursive simulation of Tower of Hanoi

class Solution {
public:
    long long hanoiMoves(int n, int from=1, int to=3, int aux=2) {
        if (n == 0) return 0; // Base case
        long long moves = 0;
        moves += hanoiMoves(n - 1, from, aux, to); // Move top n-1 disks to aux
        moves += 1;                               // Move largest disk
        moves += hanoiMoves(n - 1, aux, to, from); // Move n-1 disks from aux to target
        return moves;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Recurrence Formula)

#### 📝 Intuition

> - From recursion we see:
> - T(n) = 2\*T(n-1) + 1
> - Solving gives closed form:
> - T(n) = 2^n - 1
> - Instead of recursion, just compute 2^n - 1.

#### 🔍 Algorithm

```pseudo
function recurrence(n):
    if n == 0: return 0
    return 2^n - 1
```

#### 💻 Implementation

```cpp
// Recurrence formula: 2^n - 1

class Solution {
public:
    long long hanoiMoves(int n) {
        if (n == 0) return 0;
        return (1LL << n) - 1; // 2^n - 1 using bit shift
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Direct Formula, O(1))

#### 📝 Intuition

> - Using math directly: the number of moves is always 2^n - 1.
> - This can be computed in O(1) time and O(1) space.
> - Works efficiently for n ≤ 20 (fits in long long).

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return (1 << n) - 1   // same as 2^n - 1
```

#### 💻 Implementation

**C++:**

```cpp
// Direct formula solution

class Solution {
public:
    long long hanoiMoves(int n) {
        return (n == 0) ? 0 : ((1LL << n) - 1);
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                                | Cons                            |
| ------------- | --------------- | ---------------- | ----------------------------------- | ------------------------------- |
| 🥉 Recursive  | O(2^n)          | O(n)             | Illustrates recursion, step-by-step | Too slow for large n            |
| 🥈 Recurrence | O(1)            | O(1)             | Uses math formula, much faster      | Requires knowing closed form    |
| 🥇 Optimal ⭐ | O(1)            | O(1)             | Cleanest, direct, very efficient    | No step simulation (just count) |

---

<div align="center">

**🎯 Problem 701190 Completed!**

_Happy Coding! 🚀_

</div>
