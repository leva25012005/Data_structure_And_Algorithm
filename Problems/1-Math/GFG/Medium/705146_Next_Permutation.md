<div align="center">

# 🧠 [Next Permutation](https://www.geeksforgeeks.org/problems/next-permutation5226/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/next-permutation5226/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `705146`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Accuracy**     | `40.66%`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/next-permutation5226/1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Topic Tags**   | ![Arrays](https://img.shields.io/badge/-Arrays-blue?style=flat-square) ![permutation](https://img.shields.io/badge/-permutation-blue?style=flat-square) ![constructive algo](https://img.shields.io/badge/-constructive%20algo-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square)                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Company Tags** | ![Infosys](https://img.shields.io/badge/-Infosys-orange?style=flat-square) ![Flipkart](https://img.shields.io/badge/-Flipkart-orange?style=flat-square) ![Amazon](https://img.shields.io/badge/-Amazon-orange?style=flat-square) ![Microsoft](https://img.shields.io/badge/-Microsoft-orange?style=flat-square) ![FactSet](https://img.shields.io/badge/-FactSet-orange?style=flat-square) ![Hike](https://img.shields.io/badge/-Hike-orange?style=flat-square) ![MakeMyTrip](https://img.shields.io/badge/-MakeMyTrip-orange?style=flat-square) ![Google](https://img.shields.io/badge/-Google-orange?style=flat-square) ![Qualcomm](https://img.shields.io/badge/-Qualcomm-orange?style=flat-square) ![Salesforce](https://img.shields.io/badge/-Salesforce-orange?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an array of integers <strong>arr[]</strong> representing a permutation, implement the <strong>next permutation</strong> that rearranges the numbers into the <strong>lexicographically next greater permutation</strong>. If no such permutation exists, rearrange the numbers into the <strong>lowest</strong> possible order (i.e., sorted in ascending order).</p>

<p><strong>Note:</strong> A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> arr[] = [2, 4, 1, 7, 5, 0]
<strong>Output:</strong> [2, 4, 5, 0, 1, 7]
<strong>Explanation:</strong> The next permutation of the given array is [2, 4, 5, 0, 1, 7].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> arr[] = [3, 2, 1]
<strong>Output:</strong> [1, 2, 3]
<strong>Explanation:</strong> As arr[] is the last permutation, the next permutation is the lowest one.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
<strong>Input:</strong> arr[] = [3, 4, 2, 5, 1]
<strong>Output:</strong> [3, 4, 5, 1, 2]
<strong>Explanation:</strong> The next permutation of the given array is [3, 4, 5, 1, 2].
</pre>

## Constraints

<ul>
  <li><code>1 ≤ arr.length ≤ 10^5</code></li>
  <li><code>0 ≤ arr[i] ≤ 10^5</code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `19-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `19-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/next-permutation/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Generate All Permutations)

#### 📝 Intuition

> - Generate all permutations of the array.
> - Sort them lexicographically.
> - Find the current permutation and pick the next one.
> - This is correct but extremely inefficient for large arrays (O(n!)).

#### 🔍 Algorithm

```pseudo
function bruteForce(arr):
    perms = generate all permutations of arr
    sort perms lexicographically
    idx = index of arr in perms
    if idx < len(perms) - 1:
        return perms[idx+1]
    else:
        return perms[0] // wrap around
```

#### 💻 Implementation

```cpp
// Brute force approach (not feasible for large n)

class Solution {
public:
    vector<int> nextPermutationBruteForce(vector<int>& arr) {
        vector<vector<int>> perms;
        sort(arr.begin(), arr.end());

        // Generate all permutations
        do {
            perms.push_back(arr);
        } while (next_permutation(arr.begin(), arr.end()));

        // Find current permutation
        for (int i = 0; i < perms.size(); i++) {
            if (perms[i] == arr) {
                return perms[(i + 1) % perms.size()]; // wrap around
            }
        }
        return {}; // fallback
    }
};
```

### 🥈 Approach 2: Optimized Solution (Standard Algorithm)

#### 📝 Intuition

> - Use the well-known next permutation algorithm:
>   - Traverse from the right to find the first decreasing element (pivot).
>   - Find the smallest element greater than pivot to the right and swap.
>   - Reverse the subarray to the right of the pivot.
> - This runs in O(n) and in-place.

#### 🔍 Algorithm

```pseudo
function nextPermutation(arr):
    // Step 1: Find first decreasing element from right
    i = n-2
    while i >= 0 and arr[i] >= arr[i+1]: i--

    if i >= 0:
        // Step 2: Find element just larger than arr[i] to the right
        j = n-1
        while arr[j] <= arr[i]: j--
        swap(arr[i], arr[j])

    // Step 3: Reverse subarray to the right of i
    reverse(arr, i+1, n-1)
```

#### 💻 Implementation

```cpp
// Optimized in-place next permutation

class Solution {
public:
    void nextPermutationOptimized(vector<int>& arr) {
        int n = arr.size();
        int i = n - 2;

        // Step 1: Find first decreasing element from right
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;

        if (i >= 0) {
            // Step 2: Find the smallest element greater than arr[i]
            int j = n - 1;
            while (arr[j] <= arr[i]) j--;
            swap(arr[i], arr[j]);
        }

        // Step 3: Reverse the elements after i
        reverse(arr.begin() + i + 1, arr.end());
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Same as approach 2, but with clear, concise steps and minimal swaps:
>   - Find pivot
>   - Swap with next bigger number
>   - Reverse suffix
> - This is the canonical solution for next permutation problems.
> - Works in-place with O(n) time and O(1) extra space.

🔍 Algorithm

#### 🔍 Algorithm

```pseudo
function nextPermutation(arr):
    find pivot i from right where arr[i] < arr[i+1]
    if pivot exists:
        find j from right where arr[j] > arr[i]
        swap arr[i], arr[j]
    reverse arr[i+1 to end]
```

#### 💻 Implementation

```cpp
// Most elegant in-place next permutation

class Solution {
public:
    void nextPermutation(vector<int>& arr) {
        int n = arr.size();
        int i = n - 2;

        // Find first decreasing element from right
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;

        if (i >= 0) {
            // Swap with next larger element
            int j = n - 1;
            while (arr[j] <= arr[i]) j--;
            swap(arr[i], arr[j]);
        }

        // Reverse suffix to get the next permutation
        reverse(arr.begin() + i + 1, arr.end());
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                        | Cons                             |
| -------------- | --------------- | ---------------- | --------------------------- | -------------------------------- |
| 🥉 Brute Force | O(n!)           | O(n!)            | Simple, conceptually clear  | Extremely slow for n>10          |
| 🥈 Optimized   | O(n)            | O(1)             | In-place, fast, standard    | Slightly tricky to implement     |
| 🥇 Optimal ⭐  | O(n)            | O(1)             | Elegant, minimal operations | Needs understanding of algorithm |

---

<div align="center">

**🎯 Problem 705146 Completed!**

_Happy Coding! 🚀_

</div>
