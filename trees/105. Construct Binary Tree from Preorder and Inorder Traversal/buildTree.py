# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Create the root node from the first element of preorder
        root = TreeNode(preorder[0])
        
        # Find the index of the root in inorder (to divide left and right subtrees)
        # The number of nodes to the left of the root in the inorder list
        mid = inorder.index(preorder[0])
        
        # The left subtree in inorder is everything before the root, and in preorder, it starts after the root
        # preorder[1:mid + 1] gets the 'mid' numbers of nodes from the preorder list (starting from 1 to skip the root)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        
        # The right subtree in inorder is everything after the root, and in preorder, it starts after the left part
        # preorder[mid + 1:] gets the remaining nodes from preorder by skipping the root and the left subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root