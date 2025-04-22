# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        """
        # pre-order traversal
        stack = []
        result = []

        if not root:
            return []

        stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        print(result)
        """
        stack = []
        prev = None

        if not root:
            return []

        stack.append(root)

        while stack:
            node = stack.pop()

            if prev:
                prev.left = None
                prev.right = node
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            prev = node
        
        return root