/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
var checkBST = (node, left, right) => {
    if (!node) {
        return true;
    }

    if (!(node.val > left && node.val < right)) {
        return false;
    }

    return checkBST(node.left, left, node.val) && checkBST(node.right, node.val, right);
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    return checkBST(root, -Infinity, Infinity)
};