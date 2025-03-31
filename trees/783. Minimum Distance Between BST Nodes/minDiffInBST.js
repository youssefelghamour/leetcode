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
var minDiffInBST = function(root) {
    let current = root;
    let stack = [];
    let min = Infinity;
    let prev = null;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }

        current = stack.pop();

        if (prev) {
            if (current.val - prev.val < min) {
                min = current.val - prev.val;
            }
        }

        prev = current;
        current = current.right;
    }

    return min;
};