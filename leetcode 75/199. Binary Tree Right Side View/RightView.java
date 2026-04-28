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
class RightView {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new ArrayList<>();

        List<TreeNode> currentLevel = new ArrayList<>();
        List<Integer> result = new ArrayList<>();

        currentLevel.add(root);

        while (!currentLevel.isEmpty()) {
            List<TreeNode> nextLevel = new ArrayList<>();

            result.add(currentLevel.get(currentLevel.size() - 1).val);

            for (TreeNode node : currentLevel) {
                if (node.left != null) nextLevel.add(node.left);
                if (node.right != null) nextLevel.add(node.right);
            }

            currentLevel = nextLevel;
        }

        return result;
    }
}