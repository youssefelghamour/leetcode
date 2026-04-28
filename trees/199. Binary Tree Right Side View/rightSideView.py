# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        Doing BFS level order traversal:
        Adding nodes to the current_level stack from left to right
        the right most element (last in the stack) is the node we see on that level
        """
        if not root:
            return []
            
        current_level = [root]
        result = []

        while current_level:
            next_level = []

            result.append(current_level[-1].val)

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            current_level = next_level
        
        return result