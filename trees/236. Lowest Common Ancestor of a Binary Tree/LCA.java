/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    /**
     * - Current node is LCA if p and q are split between left and right subtrees (any depth)
     * - p is LCA if q is descendant of p and vice versa

     * BFS level order Traversal
     *  1. Traverse the tree and create a path from p or q back to root
     *  2. Make a dict with the node as key and the parent of the node as value
     *  3. After the BFS loop, starting from p and q, go up the tree using the dict
     *  4. If a common node is found in both paths that's the LCA
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> currentLevel = new ArrayList<>();
        Map<TreeNode, TreeNode> parent = new HashMap<>();

        TreeNode pNode = null;
        TreeNode qNode = null;

        Set<TreeNode> pPath = new HashSet<>();

        currentLevel.add(root);
        parent.put(root, null);

        while (!currentLevel.isEmpty()) {
            List<TreeNode> nextLevel = new ArrayList<>();

            for (TreeNode node : currentLevel) {

                if (node == p) pNode = node;
                else if (node == q) qNode = node;

                if (node.left != null) {
                    nextLevel.add(node.left);
                    parent.put(node.left, node);
                }

                if (node.right != null) {
                    nextLevel.add(node.right);
                    parent.put(node.right, node);
                }
            }

            if (pNode != null && qNode != null) break;

            currentLevel = nextLevel;
        }

        while (pNode != null) {
            pPath.add(pNode);
            pNode = parent.get(pNode);
        }

        while (qNode != null) {
            if (pPath.contains(qNode)) return qNode;
            qNode = parent.get(qNode);
        }

        return null;
    }
}