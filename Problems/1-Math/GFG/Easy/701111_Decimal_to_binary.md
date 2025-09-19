<div align="center">

# 🧠 [Decimal to binary](https://www.geeksforgeeks.org/problems/decimal-to-binary-1587115620/1)

[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/problems/decimal-to-binary-1587115620/1)

</div>

---

## 📋 Problem Overview

| Property         | Value                                                                                                                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem ID**   | `701111`                                                                                                                                                                                                                                                                 |
| **Difficulty**   | 🟢 **Easy**                                                                                                                                                                                                                                                              |
| **Accuracy**     | `55.75%`                                                                                                                                                                                                                                                                 |
| **Problem Link** | [Open in GeeksforGeeks](https://www.geeksforgeeks.org/problems/decimal-to-binary-1587115620/1)                                                                                                                                                                           |
| **Topic Tags**   | ![Practice-Problems](https://img.shields.io/badge/-Practice%20Problems-blue?style=flat-square) ![Bit Magic](https://img.shields.io/badge/-Bit%20Magic-blue?style=flat-square) ![Data Structures](https://img.shields.io/badge/-Data%20Structures-blue?style=flat-square) |
| **Company Tags** | ![Adobe](https://img.shields.io/badge/-Adobe-orange?style=flat-square)                                                                                                                                                                                                   |

## Description

<!-- description:start -->

<p>Given a decimal number <code>n</code>, return its binary equivalent as a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> "1100"
<strong>Explanation:</strong> The binary representation of 12 is "1100", since 12 = 1×2<sup>3</sup> + 1×2<sup>2</sup> + 0×2<sup>1</sup> + 0×2<sup>0</sup>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 33
<strong>Output:</strong> "100001"
<strong>Explanation:</strong> The binary representation of 33 is "100001", since 33 = 1×2<sup>5</sup> + 0×2<sup>4</sup> + 0×2<sup>3</sup> + 0×2<sup>2</sup> + 0×2<sup>1</sup> + 1×2<sup>0</sup>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Expected Time Complexity:</strong> O(log(n))<br>
<strong>Expected Auxiliary Space:</strong> O(log(n))</p>

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

1. [GeeksforGeeks Article 1](https://www.geeksforgeeks.org/program-decimal-binary-conversion/)

---

## 💡 Solutions

### 🥉 Approach 1: Brute Force (Using Division and Stack)

#### 📝 Intuition

> - Continuously divide n by 2 and store the remainder.
> - Push remainders into a stack to reverse the order since the least significant bit comes first.
> - Pop from stack to form the binary string.

#### 🔍 Algorithm

```pseudo
function decimalToBinary(n):
    stack = empty
    while n > 0:
        push n % 2 to stack
        n = n // 2
    result = ""
    while stack not empty:
        result += pop from stack
    return result
```

#### 💻 Implementation

```cpp
// Brute force using stack

class Solution {
public:
    string decimalToBinary(int n) {
        if (n == 0) return "0";

        stack<int> st;
        while (n > 0) {
            st.push(n % 2); // Get remainder
            n /= 2;         // Divide by 2
        }

        string res = "";
        while (!st.empty()) {
            res += to_string(st.top());
            st.pop();
        }
        return res;
    }
};
```

### 🥈 Approach 2: Optimized Solution (Prepend to String)

#### 📝 Intuition

> Instead of using a stack, prepend each binary digit to the result string.
> Avoids extra space for a stack but still reverses the order naturally.

#### 🔍 Algorithm

```pseudo
function decimalToBinary(n):
    if n == 0: return "0"
    result = ""
    while n > 0:
        result = (n % 2) + result
        n = n // 2
    return result
```

#### 💻 Implementation

```cpp
// Optimized approach: prepend to string

class Solution {
public:
    string decimalToBinary(int n) {
        if (n == 0) return "0";

        string res = "";
        while (n > 0) {
            res = to_string(n % 2) + res; // Prepend current bit
            n /= 2;                        // Move to next bit
        }
        return res;
    }
};
```

### 🥇 Approach 3: Optimal Solution ⭐ (Recursive)

#### 📝 Intuition

> - Use recursion to print the most significant bit first.
> - Base case: when n == 0.
> - Recurse with n / 2, then append the last bit n % 2.
> - Elegant and minimal code.

#### 🔍 Algorithm

```pseudo
// Write your pseudocode here
```

#### 💻 Implementation

```cpp
// Recursive approach

class Solution {
public:
    string decimalToBinary(int n) {
        if (n == 0) return "0";

        return helper(n);
    }

private:
    string helper(int n) {
        if (n == 0) return "";
        return helper(n / 2) + to_string(n % 2); // Recurse then append current bit
    }
};
```

## 📊 Comparison of Approaches

| Approach       | Time Complexity | Space Complexity | Pros                       | Cons                            |
| -------------- | --------------- | ---------------- | -------------------------- | ------------------------------- |
| 🥉 Brute Force | O(log n)        | O(log n)         | Clear logic using stack    | Uses extra stack memory         |
| 🥈 Optimized   | O(log n)        | O(log n)         | Avoids explicit stack      | Prepending to string costly     |
| 🥇 Optimal ⭐  | O(log n)        | O(log n)         | Elegant recursive solution | Recursion depth can be O(log n) |

---

<div align="center">

**🎯 Problem 701111 Completed!**

_Happy Coding! 🚀_

</div>
