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
class LeavesSimilar {
    public List<Integer> getLeaves(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> leaves = new ArrayList<>();
        TreeNode current = root;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.add(current);
                current = current.left;
            }

            current = stack.pop();
            
            if (current.left == null && current.right == null) {
                leaves.add(current.val);
            }

            current = current.right;
        }

        return leaves;
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        return getLeaves(root1).equals(getLeaves(root2));
    }
}