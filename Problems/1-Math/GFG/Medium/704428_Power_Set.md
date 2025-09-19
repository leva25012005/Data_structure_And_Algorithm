<div align="center">

# 🧠 [Power Set](https://www.geeksforgeeks.org/problems/power-set4302/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/power-set4302/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704428`                                                                                                                                                                                                                                                                                                                                    |
| **Difficulty**   | 🟡 **Medium**                                                                                                                                                                                                                                                                                                                               |
| **Accuracy**     | `43.3%`                                                                                                                                                                                                                                                                                                                                     |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/power-set4302/1)                                                                                                                                                                                                                                                             |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Bit Magic](https://img.shields.io/badge/-Bit%20Magic-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Snapdeal](https://img.shields.io/badge/-Snapdeal-orange?style=flat-square)                                                                                                                                                                                                                                                                |

## Description

<!-- description:start -->

<p>Given a string <strong>s</strong> of length <strong>n</strong>, find all the <strong>possible non-empty <a href="https://www.geeksforgeeks.org/data-structures/string-subsequence-substring/">subsequences</a></strong> of the string <strong>s</strong> in <strong>lexicographically-sorted</strong> order.</p>

<p><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>AllPossibleStrings()</strong> which takes a string <strong>s</strong> as input and <strong>returns a list</strong> of all possible <strong>non-empty subsequences</strong> of <strong>s</strong> in <strong>lexicographically sorted order</strong>.</p>

<!-- description:end -->

## Examples

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "abc"
<strong>Output:</strong> ["a", "ab", "abc", "ac", "b", "bc", "c"]
<strong>Explanation:</strong> There are 7 possible non-empty subsequences for the string "abc", sorted lexicographically.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "aa"
<strong>Output:</strong> ["a", "a", "aa"]
<strong>Explanation:</strong> There are 3 possible non-empty subsequences for the string "aa", sorted lexicographically.
</pre>

## Constraints

<ul>
  <li><code> ≤ n ≤ 16</code></li>
  <li><code> consists of lowercase English alphabets</code></li>
</ul>

<p><strong>Expected Time Complexity:</strong> O(n * 2^n)<br>
<strong>Expected Auxiliary Space:</strong> O(n * 2^n)</p>

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `19-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `19-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/power-set/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Using Recursion)

#### 📝 Intuition

> - A subsequence is any subset of characters in the original string, in the same order.
> - We can generate all subsequences by deciding for each character whether to include it or not.
> - Finally, we filter out the empty subsequence and sort the results lexicographically.

#### 🔍 Algorithm

```pseudo
function generateAllSubsequences(index, current):
    if index == n:
        if current is not empty: add current to results
        return
    // Include s[index]
    generateAllSubsequences(index + 1, current + s[index])
    // Exclude s[index]
    generateAllSubsequences(index + 1, current)
```

#### 💻 Implementation

```cpp
// Brute force recursive solution
class Solution {
public:
    void dfs(int index, string &s, string current, vector<string> &res) {
        if (index == s.size()) {
            if (!current.empty())
                res.push_back(current); // Add non-empty subsequence
            return;
        }

        // Include current character
        dfs(index + 1, s, current + s[index], res);

        // Exclude current character
        dfs(index + 1, s, current, res);
    }

    vector<string> AllPossibleStrings(string s) {
        vector<string> res;
        dfs(0, s, "", res);
        sort(res.begin(), res.end()); // Sort lexicographically
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Bitmasking)

#### 📝 Intuition

> - Each subsequence can be represented by a bitmask of length n.
> - For each bitmask from 1 to (1 << n) - 1, include the character if its corresponding bit is set.
> - This avoids recursion and is simpler to implement.

#### 🔍 Algorithm

```pseudo
function bitmaskApproach(s):
    n = length of s
    for mask in 1..(2^n - 1):
        subseq = ""
        for i in 0..n-1:
            if bit i of mask is set:
                subseq += s[i]
        add subseq to result
    sort result lexicographically
```

#### 💻 Implementation

```cpp
// Bitmask approach
class Solution {
public:
    vector<string> AllPossibleStrings(string s) {
        int n = s.size();
        vector<string> res;

        // Loop over all bitmasks except 0 (to exclude empty subsequence)
        for (int mask = 1; mask < (1 << n); mask++) {
            string subseq = "";
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    subseq += s[i]; // Include character if bit is set
                }
            }
            res.push_back(subseq);
        }

        sort(res.begin(), res.end()); // Lexicographical sort
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ - Optimized Recursive (Backtracking)

#### 📝 Intuition

> - Similar to Approach 1 but backtracking avoids creating many temporary strings unnecessarily.
> - Pass current by reference and remove last character after recursion (“backtrack”).
> - Still generates all subsequences and sorts them lexicographically.

#### 🔍 Algorithm

```pseudo
function backtrack(index, current):
    if index == n:
        if current not empty: add to results
        return
    // Include current character
    current += s[index]
    backtrack(index + 1, current)
    current.pop() // Remove last character to backtrack
    // Exclude current character
    backtrack(index + 1, current)
```

#### 💻 Implementation

**C++:**

```cpp
// Backtracking approach (space efficient)
class Solution {
public:
    void backtrack(int index, string &s, string &current, vector<string> &res) {
        if (index == s.size()) {
            if (!current.empty())
                res.push_back(current);
            return;
        }

        // Include s[index]
        current.push_back(s[index]);
        backtrack(index + 1, s, current, res);
        current.pop_back(); // backtrack

        // Exclude s[index]
        backtrack(index + 1, s, current, res);
    }

    vector<string> AllPossibleStrings(string s) {
        vector<string> res;
        string current = "";
        backtrack(0, s, current, res);
        sort(res.begin(), res.end());
        return res;
    }
};
```

## 📊 Comparison of Approaches

| Approach           | Time Complexity | Space Complexity | Pros                                  | Cons                           |
| ------------------ | --------------- | ---------------- | ------------------------------------- | ------------------------------ |
| 🥉 Recursive       | O(n \* 2^n)     | O(n \* 2^n)      | Simple, intuitive                     | Creates many temporary strings |
| 🥈 Bitmasking      | O(n \* 2^n)     | O(n \* 2^n)      | Iterative, avoids recursion           | Still sorts at the end         |
| 🥇 Backtracking ⭐ | O(n \* 2^n)     | O(n \* 2^n)      | Efficient, avoids extra string copies | Needs careful push/pop         |

---

<div align="center">

**🎯 Problem 704428 Completed!**

_Happy Coding! 🚀_

</div>
