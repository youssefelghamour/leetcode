# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
            
        stack = []
        result = 0

        # Each element in the stack is a list containing the node,
        # and sum of nodes leading to it from the root (path sum)
        stack.append([root, root.val])

        while stack:
            element = stack.pop()

            current = element[0]  # node
            path_sum = element[1]  # its path sum

            # If the current node is a leaf, and tha sum from root == target
            if not current.right and not current.left and path_sum == targetSum:
                return True

            if current.right:
                stack.append([current.right, path_sum + current.right.val])
            if current.left:
                stack.append([current.left, path_sum + current.left.val])
        
        return False