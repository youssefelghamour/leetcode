# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        current = root
        stack = []
        prev = None  # The last node we processed
        head = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            current.left = None

            if not prev:  # This is the first node (left most child, has no left child)
                head = current
            else:
                prev.right = current

            prev = current
            current = current.right
        
        return head