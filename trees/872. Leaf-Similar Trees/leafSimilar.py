# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def getLeaves(root):
            leaves = []
            stack = []
            current = root

            # Inorder
            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
                
                current = stack.pop()

                if not current.left and not current.right:
                    leaves.append(current.val)

                current = current.right

            return leaves

        return getLeaves(root1) == getLeaves(root2)