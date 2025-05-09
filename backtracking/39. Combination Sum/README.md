# 39. Combination Sum

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The same number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the **frequency** of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.


## Example 1:

- Input: candidates = [2,3,6,7], target = 7
- Output: [[2,2,3],[7]]
- Explanation:
    - 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    - 7 is a candidate, and 7 = 7.
    - These are the only two combinations.

## Example 2:

- Input: candidates = [2,3,5], target = 8
- Output: [[2,2,2,2],[2,3,3],[3,5]]

## Example 3:

- Input: candidates = [2], target = 1
- Output: []
 
## Constraints:

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

## Process:

- If we sort the array and use return when we exceed the target, so we don't explore further combinations (faster beats 81.99%):

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []

        candidates.sort()
        
        def backtrack(start):
            if sum(stack) == target:
                result.append(stack[:])
                return
            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                if sum(stack) > target:
                    stack.pop()
                    return
                backtrack(i)
                stack.pop()
        
        backtrack(0)

        return result
```

```
[2]
└── [2, 2]
    |── [2, 2, 2]
    |   └── [2, 2, 2, 2]
    ├── [2, 2, 3]
    └── [2, 2, 6]
└── [2, 3]
    └── [2, 3, 3]
└── [2, 6]
[3]
└── [3, 3]
    └── [3, 3, 3]
└── [3, 6]
[6]
└── [6, 6]
[7]
```

- if we don't sort the array, and use continue, we'll explore all possible combinations:

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        
        def backtrack(start):
            if sum(stack) == target:
                result.append(stack[:])
                return
            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                if sum(stack) > target:
                    stack.pop()
                    continue
                backtrack(i)
                stack.pop()
        
        backtrack(0)

        return result
```

```
[2]
└── [2, 2]
    ├── [2, 2, 2]
    │   ├── [2, 2, 2, 2]
    │   ├── [2, 2, 2, 3]
    │   ├── [2, 2, 2, 6]
    │   └── [2, 2, 2, 7]
    ├── [2, 2, 3]
    ├── [2, 2, 6]
    └── [2, 2, 7]
└── [2, 3]
    ├── [2, 3, 3]
    ├── [2, 3, 6]
    └── [2, 3, 7]
└── [2, 6]
└── [2, 7]
[3]
└── [3, 3]
    ├── [3, 3, 3]
    ├── [3, 3, 6]
    └── [3, 3, 7]
└── [3, 6]
└── [3, 7]
[6]
├── [6, 6]
└── [6, 7]
[7]
```