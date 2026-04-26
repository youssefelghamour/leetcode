# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        Bottom up:
        - Use postorder DFS starting from left most node
        - For each node keep track of the length of the longest zigzag path made from:
            - Going left of the current node
            - Going right of the current node
        - Update while you go up the tree with postorder traversal
        - Parent's length of left path = 1 + the length of the right path of the child (zigzag)
        - Parent's right path = 1 + left path of right child (right -> left on child)
        """
        # Each item in the stack is [node, left_zigzag_length, right_zigzag_length]
        stack = []
        last = None
        current = root
        # Key: node, Value: (length of zigzag path of left subtree, length of zigzag path of right subtree)
        paths_length = {}
        max_length = 0

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            node = stack[-1]

            if node.right and last != node.right:
                current = node.right
            else:
                # If current node's right child doesn't exist or has been processed
                # Its left child is guaranteed to be processed bye the inner while loop
                stack.pop()

                # If we go left first -> next step must go right -> so we use right value from left child
                # Check makes sure we avoid adding +1 to leaves
                left = (1 + paths_length[node.left][1]) if node.left else 0  # left(node) = 1 + right(left_child)
                # If we go right first -> next step must go left -> so we use left value from right child
                right = (1 + paths_length[node.right][0]) if node.right else 0  # right(x) = 1 + left(right_child)

                paths_length[node] = (left, right)

                max_length = max(max_length, paths_length[node][0], paths_length[node][1])

                # Mark it as processed
                last = node
                current = None
                
        return max_length