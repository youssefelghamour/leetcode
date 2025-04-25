# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, node):
        """ This fuction when the tree is balanced keeps going and returns
            the height of the subtree. And if it's unblanaced it returns -1
        """
        if not node:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # If left subtree, right subtree, the current tree are unblanaced 
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            # Return -1, like a boolean indicating that the tree is not balanced
            return -1
        
        return 1 + max(left_height, right_height)


    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if self.height(root) == -1:
            return False
        
        return True