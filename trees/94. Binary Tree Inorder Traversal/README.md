# 94. Binary Tree Inorder Traversal

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

## Example 1:

- **Input:** root = [1,null,2,3]
- **Output:** [1,3,2]
- **Explanation:**
    
![ex1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

## Example 2:

- **Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]
- **Output:** [4,2,6,5,7,1,3,9,8]
- **Explanation:**

![ex2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

## Example 3:

- **Input:** root = []
- **Output:** []

## Example 4:

- **Input:** root = [1]
- **Output:** [1]

## Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100