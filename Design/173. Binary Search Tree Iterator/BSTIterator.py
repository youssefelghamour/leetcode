# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    """ Breaks the Inorder Traversal into steps instead of one loop """

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []

        curr = root
        # Push all left children of the root to the stack
        while curr:
            self.stack.append(curr)
            curr = curr.left
        

    def next(self):
        """
        :rtype: int
        """
        # Pop the top node from the stack: the next smallest element in inorder
        curr = self.stack.pop()
        if curr.right:
            # Push all left children of the right child to the stack
            tmp = curr.right
            while tmp:
                self.stack.append(tmp)
                tmp = tmp.left
        return curr.val

        

    def hasNext(self):
        """
        :rtype: bool
        """
        # If stack isn't empty then there are more nodes in the inorder
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()