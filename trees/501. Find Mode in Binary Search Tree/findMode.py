# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        Finds the modes using Inorder traversal benefiting from the structure of the BST:
        since duplicate values appear consecutively, using Inorder, we can track the current value,
        its frequency, and keep track of the maximum frequency

        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = []
        current = root
        prev = None
        count = 0  # Frequency of the current node value
        max_count = 0  # Frequency of the current Mode
        result = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()

            # Count occurrences
            if prev and prev.val == current.val:
                count += 1
            else:
                count = 1  # Reset for new value

            # Store mode(s)
            if count > max_count:  # Found a new Mode
                max_count = count
                result = [current.val]  # Clear result and update it with the new Mode
            elif count == max_count:  # Found a different Mode with the same occurence
                result.append(current.val)
            
            prev = current
            current = current.right
        
        return result