<div align="center">

# 🧠 [Multiplication Table](https://www.geeksforgeeks.org/problems/print-table0303/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/print-table0303/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704112`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `44.81%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/print-table0303/1)                                                                                 |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Create the multiplication table from <code>1</code> to <code>10</code> for a given number <code>n</code> and return the table as an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 9 18 27 36 45 54 63 72 81 90
<strong>Explanation:</strong> Multiplying 9 by numbers from 1 to 10 gives the sequence.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2 4 6 8 10 12 14 16 18 20
<strong>Explanation:</strong> Multiplying 2 by numbers from 1 to 10 gives the sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/cpp-program-to-print-multiplication-table-of-a-number/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/program-to-print-multiplication-table-of-a-number/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simple Loop)

#### 📝 Intuition

> - The simplest idea is to iterate from 1 to 10 and multiply each number by n.
> - Collect the results into an array.

#### 🔍 Algorithm

```pseudo
function multiplicationTable(n):
    result = empty array
    for i from 1 to 10:
        result.append(n * i)
    return result
```

#### 💻 Implementation

```cpp
// Brute force approach

class Solution {
public:
    vector<int> multiplicationTable(int n) {
        vector<int> table;
        for (int i = 1; i <= 10; i++) {
            table.push_back(n * i); // Multiply n with i and add to table
        }
        return table;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Using Preallocation)

#### 📝 Intuition

> - Preallocate the array of size 10 to avoid dynamic resizing.
> - Fill the array directly with values n\*i.
> - This is slightly more efficient in terms of memory operations.

#### 🔍 Algorithm

```pseudo
function multiplicationTable(n):
    table = array of size 10
    for i from 1 to 10:
        table[i-1] = n * i
    return table
```

#### 💻 Implementation

```cpp
// Optimized approach with preallocated vector

class Solution {
public:
    vector<int> multiplicationTable(int n) {
        vector<int> table(10); // Preallocate array of size 10
        for (int i = 1; i <= 10; i++) {
            table[i - 1] = n * i; // Fill directly
        }
        return table;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Elegant One-line)

#### 📝 Intuition

> - Use range-based generation using modern C++ features like std::iota and std::transform.
> - Avoid explicit loops if you prefer more elegant code.

#### 🔍 Algorithm

```pseudo
function multiplicationTable(n):
    create array [1,2,...,10]
    multiply each element by n
    return array
```

#### 💻 Implementation

```cpp
#include <vector>
#include <numeric>  // for iota
#include <algorithm> // for transform

class Solution {
public:
    vector<int> multiplicationTable(int n) {
        vector<int> table(10);
        iota(table.begin(), table.end(), 1); // Fill table with 1..10
        transform(table.begin(), table.end(), table.begin(),
                  [n](int x){ return x * n; }); // Multiply each element by n
        return table;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                | Cons                          |
| -------------- | --------------- | ---------------- | ----------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(10)           | O(1) for table   | Simple and easy to read             | Vector resizes dynamically    |
| 🥈 Preallocate | O(10)           | O(1)             | Slightly more efficient memory-wise | Minor extra syntax            |
| 🥇 Elegant ⭐  | O(10)           | O(1)             | Concise, uses modern C++ style      | Might be harder for beginners |

---

<div align="center">

**🎯 Problem 704112 Completed!**

_Happy Coding! 🚀_

</div>
