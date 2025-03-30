# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool

        ex: [10,5,15,3,7,null,null], k = 12, true when curr1 = 5 and curr2 = 7
                  10
                 /  \
                5   15
               / \   
              3   7  
            Iteration 1: current1 = 3, current2 = 15, stack1 = [10, 5, 3], stack2 = [10, 15]
            Iteration 2: current1 = 3, current2 = 10, stack1 = [10, 5, 3], stack2 = [10]
            Iteration 3: current1 = 3, current2 = 7,  stack1 = [10, 5, 3], stack2 = [5, 7]
            Iteration 4: current1 = 5, current2 = 7,  stack1 = [10, 5],    stack2 = [5, 7]
        """
        if not root:
            return False
        
        current1 = root  # Leftmost node
        current2 = root  # Rightmost node
        stack1 = []  # Inorder stack (from smallest value)
        stack2 = []  # Reverse inorder stack (from highest value)

        # Initialize the leftmost node
        while current1:
            stack1.append(current1)
            current1 = current1.left

        # Initialize the rightmost node
        while current2:
            stack2.append(current2)
            current2 = current2.right

        while stack1 and stack2:  # 
            # We only pop to go forwards (inorder) or backwards (reverse inorder)
            current1 = stack1[-1]
            current2 = stack2[-1]

            # If we meet at the same node, we have checked all possilbe pairs, break & return false
            if current1 == current2:
                break

            if current1.val + current2.val < k:
                # If the sum is smaller, move the left pointer (smaller value): inorder: left -> parent -> right
                # Pop from stack1 so we can move forward in inorder traversal
                current1 = stack1.pop()
                if current1.right:
                    # The current node is the parent (already processed the left then we popped form the stack1)
                    # So we need to process the right side that has the next bigger value
                    current1 = current1.right
                    # Inorder on the right subtree to get values from smaller to greater
                    while current1:
                        stack1.append(current1)
                        current1 = current1.left
            elif current1.val + current2.val > k:
                # If the sum is greater, move the right pointer (greater value): reverse inorder: right -> parent -> left
                # Pop from stack1 so we can move backwards in reverse inorder traversal
                current2 = stack2.pop()
                if current2.left:
                    # The current node is the parent (already processed the right then we popped form the stack2)
                    # So we need to process the left side that has the next smaller value
                    current2 = current2.left
                    # Reverse inorder on the left subtree to get values from greater to smaller
                    while current2:
                        stack2.append(current2)
                        current2 = current2.right
            else:
                return True
        
        return False