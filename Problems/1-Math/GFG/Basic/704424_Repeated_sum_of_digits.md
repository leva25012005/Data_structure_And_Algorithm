<div align="center">

# 🧠 [Repeated sum of digits](https://www.geeksforgeeks.org/problems/repeated-sum-of-digits3955/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/repeated-sum-of-digits3955/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `704424`                                                                                                                                                                                                                                               |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                                                                                                           |
| **Accuracy**     | `53.83%`                                                                                                                                                                                                                                               |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/repeated-sum-of-digits3955/1)                                                                                                                                                           |
| **Topic Tags**   | ![number-theory](https://img.shields.io/badge/-number-theory-blue?style=flat-square) ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>Given an integer <code>N</code>, recursively sum the digits of <code>N</code> until we get a single digit. The process can be described as follows:</p>

<pre>
If N &lt; 10    
    digSum(N) = N
Else         
    digSum(N) = digSum(Sum of digits of N)
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> N = 1234
<strong>Output:</strong> 1
<strong>Explanation:</strong> The sum of digits is 1+2+3+4 = 10.
Since 10 has more than one digit, we sum again: 1+0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> N = 9999
<strong>Output:</strong> 9
<strong>Explanation:</strong> The sum of digits is 9+9+9+9 = 36.
Then 3+6 = 9, which is a single digit.
</pre>

<p>&nbsp;</p>
<strong>Your Task:</strong>  
You don't need to read input or print anything. Your task is to complete the function <code>repeatedSumOfDigits()</code> which takes an integer <code>N</code> and returns the repeated sum of digits of <code>N</code>.

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= N &lt;= 10<sup>6</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/digital-rootrepeated-digital-sum-given-integer/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/finding-sum-of-digits-of-a-number-until-sum-becomes-single-digit/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Recursive Sum)

#### 📝 Intuition

> - Repeatedly sum the digits of N using recursion until a single-digit number remains.
> - Straightforward recursive approach.

#### 🔍 Algorithm

```pseudo
function digSum(N):
    if N < 10:
        return N
    sum = sum of digits of N
    return digSum(sum)
```

#### 💻 Implementation

```cpp
// Brute force recursive approach

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        if (N < 10) return N; // Base case: single digit
        int sum = 0;
        int n = N;
        // Sum all digits
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        // Recurse with the sum
        return repeatedSumOfDigits(sum);
    }
};
```

### 🥈 Approach 2: Optimized Solution (Iterative Sum)

#### 📝 Intuition

> - Instead of recursion, repeatedly sum digits in a loop until the number has only one digit.
> - Avoids function call overhead.

#### 🔍 Algorithm

```pseudo
function digSumIterative(N):
    while N >= 10:
        sum = 0
        while N > 0:
            sum += N % 10
            N /= 10
        N = sum
    return N
```

#### 💻 Implementation

```cpp
// Iterative approach

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        while (N >= 10) { // Repeat until N is a single digit
            int sum = 0;
            int n = N;
            while (n > 0) {
                sum += n % 10; // Add last digit
                n /= 10;       // Remove last digit
            }
            N = sum; // Update N to the new sum
        }
        return N;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Digital Root Formula)

#### 📝 Intuition

> - There’s a mathematical shortcut known as digital root:
>   - For any N > 0, the repeated sum of digits is 1 + (N-1) % 9.
> - This gives O(1) time and space solution without loops or recursion.

#### 🔍 Algorithm

```pseudo
function digitalRoot(N):
    if N == 0: return 0
    return 1 + (N-1) % 9
```

#### 💻 Implementation

**C++:**

```cpp
// Optimal O(1) solution using digital root formula

class Solution {
public:
    int repeatedSumOfDigits(int N) {
        if (N == 0) return 0;
        return 1 + (N - 1) % 9; // Digital root formula
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                               | Cons                            |
| ------------- | --------------- | ---------------- | ---------------------------------- | ------------------------------- |
| 🥉 Recursive  | O(d)            | O(d)             | Very intuitive, easy to understand | Uses recursion stack            |
| 🥈 Iterative  | O(d)            | O(1)             | No recursion, safe for large N     | Slightly more code              |
| 🥇 Optimal ⭐ | O(1)            | O(1)             | Fastest, elegant formula           | Needs knowledge of digital root |

---

<div align="center">

**🎯 Problem 704424 Completed!**

_Happy Coding! 🚀_

</div>
