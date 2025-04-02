# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # The root is the first element in the preorder list
        root = TreeNode(preorder[0])
        # Use stack to keep track of the ancestors of each node
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                # If the current value is less than the stack's top, it goes to the left
                stack[-1].left = node
                # Push the node onto the stack because it could have further children
                stack.append(node)
            else:
                # If the value is greater than the stack's top, it goes to the right
                while stack and value > stack[-1].val:
                    # Pop nodes from the stack until we find a node that the current value can be its right child
                    parent = stack.pop()
                # Now, the current val should be greater than the parent val, it will be the parent's right child
                parent.right = node
                # Push the node to the stack because it could have further children
                stack.append(node)

        return root