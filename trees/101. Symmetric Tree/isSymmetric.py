# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compareChildren(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        if left_root.val != right_root.val:
            return False
        
        return self.compareChildren(left_root.left, right_root.right) and self.compareChildren(left_root.right, right_root.left)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compareChildren(root.left, root.right)