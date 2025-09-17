<div align="center">

# 🧠 [3609. Minimum Moves to Reach Target in Grid](https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203609-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Difficulty**      | 🔴 **Hard**                                                                              |
| **Acceptance Rate** | `13.6%`                                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                       |

## Description

<!-- description:start -->

<p>You are given a <strong>1-indexed</strong> array of <strong>distinct</strong> integers <code>nums</code> of length <code>n</code>.</p>

<p>You need to distribute all the elements of <code>nums</code> between two arrays <code>arr1</code> and <code>arr2</code> using <code>n</code> operations. In the first operation, append <code>nums[1]</code> to <code>arr1</code>. In the second operation, append <code>nums[2]</code> to <code>arr2</code>. Afterwards, in the <code>i<sup>th</sup></code> operation:</p>

<ul>
	<li>If the last element of <code>arr1</code> is<strong> greater</strong> than the last element of <code>arr2</code>, append <code>nums[i]</code> to <code>arr1</code>. Otherwise, append <code>nums[i]</code> to <code>arr2</code>.</li>
</ul>

<p>The array <code>result</code> is formed by concatenating the arrays <code>arr1</code> and <code>arr2</code>. For example, if <code>arr1 == [1,2,3]</code> and <code>arr2 == [4,5,6]</code>, then <code>result = [1,2,3,4,5,6]</code>.</p>

<p>Return <em>the array</em> <code>result</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3]
<strong>Output:</strong> [2,3,1]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3<sup>rd</sup> operation, as the last element of arr1 is greater than the last element of arr2 (2 &gt; 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,3,8]
<strong>Output:</strong> [5,3,4,8]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3<sup>rd</sup> operation, as the last element of arr1 is greater than the last element of arr2 (5 &gt; 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4<sup>th</sup> operation, as the last element of arr2 is greater than the last element of arr1 (4 &gt; 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li>All elements in <code>nums</code> are distinct.</li>
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

### 🥉 Approach 1: Brute Force (Simulation)

#### 📝 Intuition

> - Directly simulate the process exactly as described:
>   - Start with arr1 = [nums[0]] and arr2 = [nums[1]].
>   - For each i ≥ 2, check the last elements of both arrays.
>   - Append nums[i] to the correct array.
> - Finally, concatenate arr1 + arr2.
> - This is the most straightforward way.

#### 🔍 Algorithm

```pseudo
function bruteForce(nums):
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for i = 2 to n-1:
        if last(arr1) > last(arr2):
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
    return arr1 + arr2
```

#### 💻 Implementation

```cpp
// Brute force simulation

class Solution {
public:
    vector<int> distribute(vector<int>& nums) {
        vector<int> arr1, arr2;
        arr1.push_back(nums[0]); // 1st operation
        arr2.push_back(nums[1]); // 2nd operation

        // Simulate operations
        for (int i = 2; i < nums.size(); i++) {
            if (arr1.back() > arr2.back()) {
                arr1.push_back(nums[i]);
            } else {
                arr2.push_back(nums[i]);
            }
        }

        // Concatenate arr1 and arr2
        vector<int> result = arr1;
        result.insert(result.end(), arr2.begin(), arr2.end());
        return result;
    }
};
```

### 🥈 Approach 2: Optimized Solution (In-place Tracking)

#### 📝 Intuition

> - Instead of storing both arrays fully during simulation,
> - we only need to keep track of their last elements while deciding.
> - We can store the actual elements in arr1 and arr2 but with minimal overhead.
> - This reduces extra comparisons and avoids repeated .back() lookups.

#### 🔍 Algorithm

```pseudo
function optimized(nums):
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    last1 = nums[0]
    last2 = nums[1]
    for i in 2..n-1:
        if last1 > last2:
            arr1.append(nums[i])
            last1 = nums[i]
        else:
            arr2.append(nums[i])
            last2 = nums[i]
    return arr1 + arr2
```

#### 💻 Implementation

```cpp
// Optimized approach with tracking last elements

class Solution {
public:
    vector<int> distribute(vector<int>& nums) {
        vector<int> arr1, arr2;
        arr1.push_back(nums[0]);
        arr2.push_back(nums[1]);

        int last1 = nums[0], last2 = nums[1]; // Track last elements

        for (int i = 2; i < nums.size(); i++) {
            if (last1 > last2) {
                arr1.push_back(nums[i]);
                last1 = nums[i];
            } else {
                arr2.push_back(nums[i]);
                last2 = nums[i];
            }
        }

        vector<int> result = arr1;
        result.insert(result.end(), arr2.begin(), arr2.end());
        return result;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Single-pass with Preallocation)

#### 📝 Intuition

> - Since n ≤ 50, efficiency is not critical, but we can make it clean:
>   - Preallocate result vector of size n.
>   - Maintain two indices (idx1, idx2) where we’ll write elements of arr1 and arr2.
>   - After simulation, concatenate by placing arr2 elements after arr1 elements directly.
> - This avoids extra copying and minimizes memory reallocations.

#### 🔍 Algorithm

```pseudo
function optimal(nums):
    create result array of size n
    arr1 = []
    arr2 = []
    simulate distribution with last1 and last2
    write arr1 first, then arr2 into result
    return result
```

#### 💻 Implementation

```cpp
// Most optimal approach with preallocation

class Solution {
public:
    vector<int> distribute(vector<int>& nums) {
        // Step 1: Simulate
        vector<int> arr1, arr2;
        arr1.reserve(nums.size());
        arr2.reserve(nums.size());

        arr1.push_back(nums[0]);
        arr2.push_back(nums[1]);

        int last1 = nums[0], last2 = nums[1];

        for (int i = 2; i < nums.size(); i++) {
            if (last1 > last2) {
                arr1.push_back(nums[i]);
                last1 = nums[i];
            } else {
                arr2.push_back(nums[i]);
                last2 = nums[i];
            }
        }

        // Step 2: Concatenate into result
        vector<int> result;
        result.reserve(nums.size());
        result.insert(result.end(), arr1.begin(), arr1.end());
        result.insert(result.end(), arr2.begin(), arr2.end());

        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                              | Cons                       |
| -------------- | --------------- | ---------------- | --------------------------------- | -------------------------- |
| 🥉 Brute Force | O(n)            | O(n)             | Straightforward simulation        | Extra `.back()` lookups    |
| 🥈 Optimized   | O(n)            | O(n)             | Tracks last elements efficiently  | Still stores both arrays   |
| 🥇 Optimal ⭐  | O(n)            | O(n)             | Preallocates, clean concatenation | Slightly more complex code |

---

<div align="center">

**🎯 Problem 3609 Completed!**

_Happy Coding! 🚀_

</div>
