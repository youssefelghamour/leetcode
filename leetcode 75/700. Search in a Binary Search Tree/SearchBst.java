/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class SearchBst {
    public TreeNode searchBstWithBFS(TreeNode root, int val) {
        if (root == null) return null;

        List<TreeNode> currentLevel = new ArrayList<>();
        currentLevel.add(root);

        while (!currentLevel.isEmpty()) {
            List<TreeNode> nextLevel = new ArrayList<>();

            for (TreeNode node: currentLevel) {
                if (node.val == val) return node;

                if (node.left != null) nextLevel.add(node.left);
                if (node.right != null) nextLevel.add(node.right);
            }

            currentLevel = nextLevel;
        }

        return null;
    }

    public TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val == val) return root;
            else if (val < root.val ) root = root.left;
            else root = root.right;
        }

        return null;
    }
}