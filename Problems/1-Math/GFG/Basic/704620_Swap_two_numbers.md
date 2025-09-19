<div align="center">

# 🧠 [Swap two numbers](https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `704620`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `70.02%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1)                                                                            |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Samsung](https://img.shields.io/badge/-Samsung-orange?style=flat-square)                                                                                        |

## Description

<!-- description:start -->

<p>You are given two numbers <code>a</code> and <code>b</code>. Your task is to swap the given two numbers.</p>

<p><strong>Note:</strong> Try to do it without using a temporary variable.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 13, b = 9
<strong>Output:</strong> 9 13
<strong>Explanation:</strong> After swapping, a becomes 9 and b becomes 13.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 15, b = 8
<strong>Output:</strong> 8 15
<strong>Explanation:</strong> After swapping, a becomes 8 and b becomes 15.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= a, b &lt;= 10<sup>6</sup></code></li>
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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/c-program-swap-two-numbers/)
2. [GeeksforGeeks Article 2](https://www.geeksforgeeks.org/cpp-program-to-swap-two-numbers/)
3. [GeeksforGeeks Article 3](https://www.geeksforgeeks.org/java-program-to-swap-two-numbers/)
4. [GeeksforGeeks Article 4](https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/)
5. [GeeksforGeeks Article 5](https://www.geeksforgeeks.org/swap-two-numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force Using a Temporary Variable

#### 📝 Intuition

> - The most straightforward way to swap two numbers is to use a temporary variable to hold one value while assigning the other.
> - Very simple and readable, but uses extra memory (constant space).

#### 🔍 Algorithm

```pseudo
function swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
```

#### 💻 Implementation

```cpp
// Brute force approach using a temporary variable

class Solution {
public:
    void swapNumbers(int &a, int &b) {
        int temp = a; // Store a temporarily
        a = b;        // Assign b to a
        b = temp;     // Assign temp (original a) to b
    }
};
```

### 🥈 Approach 2: Optimized Solution Using Arithmetic Operations

#### 📝 Intuition

> - Swap numbers without a temporary variable using addition and subtraction:
>   - a = a + b
>   - b = a - b → b = (a + b) - b = a
>   - a = a - b → a = (a + b) - a = b
> - Works only if a + b does not overflow.

#### 🔍 Algorithm

```pseudo
function swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
```

#### 💻 Implementation

```cpp
// Optimized approach using arithmetic operations

class Solution {
public:
    void swapNumbers(int &a, int &b) {
        a = a + b; // Step 1
        b = a - b; // Step 2: b becomes original a
        a = a - b; // Step 3: a becomes original b
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Bitwise XOR)

#### 📝 Intuition

> - Swap numbers without a temporary variable using bitwise XOR:
>   - a = a ^ b
>   - b = a ^ b → b = (a ^ b) ^ b = a
>   - a = a ^ b → a = (a ^ b) ^ a = b
> - Elegant, safe from overflow, works for integers.

#### 🔍 Algorithm

```pseudo
function swap(a, b):
    a = a XOR b
    b = a XOR b
    a = a XOR b
    return a, b
```

#### 💻 Implementation

```cpp
// Most optimal approach using XOR

class Solution {
public:
    void swapNumbers(int &a, int &b) {
        a = a ^ b; // Step 1: XOR a and b
        b = a ^ b; // Step 2: b becomes original a
        a = a ^ b; // Step 3: a becomes original b
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                                   | Cons                    |
| ------------- | --------------- | ---------------- | -------------------------------------- | ----------------------- |
| 🥉 Temp Var   | O(1)            | O(1)             | Simple and readable                    | Uses extra variable     |
| 🥈 Arithmetic | O(1)            | O(1)             | No extra variable, simple math         | Risk of overflow        |
| 🥇 XOR ⭐     | O(1)            | O(1)             | No overflow, no temp variable, elegant | Slightly less intuitive |

---

<div align="center">

**🎯 Problem 704620 Completed!**

_Happy Coding! 🚀_

</div>
