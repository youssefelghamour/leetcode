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
 * @return {number[]}
 */
var findMode = function(root) {
    let frequency = {};
    let stack = [];
    let result = [];
    let current = root;
    let maxFreq = 0;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }

        current = stack.pop();

        if (current.val in frequency) frequency[current.val] += 1;
        else frequency[current.val] = 1;

        current = current.right;
    }

    for (let key in frequency) {
        if (frequency[key] > maxFreq) {
            maxFreq = frequency[key];
            result = [Number(key)];  // Keys in js obj are string
        } else if (frequency[key] === maxFreq) {
            result.push(Number(key));
        }
    }

    return result;
};