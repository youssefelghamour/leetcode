# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]

        If the node is a leaf we just remove it
        If it has one child, connect the parent directly to the child
        If it has two children, we connect parent to the node with the smallest value
            on the right subtree to maintain the BST
        """
        def replace(parent, current, new_node):
            """
            Deletes the current node by replacing it with the new_node
            by connecting parent to new_node
            """
            # If current has no parent then it's the root node just return the new node as root
            if not parent:
                return new_node
            
            # If current is a left or right child
            if parent.left is current:
                parent.left = new_node
            else:
                parent.right = new_node
            
            return root


        parent = None
        current = root

        # Find thenode to delete
        while current:
            if current.val == key:
                break
            elif key > current.val:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        
        if not current:
            return root
        
        # Has only one child or leaf
        if not current.left:
            return replace(parent, current, current.right)
        if not current.right:
            return replace(parent, current, current.left)
        
        # Has two children
        # Or root as leaf

        # Find the min of the right subtree
        temp = current.right
        temp_parent = current
        while temp.left:
            temp_parent = temp
            temp = temp.left
        
        # Replace the deleted current node with the min node of right subtree
        if temp_parent != current:
            temp_parent.left = temp.right  # In case left most leaf had a right child
        else:
            # Right child has no left subtree
            current.right = temp.right
        current.val = temp.val
        
        return root