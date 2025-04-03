# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        Returns a list conatining all the values of both trees in ascending order,
        By doing an Inorder traversal of both the trees at the same time
        
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        curr1 = root1
        curr2 = root2
        stack1 = []
        stack2 = []
        result = []

        while curr1 or curr2 or stack1 or stack2:
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left
            
            while curr2:
                stack2.append(curr2)
                curr2 = curr2.left
            
            if stack1 and not stack2:
                # If the tree1 has more node, but tree2 is done
                curr1 = stack1.pop()
                result.append(curr1.val)
                curr1 = curr1.right
            elif stack2 and not stack1:
                # If the tree2 has more node, but tree1 is done
                curr2 = stack2.pop()
                result.append(curr2.val)
                curr2 = curr2.right
            elif stack1 and stack2:
                # If both trees still have nodes
                if stack1[-1].val < stack2[-1].val:
                    # Continue with the inorder traversal of the first tree
                    # Keep the second tree where it is as we'll need to compare it's curr2 node with the next curr1
                    curr1 = stack1.pop()
                    result.append(curr1.val)
                    curr1 = curr1.right
                else:
                    curr2 = stack2.pop()
                    result.append(curr2.val)
                    curr2 = curr2.right
        
        return result