<div align="center">

# 🧠 [2198. Number of Single Divisor Triplets](https://leetcode.com/problems/number-of-single-divisor-triplets/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202198-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/number-of-single-divisor-triplets/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Difficulty**      | 🟡 **Medium**                                                                        |
| **Acceptance Rate** | `54.3%`                                                                              |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/number-of-single-divisor-triplets/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                   |

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of positive integers <code>nums</code>. A triplet of three <strong>distinct</strong> indices <code>(i, j, k)</code> is called a <strong>single divisor triplet</strong> of <code>nums</code> if <code>nums[i] + nums[j] + nums[k]</code> is divisible by <strong>exactly one</strong> of <code>nums[i]</code>, <code>nums[j]</code>, or <code>nums[k]</code>.</p>
Return <em>the number of <strong>single divisor triplets</strong> of </em><code>nums</code><em>.</em>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,6,7,3,2]
<strong>Output:</strong> 12
<strong>Explanation:
</strong>The triplets (0, 3, 4), (0, 4, 3), (3, 0, 4), (3, 4, 0), (4, 0, 3), and (4, 3, 0) have the values of [4, 3, 2] (or a permutation of [4, 3, 2]).
4 + 3 + 2 = 9 which is only divisible by 3, so all such triplets are single divisor triplets.
The triplets (0, 2, 3), (0, 3, 2), (2, 0, 3), (2, 3, 0), (3, 0, 2), and (3, 2, 0) have the values of [4, 7, 3] (or a permutation of [4, 7, 3]).
4 + 7 + 3 = 14 which is only divisible by 7, so all such triplets are single divisor triplets.
There are 12 single divisor triplets in total.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The triplets (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), and (2, 1, 0) have the values of [1, 2, 2] (or a permutation of [1, 2, 2]).
1 + 2 + 2 = 5 which is only divisible by 1, so all such triplets are single divisor triplets.
There are 6 single divisor triplets in total.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
There are no single divisor triplets.
Note that (0, 1, 2) is not a single divisor triplet because nums[0] + nums[1] + nums[2] = 3 and 3 is divisible by nums[0], nums[1], and nums[2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
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

| Problem                                                                                             | Difficulty  | Relationship  |
| --------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| [Count Array Pairs Divisible by K](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) | 🔴 **Hard** | Similar logic |

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> - Check all possible ordered triplets (i, j, k) with distinct indices.
> - Compute the sum = nums[i] + nums[j] + nums[k].
> - Check if the sum is divisible by exactly one of nums[i], nums[j], nums[k].
> - Count all valid triplets.
> - This works but is extremely slow (O(n^3)).

#### 🔍 Algorithm

```pseudo
function bruteForce(nums):
    n = length(nums)
    count = 0
    for i in 0..n-1:
        for j in 0..n-1:
            for k in 0..n-1:
                if i, j, k distinct:
                    sum = nums[i] + nums[j] + nums[k]
                    divisors = 0
                    if sum % nums[i] == 0: divisors++
                    if sum % nums[j] == 0: divisors++
                    if sum % nums[k] == 0: divisors++
                    if divisors == 1: count++
    return count
```

#### 💻 Implementation

```cpp
// Brute force approach: O(n^3), only works for small inputs

class Solution {
public:
    long long solutionBruteForce(vector<int>& nums) {
        int n = nums.size();
        long long count = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (i == j || j == k || i == k) continue; // indices must be distinct

                    int sum = nums[i] + nums[j] + nums[k];
                    int divisors = 0;

                    if (sum % nums[i] == 0) divisors++;
                    if (sum % nums[j] == 0) divisors++;
                    if (sum % nums[k] == 0) divisors++;

                    if (divisors == 1) count++;
                }
            }
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> - Values of nums[i] are small (≤ 100).
> - Instead of iterating over indices, we iterate over values.
> - Count frequency of each number (from 1 to 100).
> - Pick three values (a, b, c) with their counts, check condition.
> - For each valid triplet of values, compute how many index triplets exist using combinatorics.
> - This reduces complexity from O(n^3) to about O(100^3) = 1,000,000 (feasible).

#### 🔍 Algorithm

```pseudo
function optimized(nums):
    freq = count frequency of each number in nums
    result = 0
    for a in 1..100:
        for b in 1..100:
            for c in 1..100:
                if freq[a], freq[b], freq[c] > 0:
                    sum = a+b+c
                    divisors = (sum%a==0) + (sum%b==0) + (sum%c==0)
                    if divisors == 1:
                        result += countTriplets(a, b, c, freq)
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach using frequency map

class Solution {
public:
    long long solutionOptimized(vector<int>& nums) {
        vector<long long> freq(101, 0); // freq[x] = count of number x
        for (int x : nums) freq[x]++;

        long long res = 0;

        // Iterate over all possible values of a, b, c
        for (int a = 1; a <= 100; a++) {
            for (int b = 1; b <= 100; b++) {
                for (int c = 1; c <= 100; c++) {
                    if (freq[a] == 0 || freq[b] == 0 || freq[c] == 0) continue;

                    int sum = a + b + c;
                    int divisors = (sum % a == 0) + (sum % b == 0) + (sum % c == 0);

                    if (divisors == 1) {
                        // Count combinations of indices
                        if (a == b && b == c) {
                            // All equal
                            if (freq[a] >= 3) {
                                res += freq[a] * (freq[a]-1) * (freq[a]-2);
                            }
                        } else if (a == b) {
                            // Two equal
                            if (freq[a] >= 2) res += freq[a] * (freq[a]-1) * freq[c];
                        } else if (b == c) {
                            if (freq[b] >= 2) res += freq[b] * (freq[b]-1) * freq[a];
                        } else if (a == c) {
                            if (freq[a] >= 2) res += freq[a] * (freq[a]-1) * freq[b];
                        } else {
                            // All distinct
                            res += freq[a] * freq[b] * freq[c];
                        }
                    }
                }
            }
        }

        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Notice nums[i] ≤ 100.
> - We only need to check unique triplets (a, b, c) with a ≤ b ≤ c.
> - Compute once and multiply by permutations:
>   - If all distinct → multiply by 6 (since 3! permutations).
>   - If two equal → multiply by 3.
>   - If all equal → multiply by 1.
> - This cuts redundant checks and makes it ~O(100^3 / 6) ≈ 166,000 iterations.

#### 🔍 Algorithm

```pseudo
function optimal(nums):
    freq = frequency map
    result = 0
    for a in 1..100:
        for b in a..100:
            for c in b..100:
                if freq[a], freq[b], freq[c] > 0:
                    sum = a+b+c
                    divisors = (sum%a==0) + (sum%b==0) + (sum%c==0)
                    if divisors == 1:
                        count = numberOfWays(a, b, c, freq)
                        result += count
    return result
```

#### 💻 Implementation

```cpp
// Most optimal approach: avoid redundant permutations

class Solution {
public:
    long long numSingleDivisorTriplets(vector<int>& nums) {
        vector<long long> freq(101, 0);
        for (int x : nums) freq[x]++;

        long long res = 0;

        for (int a = 1; a <= 100; a++) {
            for (int b = a; b <= 100; b++) {
                for (int c = b; c <= 100; c++) {
                    if (freq[a] == 0 || freq[b] == 0 || freq[c] == 0) continue;

                    int sum = a + b + c;
                    int divisors = (sum % a == 0) + (sum % b == 0) + (sum % c == 0);

                    if (divisors == 1) {
                        if (a == b && b == c) {
                            // All equal
                            if (freq[a] >= 3) {
                                res += freq[a] * (freq[a]-1) * (freq[a]-2);
                            }
                        } else if (a == b && b != c) {
                            if (freq[a] >= 2) res += freq[a] * (freq[a]-1) * freq[c] * 3; // 3 permutations
                        } else if (b == c && a != b) {
                            if (freq[b] >= 2) res += freq[b] * (freq[b]-1) * freq[a] * 3;
                        } else if (a == c && a != b) {
                            if (freq[a] >= 2) res += freq[a] * (freq[a]-1) * freq[b] * 3;
                        } else {
                            // All distinct
                            res += freq[a] * freq[b] * freq[c] * 6; // 6 permutations
                        }
                    }
                }
            }
        }

        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity         | Space Complexity | Pros                                     | Cons                   |
| -------------- | ----------------------- | ---------------- | ---------------------------------------- | ---------------------- |
| 🥉 Brute Force | O(n³)                   | O(1)             | Very intuitive                           | Impossible for n > 100 |
| 🥈 Optimized   | O(100³) = 1,000,000     | O(100)           | Uses frequency map, feasible             | Some redundant checks  |
| 🥇 Optimal ⭐  | \~O(100³ / 6) ≈ 166,000 | O(100)           | Efficient, avoids duplicates, clean code | A bit more complex     |

---

<div align="center">

**🎯 Problem 2198 Completed!**

_Happy Coding! 🚀_

</div>
