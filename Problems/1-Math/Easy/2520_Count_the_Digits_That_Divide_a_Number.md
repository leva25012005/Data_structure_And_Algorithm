<div align="center">

# 🧠 [2520. Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202520-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/count-the-digits-that-divide-a-number/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                              |
| **Acceptance Rate** | `85.9%`                                                                                  |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)                       |

## Description

<!-- description:start -->

<p>Given an integer <code>num</code>, return <em>the number of digits in <code>num</code> that divide </em><code>num</code>.</p>

<p>An integer <code>val</code> divides <code>nums</code> if <code>nums % val == 0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> 1
<strong>Explanation:</strong> 7 divides itself, hence the answer is 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 121
<strong>Output:</strong> 2
<strong>Explanation:</strong> 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 1248
<strong>Output:</strong> 4
<strong>Explanation:</strong> 1248 is divisible by all of its digits, hence the answer is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>num</code> does not contain <code>0</code> as one of its digits.</li>
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

| Problem                                                                       | Difficulty  | Relationship    |
| ----------------------------------------------------------------------------- | ----------- | --------------- |
| [Happy Number](https://leetcode.com/problems/happy-number/)                   | 🟢 **Easy** | Similar logic   |
| [Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/) | 🟢 **Easy** | Related concept |

## 🏢 Companies Asked (Frequency)

### 🔥 High Frequency (80%+)

_No high frequency companies_

### ⭐ Medium Frequency (60-79%)

_No medium frequency companies_

### 📈 Regular Frequency (40-59%)

- **tcs** 📈 59.9%

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force

#### 📝 Intuition

> The most direct way is to iterate through each digit of num and check if it divides num. Since the number can have at most 10 digits (because num ≤ 10^9), this brute force solution is feasible.

#### 🔍 Algorithm

```pseudo
function countDividingDigits(num):
    count = 0
    for each digit d in num:
        if num % d == 0:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Brute Force Approach

class Solution {
public:
    int countDigits(int num) {
        int count = 0;
        int temp = num; // store the original number
        while (temp > 0) {
            int d = temp % 10;  // extract last digit
            if (num % d == 0) { // check divisibility
                count++;
            }
            temp /= 10; // move to next digit
        }
        return count;
    }
};
```

### 🥈 Approach 2: Optimized Solution

#### 📝 Intuition

> Instead of repeatedly using % and / to extract digits, we can convert num to a string and directly iterate over the characters. This makes the code shorter and easier to read.

#### 🔍 Algorithm

```pseudo
function countDividingDigits(num):
    convert num to string
    count = 0
    for each char c in string:
        d = int(c)
        if num % d == 0:
            count += 1
    return count
```

#### 💻 Implementation

```cpp
// Optimized with string conversion

class Solution {
public:
    int countDigits(int num) {
        int count = 0;
        string s = to_string(num); // convert number to string
        for (char c : s) {
            int d = c - '0';       // convert char to int
            if (num % d == 0) {    // check divisibility
                count++;
            }
        }
        return count;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐

#### 📝 Intuition

> - Both brute force and string conversion are already O(d) where d ≤ 10. Since the constraints are small, the time complexity is effectively constant.
> - The optimal solution focuses on clean, readable code rather than performance improvement, because all approaches run fast.
> - We just combine digit extraction in a concise loop with minimal operations.

#### 🔍 Algorithm

```pseudo
// function countDividingDigits(num):
    return sum(1 for each digit d in num if num % d == 0)

```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int countDigits(int num) {
        int result = 0;
        for (int temp = num; temp > 0; temp /= 10) {
            int d = temp % 10;     // extract digit
            result += (num % d == 0); // increment if divisible
        }
        return result;
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                               | Cons                    |
| -------------- | --------------- | ---------------- | ---------------------------------- | ----------------------- |
| 🥉 Brute Force | O(d) (d ≤ 10)   | O(1)             | Straightforward, easy to implement | Slightly verbose        |
| 🥈 Optimized   | O(d)            | O(d) (string)    | Cleaner using string iteration     | Extra string conversion |
| 🥇 Optimal ⭐  | O(d)            | O(1)             | Concise, elegant, no extra memory  | Similar logic as brute  |

---

<div align="center">

**🎯 Problem 2520 Completed!**

_Happy Coding! 🚀_

</div>
