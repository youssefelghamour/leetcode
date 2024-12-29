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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (!root) {
        return [];
    }

    let result = [];
    let currentLevel = [root];

    while (currentLevel.length > 0) {
        currentLevelValues = [];
        nextLevel = [];

        for (let node of currentLevel) {
            currentLevelValues.push(node.val)

            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }

        result.push(currentLevelValues);
        currentLevel = nextLevel;
    }

    return result;
};