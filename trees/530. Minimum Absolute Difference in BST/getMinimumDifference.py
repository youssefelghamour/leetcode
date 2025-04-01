# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
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

            if prev and current.val - prev.val < minimum:
                minimum = current.val - prev.val
            
            prev = current
            current = current.right
        
        return minimum