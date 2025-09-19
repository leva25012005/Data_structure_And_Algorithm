<div align="center">

# 🧠 [GCD of two numbers](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `703672`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `51.03%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)                                                                          |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |
| **Company Tags** | ![Accenture](https://img.shields.io/badge/-Accenture-orange?style=flat-square) ![TCS](https://img.shields.io/badge/-TCS-orange?style=flat-square)                 |

## Description

<!-- description:start -->

<p>Given two positive integers <code>a</code> and <code>b</code>, find the <strong>Greatest Common Divisor (GCD)</strong> of <code>a</code> and <code>b</code>.</p>

<p><strong>Note:</strong> Do not use the inbuilt gcd function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 20, b = 28
<strong>Output:</strong> 4
<strong>Explanation:</strong> GCD of 20 and 28 is 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 60, b = 36
<strong>Output:</strong> 12
<strong>Explanation:</strong> GCD of 60 and 36 is 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= a, b &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(log(min(a, b)))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</p>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `17-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `17-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Check Divisors)

#### 📝 Intuition

> - Start from min(a, b) and check downwards.
> - The first number that divides both a and b is the GCD.
> - This is simple but very slow for large numbers.

#### 🔍 Algorithm

```pseudo
function bruteForce(a, b):
    m = min(a, b)
    for i from m down to 1:
        if a % i == 0 and b % i == 0:
            return i
```

#### 💻 Implementation

```cpp
// Brute force solution

class Solution {
public:
    int gcdBruteForce(int a, int b) {
        int m = min(a, b);
        // Check all numbers from m down to 1
        for (int i = m; i >= 1; i--) {
            if (a % i == 0 && b % i == 0) {
                return i; // First common divisor found
            }
        }
        return 1; // Default case
    }
};
```

### 🥈 Approach 2: Optimized Solution (Subtraction-based Euclidean Algorithm)

#### 📝 Intuition

> - Euclid’s algorithm: GCD(a, b) = GCD(b, a-b) when a > b.
> - Keep subtracting the smaller from the larger until both are equal.
> - When a == b, that’s the GCD.
> - This is more efficient but still slower than modulo-based.

#### 🔍 Algorithm

```pseudo
function gcdSubtraction(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
```

#### 💻 Implementation

```cpp
// Euclidean algorithm (subtraction method)

class Solution {
public:
    int gcdSubtraction(int a, int b) {
        if (a == 0)
		    return b;
		if (b == 0)
		    return a;
		if (a == b)
		    return a;

        while (a != b) {
            if (a > b) a = a - b;
            else b = b - a;
        }
        return a; // When a == b, that's the GCD
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Modulo-based Euclidean Algorithm)

#### 📝 Intuition

> - Instead of repeated subtraction, use modulo:
>   - GCD(a, b) = GCD(b, a % b).
> - Keep applying until b == 0.
> - At that point, a is the GCD.
> - This runs in O(log(min(a, b))), very fast.

#### 🔍 Algorithm

```pseudo
function gcdOptimal(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
```

#### 💻 Implementation

```cpp
// Most optimal solution: Euclidean algorithm (modulo)

class Solution {
public:
    int gcdOptimal(int a, int b) {
        if (a == 0)
		    return b;
		if (b == 0)
		    return a;
		if (a == b)
		    return a;

        while (b != 0) {
            int temp = b;
            b = a % b; // Remainder becomes new b
            a = temp;  // Swap roles
        }
        return a; // GCD found
    }
};
```

### 🥇 Approach 4: Optimal Solution ⭐ ( ptimized Euclidean Algorithm by Checking Remainder)

#### 📝 Intuition

> - Instead of the Euclidean algorithm by subtraction, a better approach can be used
> - We don't perform subtraction here. we continuously divide the bigger number by the smaller number.
> - More can be learned about this efficient solution by using the modulo operator in Euclidean algorithm-

#### 🔍 Algorithm

```pseudo
function gcdOptimal(a, b):
    return b == 0 ? a : gcd(b, a % b);
```

#### 💻 Implementation

```cpp
// Most optimal solution: Euclidean algorithm (modulo)

class Solution {
public:
    int gcdOptimal(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
};
```

### 🥇 Approach 5: Optimal Solution ⭐ ( Using Built-in Function)

#### 📝 Intuition

> - Languages like C++ have inbuilt functions to calculate GCD of two numbers.

#### 🔍 Algorithm

#### 💻 Implementation

```cpp
// Most optimal solution: Euclidean algorithm (modulo)
#include <algorithm>
#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    return __gcd(a, b);
}
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity    | Space Complexity | Pros                              | Cons                          |
| -------------- | ------------------ | ---------------- | --------------------------------- | ----------------------------- |
| 🥉 Brute Force | O(min(a, b))       | O(1)             | Very simple, easy to understand   | Too slow for large numbers    |
| 🥈 Subtraction | O(max(a, b)) worst | O(1)             | Better than brute force           | Still inefficient for big gap |
| 🥇 Optimal 1⭐ | O(log(min(a, b)))  | O(1)             | Fastest, elegant, works up to 1e9 | None                          |
| 🥇 Optimal 2⭐ | O(log(min(a,b)))   | O(log(min(a,b))) | Fastest, elegant                  | None                          |
| 🥇 Optimal 3⭐ | O(log(min(a,b)))   | O(1)             | Fastest, Easy                     | None                          |

---

<div align="center">

**🎯 Problem 703672 Completed!**

_Happy Coding! 🚀_

</div>
```
