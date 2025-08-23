/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (!root) return 0;

    let stack = [];
    let min_path = Infinity;

    // Stack contains the node and the its depth in the tree
    stack.push([root, 1]);

    while (stack.length > 0) {
        let [current, curr_depth] = stack.pop();

        // If the current node is a leaf and it's the new smallest path
        if (!current.right && !current.left && curr_depth <= min_path) {
            min_path = curr_depth;
        }

        if (current.right) stack.push([current.right, curr_depth + 1]);
        if (current.left) stack.push([current.left, curr_depth + 1]);
    }

    return min_path;
};