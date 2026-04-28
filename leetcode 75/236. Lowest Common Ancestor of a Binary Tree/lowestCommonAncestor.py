# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        - Current node is LCA if p and q are split between left and right subtrees (any depth)
        - p is LCA if q is descendant of p and vice versa

        BFS level order Traversal
        1. Traverse the tree and create a path from p or q back to root
        2. Make a dict with the node as key and the parent of the node as value
        3. After the BFS loop, starting from p and q, go up the tree using the dict
        4. If a common node is found in both paths that's the LCA
        """
        current_level = [root]
        parent = {}
        p_node = None
        q_node = None
        p_path = set()

        parent[root] = None

        while current_level:
            next_level = []

            for node in current_level:
                # Remember the nodes so we can use them traverse the path up to root
                if node == p:
                    p_node = node
                elif node == q:
                    q_node = node
                
                if node.left:
                    next_level.append(node.left)
                    parent[node.left] = node
                if node.right:
                    next_level.append(node.right)
                    parent[node.right] = node
        
            # Stop early if both are found
            if p_node and q_node:
                break
            
            current_level = next_level
        
        
        while p_node:
            p_path.add(p_node)
            p_node = parent[p_node]
        
        while q_node:
            if q_node in p_path:
                return q_node
            # Go up the tree q_node -> root until an intersection of both paths is found
            q_node = parent[q_node]