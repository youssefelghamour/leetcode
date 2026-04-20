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
class CountGoodNodes {
    public int goodNodes(TreeNode root) {
        // The main stack for nodes
        Stack<TreeNode> nodeStack = new Stack<>();
        // Stores max values in the path leading to each node in nodeStack
        // For every node we push in nodeStack, we push the max of the path leading to it
        Stack<Integer> maxStack = new Stack<>();
        TreeNode current = root;
        int max = root.val;
        int total = 0;

        nodeStack.push(current);
        maxStack.push(current.val);

        while (!nodeStack.isEmpty()) {
            current = nodeStack.pop();
            max = maxStack.pop();

            if (current.val >= max) {
                max = current.val;
                total++;
            }

            if (current.right != null) {
                nodeStack.push(current.right);
                maxStack.push(max);
            }
            if (current.left != null) {
                nodeStack.push(current.left);
                maxStack.push(max);
            }
        }

        return total;
    }
}