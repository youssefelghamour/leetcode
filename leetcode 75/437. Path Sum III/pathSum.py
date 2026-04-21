# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int


        Process:

        Conventionel preorder traversal will only check sums to a node starting from the root
        To solve this problem and check all paths leading to this node we make a dict to store path sums
        Sums = Key: node, value: a list of all possible sub-path sums ending at that node
        If path with preorder traversal is root -> grandparent -> parent -> node
        Then sums[node] = [sum_from_root, sum_from_grandparent, sum_from_parent, node.val]
        To keep track of all these sums while doing preorder (parent > left > right), when reaching a node
        sums[node] = we take the parent's sums[parent] list and add node.val to each item and node.val as a standalone item
        If any of the sums in sums[node] == targetSum then we increment result
        """
        stack = []
        sums = {}
        result = 0
        current = root

        if not root: return 0

        stack.append(current)
        sums[current] = [current.val]

        while stack:
            current = stack.pop()
            current_sums = sums[current]

            for s in current_sums:
                result += 1 if s == targetSum else 0

            if current.right:
                stack.append(current.right)
                sums[current.right] = [s + current.right.val for s in sums[current]] + [current.right.val]
            if current.left:
                stack.append(current.left)
                sums[current.left] = [s + current.left.val for s in sums[current]] + [current.left.val]
        
        return result