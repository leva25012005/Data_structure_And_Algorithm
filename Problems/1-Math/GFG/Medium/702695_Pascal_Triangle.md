<div align="center">

# 🧠 [Pascal Triangle](https://www.geeksforgeeks.org/problems/pascal-triangle0652/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/pascal-triangle0652/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `702695`                                                                                                                                                                                                                                                                                                                      |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                                 |
| **Accuracy**     | `23.68%`                                                                                                                                                                                                                                                                                                                      |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/pascal-triangle0652/1)                                                                                                                                                                                                                                         |
| **Topic Tags**   | ![Arrays](https://img.shields.io/badge/-Arrays-blue?style=flat-square) ![Recursion](https://img.shields.io/badge/-Recursion-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![Adobe](https://img.shields.io/badge/-Adobe-orange?style=flat-square)                                                                                                |

## Description

<!-- description:start -->

<p>Given a positive integer <strong>n</strong>, return the <strong>n<sup>th</sup> row of <a href="https://en.wikipedia.org/wiki/Pascal%27s_triangle" target="_blank" rel="noopener">Pascal's triangle</a>.</strong></p>

<p>Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of the previous row.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" alt="Pascal's Triangle Animation" /></p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> [1, 3, 3, 1]
<strong>Explanation:</strong> The 4th row of Pascal's triangle is [1, 3, 3, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [1, 4, 6, 4, 1]
<strong>Explanation:</strong> The 5th row of Pascal's triangle is [1, 4, 6, 4, 1].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The 1st row of Pascal's triangle is [1].
</pre>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 30</code></li>
</ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(n)</li>
  <li><strong>Auxiliary Space:</strong> O(n)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/find-the-nth-row-in-pascals-triangle/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/java-program-to-print-star-pascals-triangle/)
3. [GeeksforGeeks Article 3](https://www.geeksforgeeks.org/pascal-triangle/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Build Full Pascal’s Triangle)

#### 📝 Intuition

> - The simplest way: construct Pascal’s triangle row by row.
> - Start with the first row [1].
> - Each row is formed by summing adjacent numbers from the previous row, with 1 at both ends.
> - Continue until reaching row n.
> - This works but wastes memory since we only need the nth row.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    triangle = [[1]]
    for i in 2..n:
        prev = last row in triangle
        newRow = [1]
        for j in 1..len(prev)-1:
            newRow.append(prev[j-1] + prev[j])
        newRow.append(1)
        triangle.append(newRow)
    return triangle[n-1]
```

#### 💻 Implementation

```cpp
// Brute force: build full Pascal's triangle
class Solution {
public:
    vector<int> getRow(int n) {
        vector<vector<int>> triangle;
        triangle.push_back({1}); // first row

        for (int i = 1; i < n; i++) {
            vector<int> prev = triangle.back();
            vector<int> row(i + 1, 1); // row always starts/ends with 1
            for (int j = 1; j < i; j++) {
                row[j] = prev[j - 1] + prev[j]; // sum of two above
            }
            triangle.push_back(row);
        }
        return triangle[n - 1]; // nth row (1-indexed in problem)
    }
};
```

### 🥈 Approach 2: Optimized Solution - : Iterative Row Construction (One Row at a Time)

#### 📝 Intuition

> - Instead of storing the entire triangle, build row by row in place.
> - Start with [1], then compute the next row using only the current one.
> - Repeat until reaching row n.
> - Saves space compared to Approach 1.

#### 🔍 Algorithm

```pseudo
function optimized(n):
    row = [1]
    for i in 2..n:
        newRow = [1]
        for j in 1..len(row)-1:
            newRow.append(row[j-1] + row[j])
        newRow.append(1)
        row = newRow
    return row
```

#### 💻 Implementation

```cpp
// Optimized: only keep the current row
class Solution {
public:
    vector<int> getRow(int n) {
        vector<int> row = {1};
        for (int i = 1; i < n; i++) {
            vector<int> newRow(i + 1, 1);
            for (int j = 1; j < i; j++) {
                newRow[j] = row[j - 1] + row[j];
            }
            row = newRow;
        }
        return row;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Using Binomial Coefficient)

#### 📝 Intuition

> The $n$th row of Pascal’s triangle is just binomial coefficients:
>
> $$
> C(n-1,0), \; C(n-1,1), \; \dots, \; C(n-1,n-1)
> $$
>
> We can compute them iteratively:
>
> $$
> C(n,k) = C(n,k-1) \times \frac{n-k+1}{k}
> $$
>
> This avoids building any triangle, just compute directly.

#### 🔍 Algorithm

```pseudo
function optimal(n):
    row = []
    val = 1
    for k in 0..n-1:
        row.append(val)
        val = val * (n-1-k) / (k+1)
    return row
```

#### 💻 Implementation

```cpp
// Optimal: directly compute binomial coefficients
class Solution {
public:
    vector<int> getRow(int n) {
        vector<int> row;
        long long val = 1;
        for (int k = 0; k < n; k++) {
            row.push_back((int)val); // C(n-1, k)
            val = val * (n - 1 - k) / (k + 1); // recurrence relation
        }
        return row;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                                |
| -------------- | --------------- | ---------------- | ------------------------------------ | ----------------------------------- |
| 🥉 Brute Force | O(n²)           | O(n²)            | Very intuitive, builds full triangle | Wastes memory and time              |
| 🥈 Optimized   | O(n²)           | O(n)             | Only keeps the current row           | Still quadratic time                |
| 🥇 Optimal ⭐  | O(n)            | O(n)             | Fastest, elegant, uses math formula  | Requires careful handling of `long` |

---

<div align="center">

**🎯 Problem 702695 Completed!**

_Happy Coding! 🚀_

</div>
