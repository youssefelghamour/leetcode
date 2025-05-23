# 2625. Flatten Deeply Nested Array

Given a multi-dimensional array `arr` and a depth `n`, return a flattened version of that array.

A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.

A flattened array is a version of that array with some or all of the sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation should only be done if the current depth of nesting is less than `n`. The depth of the elements in the first array are considered to be 0.

Please solve it without the built-in `Array.flat` method.

## Example 1

- **Input:**
  ```json
  arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
  n = 0
  ```

- **Output:** `[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]`

- **Explanation:** With `n=0`, no subarray is flattened as their depth is not less than 0.

## Example 2

- **Input:**
  ```json
  arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
  n = 1
  ```

- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]`

- **Explanation:** Subarrays starting with 4, 7, and 13 are flattened to depth 0, which is less than 1.

## Example 3

- **Input:**
  ```json
  arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],
  n = 2
  ```

- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`

- **Explanation:** All subarrays are flattened as their max depth is 1, which is less than 2.

## Constraints

- `0 <= count of numbers in arr <= 10^5`
- `0 <= count of subarrays in arr <= 10^5`
- `maxDepth <= 1000`
- `-1000 <= each number <= 1000`
- `0 <= n <= 1000`