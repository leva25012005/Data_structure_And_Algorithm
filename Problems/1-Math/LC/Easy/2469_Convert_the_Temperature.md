<div align="center">

# 🧠 [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/)

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem%202469-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/convert-the-temperature/)

</div>

---

## 📋 Problem Overview

| Property            | Value                                                                      |
| ------------------- | -------------------------------------------------------------------------- |
| **Difficulty**      | 🟢 **Easy**                                                                |
| **Acceptance Rate** | `90.2%`                                                                    |
| **Problem Link**    | [Open in LeetCode](https://leetcode.com/problems/convert-the-temperature/) |
| **Tags**            | ![Math](https://img.shields.io/badge/-Math-blue?style=flat-square)         |

## Description

<!-- description:start -->

<p>You are given a non-negative floating point number rounded to two decimal places <code>celsius</code>, that denotes the <strong>temperature in Celsius</strong>.</p>

<p>You should convert Celsius into <strong>Kelvin</strong> and <strong>Fahrenheit</strong> and return it as an array <code>ans = [kelvin, fahrenheit]</code>.</p>

<p>Return <em>the array <code>ans</code>. </em>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note that:</strong></p>

<ul>
	<li><code>Kelvin = Celsius + 273.15</code></li>
	<li><code>Fahrenheit = Celsius * 1.80 + 32.00</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> celsius = 36.50
<strong>Output:</strong> [309.65000,97.70000]
<strong>Explanation:</strong> Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> celsius = 122.11
<strong>Output:</strong> [395.26000,251.79800]
<strong>Explanation:</strong> Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= celsius &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## ⏰ Progress Tracking

| Status           | Date         | Notes                                    |
| ---------------- | ------------ | ---------------------------------------- |
| 🎯 **Attempted** | `16-09-2025` | First attempt, understanding the problem |
| ✅ **Solved**    | `16-09-2025` | Successfully implemented solution        |
| 🔄 **Review 1**  | `DD-MM-YYYY` | First review, optimization               |
| 🔄 **Review 2**  | `DD-MM-YYYY` | Second review, different approaches      |
| 🔄 **Review 3**  | `DD-MM-YYYY` | Final review, mastery                    |

## 🔗 Related Problems

| Problem                                                                         | Difficulty  | Relationship  |
| ------------------------------------------------------------------------------- | ----------- | ------------- |
| [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | 🟢 **Easy** | Similar logic |

---

## 💡 Solutions

### 🥇 Approach 1: Optimal Solution ⭐ (Formula)

#### 📝 Intuition

> - The problem gives the formulas directly:
>   - Kelvin = Celsius + 273.15
>   - Fahrenheit = Celsius \* 1.80 + 32.00
>   - Simply apply these formulas and return results in an array.
> - Straightforward but repeats computation directly inside the function.

#### 🔍 Algorithm

```pseudo
function convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
```

#### 💻 Implementation

```cpp
// Most optimal and elegant solution with directly apply formulas

class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = celsius * 1.80 + 32.00;
        return {kelvin, fahrenheit};
    }
};
```

## 📊 Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Pros                         | Cons |
| ------------- | --------------- | ---------------- | ---------------------------- | ---- |
| 🥇 Optimal ⭐ | O(1)            | O(1)             | Very simple, direct formulas | None |

---

<div align="center">

**🎯 Problem 2469 Completed!**

_Happy Coding! 🚀_

</div>
