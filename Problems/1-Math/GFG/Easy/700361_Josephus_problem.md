<div align="center">

# 🧠 [Josephus problem](https://www.geeksforgeeks.org/problems/josephus-problem/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/josephus-problem/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `700361`                                                                                                                                                                                                                                               |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                            |
| **Accuracy**     | `57.26%`                                                                                                                                                                                                                                               |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/josephus-problem/1)                                                                                                                                                                     |
| **Topic Tags**   | ![Recursion](https://img.shields.io/badge/-Recursion-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![Walmart](https://img.shields.io/badge/-Walmart-orange?style=flat-square)                     |

## Description

<!-- description:start -->

<p>You are playing a game with <code>n</code> people standing in a circle, numbered from <code>1</code> to <code>n</code>. Starting from person 1, every <strong>k<sup>th</sup></strong> person is eliminated in a circular fashion. The process continues until only one person remains.</p>

<p>Given integers <code>n</code> and <code>k</code>, return the position (1-based index) of the person who will survive.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 persons. Skipping 1 person, the 2nd person will be eliminated. The safe position is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 5 persons. Skipping 2 persons, the 3rd person will be eliminated. The safe position is 4.
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 7, k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Eliminating every 2nd person in a circle of 7, the last remaining person is at position 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n, k &lt;= 20</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `18-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `18-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/josephus-problem/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Simulate the elimination process using a list.
> - Start from the first person, skip k-1 people, and remove the k-th person.
> - Repeat until only one person remains.
> - This is intuitive but less elegant.

#### 🔍 Algorithm

```pseudo
function josephus_brute(n, k):
    people = [1..n]
    index = 0
    while length(people) > 1:
        index = (index + k - 1) % length(people)
        remove person at index
    return people[0]
```

#### 💻 Implementation

**C++:**

```cpp
// Brute force approach using vector simulation

class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int> people(n);
        iota(people.begin(), people.end(), 1); // Fill 1..n

        int index = 0;
        while (people.size() > 1) {
            // Compute the index of person to eliminate
            index = (index + k - 1) % people.size();
            people.erase(people.begin() + index); // Remove person
        }
        return people[0]; // Last remaining person
    }
};
```

### 🥈 Approach 2: Optimized Solution (Recursive Josephus Formula)

#### 📝 Intuition

> - he Josephus problem has a mathematical recursive solution:
>   - For 1 person, survivor = 0 (0-indexed).
>   - For n people: survivor(n) = (survivor(n-1) + k) % n.
> - Convert to 1-indexed at the end.
> - This avoids simulating all eliminations explicitly.

#### 🔍 Algorithm

```pseudo
function josephus_recursive(n, k):
    if n == 1: return 0
    return (josephus_recursive(n-1, k) + k) % n
```

#### 💻 Implementation

```cpp
// Recursive Josephus formula

class Solution {
public:
    int findTheWinner(int n, int k) {
        // Recursive helper (0-indexed)
        function<int(int)> josephus = [&](int n) -> int {
            if (n == 1) return 0;
            return (josephus(n - 1) + k) % n;
        };
        return josephus(n) + 1; // Convert to 1-indexed
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Iterative)

#### 📝 Intuition

> - Use the iterative version of the recursive formula to avoid recursion overhead.
> - Start with 1 person and build up to n.
> - Very efficient: O(n) time, O(1) space.

#### 🔍 Algorithm

```pseudo
function josephus_iterative(n, k):
    survivor = 0
    for i = 2 to n:
        survivor = (survivor + k) % i
    return survivor + 1  // Convert to 1-indexed
```

#### 💻 Implementation

```cpp
// Iterative optimal Josephus solution

class Solution {
public:
    int findTheWinner(int n, int k) {
        int survivor = 0; // 0-indexed
        for (int i = 2; i <= n; i++) {
            survivor = (survivor + k) % i; // Update survivor for i persons
        }
        return survivor + 1; // Convert to 1-indexed
    }
};
```

## 📊 Comparison of Approaches

| Approach        | Time Complexity | Space Complexity | Pros                                  | Cons                    |
| --------------- | --------------- | ---------------- | ------------------------------------- | ----------------------- |
| 🥉 Brute Force  | O(n²)           | O(n)             | Easy to understand, direct simulation | Slow for large n        |
| 🥈 Recursive    | O(n)            | O(n) recursion   | Elegant formula-based solution        | Uses recursion stack    |
| 🥇 Iterative ⭐ | O(n)            | O(1)             | Most efficient, avoids recursion      | Slightly less intuitive |

---

<div align="center">

**🎯 Problem 700361 Completed!**

_Happy Coding! 🚀_

</div>
