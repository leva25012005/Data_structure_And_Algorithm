<div align="center">

# 🧠 [The dice problem](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704133`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `73.72%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/the-dice-problem2316/1)                                                                            |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>You are given a <strong>cubic dice</strong> with <strong>6</strong> faces. All the individual faces have a number printed on them. The numbers are in the range of <strong>1 to 6</strong>, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong> For dice facing number 6, the opposite face will have the number 1.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> For dice facing number 2, the opposite face will have the number 5.
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 6</code></li>
</ul>

<p>&nbsp;</p>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/the-dice-problem/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Hardcoded Mapping)

#### 📝 Intuition

> - A standard dice always has opposite faces that sum to 7: (1,6), (2,5), (3,4).
> - We can hardcode a mapping between faces.

🔍 Algorithm

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    create a dictionary {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    return dict[n]
```

#### 💻 Implementation

```cpp
// Brute force with hardcoded mapping

class Solution {
public:
    int oppositeFace(int n) {
        // Direct mapping of each face
        if (n == 1) return 6;
        if (n == 2) return 5;
        if (n == 3) return 4;
        if (n == 4) return 3;
        if (n == 5) return 2;
        if (n == 6) return 1;
        return -1; // invalid input
    }
};
```

### 🥈 Approach 2: Optimized Solution (Array)

#### 📝 Intuition

> - Instead of multiple if-else, store the mapping in an array.
> - Since input is from 1 to 6, we can directly index into the array.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    mapping = [0, 6, 5, 4, 3, 2, 1]
    return mapping[n]
```

#### 💻 Implementation

```cpp
// Optimized using array mapping

class Solution {
public:
    int oppositeFace(int n) {
        // Index 0 is unused
        int mapping[7] = {0, 6, 5, 4, 3, 2, 1};
        return mapping[n];
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ - Mathematical Formula

#### 📝 Intuition

> - On a standard dice, opposite faces always add up to 7.
> - So the opposite face of n is simply 7 - n.
>   -This is the cleanest and most efficient approach.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    return 7 - n
```

#### 💻 Implementation

```cpp
// Most optimal using math formula

class Solution {
public:
    int oppositeFace(int n) {
        return 7 - n; // Opposite faces always sum to 7
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                         | Cons                               |
| -------------- | --------------- | ---------------- | ---------------------------- | ---------------------------------- |
| 🥉 Brute Force | O(1)            | O(1)             | Very explicit and clear      | Verbose, long                      |
| 🥈 Optimized   | O(1)            | O(1)             | Compact, avoids many if-else | Still extra array                  |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Cleanest, single formula     | Assumes knowledge of dice property |

---

<div align="center">

**🎯 Problem 704133 Completed!**

_Happy Coding! 🚀_

</div>
