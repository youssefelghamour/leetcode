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
class NodeDelete {
    /**
     * Deletes the current node by replacing it with the new_node
     * by connecting parent to new_node
     */
    public TreeNode replace(TreeNode root, TreeNode parent, TreeNode current, TreeNode newNode) {
        // If current has no parent then it's the root node just return the new node as root
        if (parent == null) {
            return newNode;
        }

        // If current is a left or right child
        if (parent.left == current) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
        }

        return root;
    }


    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode parent = null;
        TreeNode current = root;

        // Find the node to delete
        while (current != null) {
            if (current.val == key) {
                break;
            } else if (key > current.val) {
                parent = current;
                current = current.right;
            } else {
                parent = current;
                current = current.left;
            }
        }

        if (current == null) {
            return root;
        }

        // Has only one child or leaf
        if (current.left == null) {
            return replace(root, parent, current, current.right);
        }
        if (current.right == null) {
            return replace(root, parent, current, current.left);
        }

        // Has two children
        // Or root as leaf

        // Find the min of the right subtree
        TreeNode temp = current.right;
        TreeNode tempParent = current;
        while (temp.left != null) {
            tempParent = temp;
            temp = temp.left;
        }

        // Replace the deleted current node with the min node of right subtree
        if (tempParent != current) {
            tempParent.left = temp.right;  // In case left most leaf had a right child
        } else {
            // Right child has no left subtree
            current.right = temp.right;
        }
        current.val = temp.val;
        
        return root;
    }
}