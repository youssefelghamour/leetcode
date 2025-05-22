# 2629. Function Composition

Given an array of functions `[f1, f2, f3, ..., fn]`, return a new function `fn` that is the function composition of the array of functions.

The function composition of `[f(x), g(x), h(x)]` is `fn(x) = f(g(h(x)))`.

If the array is empty, return the **identity function**: `f(x) = x`.

Each function in the array accepts one integer as input and returns one integer as output.

## Example 1:

- **Input:**  
  `functions = [x => x + 1, x => x * x, x => 2 * x]`  
  `x = 4`
- **Output:** `65`
- **Explanation:**  
  Evaluating from right to left:  
  → `2 * 4 = 8`  
  → `8 * 8 = 64`  
  → `64 + 1 = 65`  
  Final result is `65`.

## Example 2:

- **Input:**  
  `functions = [x => 10 * x, x => 10 * x, x => 10 * x]`  
  `x = 1`
- **Output:** `1000`
- **Explanation:**  
  → `10 * 1 = 10`  
  → `10 * 10 = 100`  
  → `10 * 100 = 1000`  
  Final result is `1000`.

## Example 3:

- **Input:**  
  `functions = []`  
  `x = 42`
- **Output:** `42`
- **Explanation:**  
  No functions to apply, so return `x` directly.

## Constraints:

- `-1000 <= x <= 1000`  
- `0 <= functions.length <= 1000`  
- All functions accept and return a single integer