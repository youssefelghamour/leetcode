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
class SumPath {
    public int pathSum(TreeNode root, int targetSum) {
        Stack<TreeNode> stack = new Stack<>();
        // Long because problem input might make the sums exceed int
        Map<TreeNode, List<Long>> sums = new HashMap<>();
        int result = 0;
        TreeNode current = root;

        if (root == null) { return 0; }
        
        stack.push(current);
        
        List<Long> currentSums = new ArrayList<>();
        currentSums.add((long) current.val);
        sums.put(current, currentSums);

        while (!stack.isEmpty()) {
            current = stack.pop();
            currentSums = sums.get(current);

            for (long s: currentSums) {
                result += (s == (long) targetSum) ? 1 : 0;
            }

            if (current.right != null) {
                List<Long> rightSums = new ArrayList<>();

                for (long s: currentSums) {
                    rightSums.add(s + current.right.val);
                }
                rightSums.add((long) current.right.val);

                sums.put(current.right, rightSums);
                stack.push(current.right);
            }
            if (current.left != null) {
                List<Long> leftSums = new ArrayList<>();

                for (long s: currentSums) {
                    leftSums.add(s + current.left.val);
                }
                leftSums.add((long) current.left.val);

                sums.put(current.left, leftSums);
                stack.push(current.left);
            }
        }

        return result;
    }
}