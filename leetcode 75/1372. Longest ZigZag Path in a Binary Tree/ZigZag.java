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
class ZigZag {
    public int longestZigZag(TreeNode root) {
        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        TreeNode current = root;
        TreeNode last = null;
        Map<TreeNode, List<Integer>> pathsLength = new HashMap<>();
        int maxLength = 0;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            TreeNode node = stack.peek();
            
            if (node.right != null && last != node.right) {
                current = node.right;
            } else {
                stack.pop();

                int left = node.left != null ? (1 + pathsLength.get(node.left).get(1)) : 0;
                int right = node.right != null ? (1 + pathsLength.get(node.right).get(0)) : 0;

                pathsLength.put(
                    node,
                    new ArrayList<>(
                        Arrays.asList(left, right)
                    )
                );

                maxLength = Math.max(
                    maxLength,
                    Math.max(
                        pathsLength.get(node).get(0),
                        pathsLength.get(node).get(1)
                    )
                );

                last = node;
                current = null;
            }
        }
    
        return maxLength;
    }
}