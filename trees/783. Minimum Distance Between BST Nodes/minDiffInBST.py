# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        Finds the minimum distance in the BST using inorder traversal (since it gives the values in sorted order),
        by keeping track of the minimum distance while traversing the BST

        :type root: Optional[TreeNode]
        :rtype: int
        """
        current = root
        stack = []
        minimum = float('inf')
        prev = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            if prev:
                if current.val - prev.val < minimum:
                    minimum = current.val - prev.val
            
            prev = current
            current = current.right
        
        return minimum