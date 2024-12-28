# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBST(self, node, left, right) -> bool: 
        if not node:
            return True
        
        if not (node.val > left and node.val < right):
            return False
        
        return self.checkBST(node.left, left, node.val) and self.checkBST(node.right, node.val, right)
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float(-inf), float(inf)) 