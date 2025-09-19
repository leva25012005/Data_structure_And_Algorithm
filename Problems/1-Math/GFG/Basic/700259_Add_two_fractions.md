<div align="center">

# 🧠 [Add two fractions](https://www.geeksforgeeks.org/problems/add-two-fractions/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/add-two-fractions/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem ID**   | `700259`                                                                                                                                                          |
| **Difficulty**   | ⚪ **Basic**                                                                                                                                                      |
| **Accuracy**     | `33.11%`                                                                                                                                                          |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/add-two-fractions/1)                                                                               |
| **Topic Tags**   | ![Mathematical](https://img.shields.io/badge/-Mathematical-blue?style=flat-square) ![Algorithms](https://img.shields.io/badge/-Algorithms-blue?style=flat-square) |

## Description

<!-- description:start -->

<p>You are given four numbers <code>num1</code>, <code>den1</code>, <code>num2</code>, and <code>den2</code>. You need to compute <code>(num1/den1) + (num2/den2)</code> and output the result in the form of <strong>num/den</strong> in reduced form.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 1, den1 = 500, num2 = 2, den2 = 500
<strong>Output:</strong> 3/500
<strong>Explanation:</strong> (1/500) + (2/500) = 3/500
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 1, den1 = 2, num2 = 1, den2 = 3
<strong>Output:</strong> 5/6
<strong>Explanation:</strong> (1/2) + (1/3) = 5/6 after reducing the fraction.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num1 = 2, den1 = 7, num2 = 3, den2 = 5
<strong>Output:</strong> 31/35
<strong>Explanation:</strong> (2/7) + (3/5) = (10/35 + 21/35) = 31/35
</pre>

<p>&nbsp;</p>
<strong>Your Task:</strong>  
You don't need to read input or print anything. Your task is to complete the function <code>addFraction(num1, den1, num2, den2)</code> which adds the two fractions and returns the resulting fraction in reduced form.

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= T &lt;= 100</code></li>
  <li><code>1 &lt;= den1, den2, num1, num2 &lt;= 1000</code></li>
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

## 📚 Related Articles

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-to-add-two-fractions/)

---

## 💡 Solutions

### 🥈 Approach 1: Optimized Solution (Using LCM of Denominators)

#### 📝 Intuition

> - Instead of multiplying denominators directly, find the LCM of den1 and den2.
> - Convert fractions to this denominator and sum.
> - Reduces overflow risk compared to brute force.

#### 🔍 Algorithm

```pseudo
function optimized(num1, den1, num2, den2):
    lcm = den1 * den2 / gcd(den1, den2)
    num = num1 * (lcm/den1) + num2 * (lcm/den2)
    den = lcm
    g = gcd(num, den)
    return (num/g, den/g)
```

#### 💻 Implementation

```cpp
// Optimized approach using LCM

class Solution {
public:
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    int lcm(int a, int b) {
        return a / gcd(a, b) * b; // prevent overflow
    }

    string fractionAddition(int num1, int den1, int num2, int den2) {
        // Step 1: find least common denominator
        int commonDen = lcm(den1, den2);

        // Step 2: adjust numerators
        int num = num1 * (commonDen / den1) + num2 * (commonDen / den2);
        int den = commonDen;

        // Step 3: reduce fraction
        int g = gcd(abs(num), abs(den));
        num /= g;
        den /= g;

        return to_string(num) + "/" + to_string(den);
    }
};
```

### 🥇 Approach 2: Optimal Solution ⭐ (Direct Formula)

#### 📝 Intuition

> - Instead of LCM or full expansion, directly compute:
>   - (num1 _ den2 + num2 _ den1) / (den1 \* den2)
> - Reduce immediately by GCD.
> - Since den1, den2 ≤ 1000, no overflow issues in int.
> - Clean and elegant.

#### 🔍 Algorithm

```pseudo
function optimal(num1, den1, num2, den2):
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    g = gcd(num, den)
    return (num/g, den/g)
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution

class Solution {
public:
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    string fractionAddition(int num1, int den1, int num2, int den2) {
        // Step 1: compute numerator and denominator directly
        int num = num1 * den2 + num2 * den1;
        int den = den1 * den2;

        // Step 2: reduce using gcd
        int g = gcd(abs(num), abs(den));
        num /= g;
        den /= g;

        // Step 3: return string
        return to_string(num) + "/" + to_string(den);
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                                | Cons                    |
| ------------- | --------------- | ---------------- | ----------------------------------- | ----------------------- |
| 🥈 Optimized  | O(log(min))     | O(1)             | Uses LCM to avoid huge denominators | Slightly more complex   |
| 🥇 Optimal ⭐ | O(log(min))     | O(1)             | Clean formula, elegant, efficient   | None (best choice here) |

---

<div align="center">

**🎯 Problem 700259 Completed!**

_Happy Coding! 🚀_

</div>
