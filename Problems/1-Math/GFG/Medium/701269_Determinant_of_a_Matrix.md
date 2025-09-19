<div align="center">

# 🧠 [Determinant of a Matrix](https://www.geeksforgeeks.org/problems/determinant-of-a-matrix-1587115620/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/determinant-of-a-matrix-1587115620/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `701269`                                                                                                                                                          |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                     |
| **Accuracy**     | `56.66%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/determinant-of-a-matrix-1587115620/1)                                                              |
| **Topic Tags**   | ![Matrix](https://img.shields.io/badge/-Matrix-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given a square matrix of size <strong>n × n</strong>, the task is to find the <a href="https://en.wikipedia.org/wiki/Determinant"><strong>determinant</strong></a> of this matrix.</p>

<!-- description:end -->

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
n = 4
matrix = {{1, 0, 2, -1},
          {3, 0, 0, 5},
          {2, 1, 4, -3},
          {1, 0, 5, 0}}

<strong>Output:</strong> 30

<strong>Explanation:</strong>
Determinant of the given matrix is 30.

</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> 
n = 3
matrix = {{1, 2, 3},
          {4, 5, 6},
          {7, 10, 9}}

<strong>Output:</strong> 12

<strong>Explanation:</strong>
Determinant of the given matrix is 12.

</pre>

## Your Task

<p>You don’t need to read input or print anything. Complete the function <code>determinantOfMatrix()</code> that takes a 2D array <code>matrix</code> and its size <code>n</code> as input parameters and returns the determinant of the matrix.</p>

## Constraints

<ul>
  <li><code>1 ≤ n ≤ 10</code></li>
  <li><code>-10 ≤ matrix[i][j] ≤ 10</code></li>
</code></ul>

## Expected Complexity

<ul>
  <li><strong>Time Complexity:</strong> O(N<sup>4</sup>)</li>
  <li><strong>Auxiliary Space:</strong> O(N<sup>2</sup>)</li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/cpp-program-for-determinant-of-a-matrix/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/determinant-of-a-matrix/)
3. [GeeksforGeeks Article 3](https://www.geeksforgeeks.org/java-program-to-find-the-determinant-of-a-matrix/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursive Expansion)

#### 📝 Intuition

> MThe determinant can be computed recursively using Laplace expansion (cofactor expansion).
>
> For an $n \times n$ matrix:
>
> $$
> \det(A) = \sum_{j=0}^{n-1} (-1)^j \cdot A[0][j] \cdot \det(\text{minor of } A[0][j])
> $$
>
> **Base cases:**
>
> - If $n = 1$, return the single element.
> - If $n = 2$, use formula $\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$.
>
> This works but is exponential in time: $O(n!)$.

#### 🔍 Algorithm

```pseudo
function determinant(matrix, n):
    if n == 1: return matrix[0][0]
    if n == 2: return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for j in 0..n-1:
        submatrix = remove row 0 and column j
        det += ((-1)^j) * matrix[0][j] * determinant(submatrix, n-1)
    return det
```

#### 💻 Implementation

```cpp
// Brute force: recursive Laplace expansion

class Solution {
public:
    int determinantOfMatrix(vector<vector<int>> mat, int n) {
        // Base cases
        if (n == 1) return mat[0][0];
        if (n == 2) return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0];

        int det = 0;
        for (int col = 0; col < n; col++) {
            // Create minor matrix
            vector<vector<int>> submat(n-1, vector<int>(n-1));
            for (int i = 1; i < n; i++) {
                int subcol = 0;
                for (int j = 0; j < n; j++) {
                    if (j == col) continue;
                    submat[i-1][subcol++] = mat[i][j];
                }
            }
            // Cofactor expansion
            int sign = (col % 2 == 0) ? 1 : -1;
            det += sign * mat[0][col] * determinantOfMatrix(submat, n-1);
        }
        return det;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Row Reduction / Gaussian Elimination)

#### 📝 Intuition

> - Determinant can also be computed using row operations to convert the matrix into upper triangular form.
> - The determinant is the product of diagonal elements.
> - Swap rows when needed (each swap changes sign of determinant).
> - Time complexity: O(n^3).

#### 🔍 Algorithm

```pseudo
function determinant(matrix, n):
    det = 1
    for col in 0..n-1:
        find pivot row
        if pivot == 0: return 0
        if row swapped: det = -det
        normalize matrix
    det *= product of diagonal
    return det
```

#### 💻 Implementation

```cpp
// Optimized approach using Gaussian elimination

class Solution {
public:
    int determinantOfMatrix(vector<vector<int>> mat, int n) {
        long long det = 1;

        for (int i = 0; i < n; i++) {
            // Find pivot row
            int pivot = i;
            for (int j = i+1; j < n; j++) {
                if (abs(mat[j][i]) > abs(mat[pivot][i])) {
                    pivot = j;
                }
            }

            // If pivot is zero -> determinant = 0
            if (mat[pivot][i] == 0) return 0;

            // Swap rows if needed
            if (i != pivot) {
                swap(mat[i], mat[pivot]);
                det = -det; // Swapping rows changes sign
            }

            det *= mat[i][i];

            // Eliminate below
            for (int j = i+1; j < n; j++) {
                if (mat[j][i] == 0) continue;
                double ratio = (double)mat[j][i] / mat[i][i];
                for (int k = i; k < n; k++) {
                    mat[j][k] -= ratio * mat[i][k];
                }
            }
        }
        return (int)det;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Gaussian Elimination with Modular Safety)

#### 📝 Intuition

> - Same as Approach 2 but done carefully using integer arithmetic to avoid floating-point precision issues.
> - Since constraints are small (n ≤ 10 and values ≤ 10), we can keep everything in integers safely.
> - This is the most stable, elegant solution for competitive programming.

#### 🔍 Algorithm

```pseudo
function determinant(matrix, n):
    det = 1
    for i in 0..n-1:
        find pivot row
        if pivot element == 0: return 0
        if swapped: det = -det
        for each row below: eliminate using integer operations
    det = product of diagonal
    return det
```

#### 💻 Implementation

```cpp
// Most optimal approach: integer-safe Gaussian elimination

class Solution {
public:
    int determinantOfMatrix(vector<vector<int>> mat, int n) {
        long long det = 1;

        for (int i = 0; i < n; i++) {
            // Find pivot
            int pivot = i;
            for (int j = i+1; j < n; j++) {
                if (abs(mat[j][i]) > abs(mat[pivot][i]))
                    pivot = j;
            }

            if (mat[pivot][i] == 0) return 0;

            // Swap rows if necessary
            if (i != pivot) {
                swap(mat[i], mat[pivot]);
                det = -det;
            }

            det *= mat[i][i];

            // Eliminate below using integer arithmetic
            for (int j = i+1; j < n; j++) {
                while (mat[j][i] != 0) {
                    int t = mat[i][i] / mat[j][i];
                    for (int k = i; k < n; k++) {
                        mat[i][k] -= t * mat[j][k];
                        swap(mat[i][k], mat[j][k]);
                    }
                    det = -det; // Each row swap changes sign
                }
            }
        }
        return (int)det;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                                 | Cons                                 |
| -------------- | --------------- | ---------------- | ------------------------------------ | ------------------------------------ |
| 🥉 Brute Force | O(n!)           | O(n²)            | Very intuitive, recursive definition | Extremely slow for n > 6             |
| 🥈 Optimized   | O(n³)           | O(1)             | Faster with Gaussian elimination     | Uses floating-point (precision risk) |
| 🥇 Optimal ⭐  | O(n³)           | O(1)             | Stable, integer-safe, competitive CP | Code more complex                    |

---

<div align="center">

**🎯 Problem 701269 Completed!**

_Happy Coding! 🚀_

</div>
