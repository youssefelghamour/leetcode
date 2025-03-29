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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    let result = 0;
    let currentLevel = [root];

    while (currentLevel.length > 0) {
        let nextLevel = [];

        for (let node of currentLevel) {
            if (low <= node.val && node.val <= high) result += node.val;
            if (node.left && node.val > low) nextLevel.push(node.left);
            if (node.right && node.val < high) nextLevel.push(node.right);
        }

        currentLevel = nextLevel;
    }

    return result;
};