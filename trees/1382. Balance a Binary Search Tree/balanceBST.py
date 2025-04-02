# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def arrToBST(self, arr):
        """
        Constructs a BST from an array representing the Inorder traversal
        Splitting the arr in half ensure the left and right subtrees have same number of nodes => balanced
            - The left half contains smaller values -> becomes the left subtree
            - The right half contains larger values -> becomes the right subtree

        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not arr:
            return None

        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        node.left = self.arrToBST(arr[:mid])
        node.right = self.arrToBST(arr[mid + 1:])

        return node


    def balanceBST(self, root):
        """
        Balances a BST

        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        current = root
        stack = []
        # Array representaion of the Inorder traversal of the BST; contains node values
        inorder_arr = []

        # Inorder traversal
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            inorder_arr.append(current.val)
            current = current.right
        
        root = self.arrToBST(inorder_arr)

        return root