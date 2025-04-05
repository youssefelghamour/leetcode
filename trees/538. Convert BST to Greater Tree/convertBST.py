# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        Turns a BST into a Greater Sum Tree where each node’s value is updated to be the sum of its original
        value plus the sum of all node values greater than it => Reverse Inorder Traversal: right -> node -> left
        
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        current = root
        stack = []
        prev = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.right
            
            current = stack.pop()

            if prev:
                current.val += prev.val
            
            prev = current
            current = current.left
        
        return root