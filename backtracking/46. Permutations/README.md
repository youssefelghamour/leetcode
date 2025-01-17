# 46. Permutations

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

## Example 1:

- **Input:** nums = [1,2,3]
- **Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Example 2:

- **Input:** nums = [0,1]
- **Output:** [[0,1],[1,0]]

## Example 3:

- **Input:** nums = [1]
- **Output:** [[1]]

## Constraints:

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.


### Process:

```
            ex: nums =                                  [1,2,3]
                                             ______________|_______
                                            /              |       \
i = 0: adds nums[2], stack =              [1]             [2]     [3]
    call backtrack                       /    \           ...      ...
new loop skips 0 (visited),             /      \
j = 1: adds nums[1], stack =         [1,2]    [1,3]  branch B
    call backtrack                     |        |
new loop skips 0 & 1 (visited),        |        |
k = 2: adds nums[2], stack =        [1,2,3]  [1,3,2] 
    call bakctrack
result.append([1,2,3])
stack.pop(), stack = [1,2], loop ends for k, return to j
stack.pop(), stack = [1],
j = 2: adds nums[2], stack = [1,3], now we're at branch B
when second level j loop is done, stack.pop() and we'll move to i = 1, stack = [2], on a new path
```