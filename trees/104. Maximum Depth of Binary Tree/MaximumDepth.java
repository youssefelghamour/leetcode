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
 * 
 * 
 * Instead of the stack of lists, we could use a custom class for the stack items (pairs)
 * 
 * static class Pair {
 *    TreeNode node;
 *    int depth;
 *
 *    Pair(TreeNode node, int depth) {
 *       this.node = node;
 *       this.depth = depth;
 *    }
 * }
 * 
 * And use it as such:
 * Stack<Pair> stack = new Stack<>();
 * stack.push(new Pair(current, 1));
 * 
 * Pair p = stack.pop();
 * TreeNode current = p.node;
 * int currentDepth = p.depth;
 */
class MaximumDepth {
    /**
    * The DFS stack items are a list of the node and its depth
    * A node's depth = depth of its parent + 1
    */
    public int maxDepth(TreeNode root) {
        Stack<List<Object>> stack = new Stack<>();
        TreeNode current = root;
        int maxDepth = 0;

        if (root == null) return 0;

        stack.push(Arrays.asList(current, 1));

        while (!stack.isEmpty()) {
            List<Object> currentItem = stack.pop();
            current = (TreeNode) currentItem.get(0);
            int currentDepth = (int) currentItem.get(1);

            maxDepth = Math.max(maxDepth, currentDepth);

            if (current.right != null) {
                stack.push(Arrays.asList(current.right, currentDepth + 1));
            }
            if (current.left != null) {
                stack.push(Arrays.asList(current.left, currentDepth + 1));
            }
        }

        return maxDepth;
    }
}