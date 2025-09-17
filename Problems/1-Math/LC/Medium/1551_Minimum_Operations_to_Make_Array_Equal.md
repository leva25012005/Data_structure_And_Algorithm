<div align="center">

# 🧠 [1551. Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%201551-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟡 **Medium**                                                                             |
| **Acceptance Rate** | `82.4%`                                                                                   |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                        |

## Description

<!-- description:start -->

<p>You have an array <code>arr</code> of length <code>n</code> where <code>arr[i] = (2 * i) + 1</code> for all valid values of <code>i</code> (i.e.,&nbsp;<code>0 &lt;= i &lt; n</code>).</p>

<p>In one operation, you can select two indices <code>x</code> and <code>y</code> where <code>0 &lt;= x, y &lt; n</code> and subtract <code>1</code> from <code>arr[x]</code> and add <code>1</code> to <code>arr[y]</code> (i.e., perform <code>arr[x] -=1 </code>and <code>arr[y] += 1</code>). The goal is to make all the elements of the array <strong>equal</strong>. It is <strong>guaranteed</strong> that all the elements of the array can be made equal using some operations.</p>

<p>Given an integer <code>n</code>, the length of the array, return <em>the minimum number of operations</em> needed to make all the elements of arr equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `15-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `15-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                                                                                   | Difficulty    | Relationship    |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------- |
| [Minimum Number of Operations to Make Arrays Similar](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/) | 🔴 **Hard**   | Similar logic   |
| [Minimum Operations to Make Array Equal II](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/)                     | 🟡 **Medium** | Related concept |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Simulate Operations)

#### 📝 Intuition

> - Start with arr[i] = 2\*i + 1.
> - Simulate the operation: pick the largest element and smallest element, decrease the largest by 1 and increase the smallest by 1.
> - Repeat until all elements are equal.
> - This works logically but is too slow for large n.

#### 🔍 Algorithm

```pseudo
function bruteForce(n):
    arr = [2*i + 1 for i in 0..n-1]
    count = 0
    while not all elements equal:
        subtract 1 from max element
        add 1 to min element
        count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach (too slow for large n)

class Solution {
public:
    int minOperations(int n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) arr[i] = 2 * i + 1;

        int count = 0;
        while (true) {
            int minVal = *min_element(arr.begin(), arr.end());
            int maxVal = *max_element(arr.begin(), arr.end());
            if (minVal == maxVal) break; // all elements equal

            // Find indices
            auto x = find(arr.begin(), arr.end(), maxVal) - arr.begin();
            auto y = find(arr.begin(), arr.end(), minVal) - arr.begin();

            arr[x]--; arr[y]++; // Perform operation
            count++;
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - The target value is the middle element, because the array is symmetric and arithmetic: arr = [1, 3, 5, ..., 2*n-1]
> - The median is (arr[0] + arr[n-1])/2 = n.
> - Number of operations is just the sum of differences between elements less than the median and the median.

#### 🔍 Algorithm

```pseudo
function minOperations(n):
    target = n
    result = 0
    for i in 0..n/2 - 1:
        result += target - arr[i]  // only sum for first half
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach using arithmetic property

class Solution {
public:
    int minOperations(int n) {
        int target = n; // Median of array
        int res = 0;
        for (int i = 0; i < n/2; i++) {
            res += target - (2*i + 1); // difference from median
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Mathematical Formula )

#### 📝 Intuition

> Using arithmetic series sum formula:
>
> - First half elements: \(1, 3, 5, \dots, 2 \cdot ( \lfloor n/2 \rfloor ) - 1\)
> - Sum of first half:  
>   \[
>   \text{Sum} =
>   \begin{cases}
>   \left(\frac{n}{2}\right)^2 & \text{if } n \text{ even} \\[2mm]
>   \frac{n-1}{2} \cdot \frac{n+1}{2} & \text{if } n \text{ odd}
>   \end{cases}
>   \]
>
> - Each difference to median = operations required.
>
> - Formula for minimum operations:
>   \[
>   \text{operations} =
>   \begin{cases}
>   \frac{n^2}{4} & \text{if } n \text{ even} \\[1mm]
>   \frac{n^2-1}{4} & \text{if } n \text{ odd}
>   \end{cases}
>   \]

#### 🔍 Algorithm

```pseudo
function minOperationsFormula(n):
    if n % 2 == 0:
        return (n * n) / 4
    else:
        return (n * n - 1) / 4
```

#### 💻 Implementation

```cpp
// Optimal approach using formula

class Solution {
public:
    int minOperations(int n) {
        if (n % 2 == 0)
            return (n * n) / 4;       // even n
        else
            return (n * n - 1) / 4;   // odd n
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                         | Cons                              |
| -------------- | --------------- | ---------------- | ---------------------------- | --------------------------------- |
| 🥉 Brute Force | O(n^2)          | O(n)             | Simple, follows definition   | Too slow for large n              |
| 🥈 Optimized   | O(n)            | O(1)             | Simple logic using median    | Still iterates through half array |
| 🥇 Optimal ⭐  | O(1)            | O(1)             | Fastest, closed-form formula | Need arithmetic insight           |

---

<div align="center">

**🎯 Problem 1551 Completed!**

_Happy Coding! 🚀_

</div>
