# 2626. Array Reduce Transformation

Given an integer array `nums`, a reducer function `fn`, and an initial value `init`, return the final result obtained by executing the `fn` function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations:  
`val = fn(init, nums[0])`,  
`val = fn(val, nums[1])`,  
`val = fn(val, nums[2])`,  
... until every element in the array has been processed. The final value of `val` is then returned.

If the array is empty, the function should return `init`.

**Do not use the built-in `Array.prototype.reduce` method.**

## Example 1:

- **Input:**  
  `nums = [1, 2, 3, 4]`  
  `fn = function sum(accum, curr) { return accum + curr; }`  
  `init = 0`
- **Output:** `10`
- **Explanation:**  
  Start with `init = 0`  
  → `0 + 1 = 1`  
  → `1 + 2 = 3`  
  → `3 + 3 = 6`  
  → `6 + 4 = 10`  
  Final result is `10`.

## Example 2:

- **Input:**  
  `nums = [1, 2, 3, 4]`  
  `fn = function sum(accum, curr) { return accum + curr * curr; }`  
  `init = 100`
- **Output:** `130`
- **Explanation:**  
  Start with `init = 100`  
  → `100 + 1*1 = 101`  
  → `101 + 2*2 = 105`  
  → `105 + 3*3 = 114`  
  → `114 + 4*4 = 130`  
  Final result is `130`.

## Example 3:

- **Input:**  
  `nums = []`  
  `fn = function sum(accum, curr) { return 0; }`  
  `init = 25`
- **Output:** `25`
- **Explanation:**  
  Array is empty, so return `init`.

## Constraints:

- `0 <= nums.length <= 1000`  
- `0 <= nums[i] <= 1000`  
- `0 <= init <= 1000`
