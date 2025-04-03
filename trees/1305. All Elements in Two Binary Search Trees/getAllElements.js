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
var inroderList = function(root) {
    let curr = root;
    let stack = [];
    let inorder = [];

    while (curr || stack.length > 0) {
        while (curr) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        inorder.push(curr.val);
        curr = curr.right;
    }

    return inorder;
}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function(root1, root2) {
    let result = [];

    let inorder1 = inroderList(root1);
    let inorder2 = inroderList(root2);

    // Merge the two inorder lists
    let i = 0, j = 0;
    while (i < inorder1.length && j < inorder2.length) {
        if (inorder1[i] < inorder2[j]) {
            result.push(inorder1[i]);
            i++;
        } else {
            result.push(inorder2[j]);
            j++;
        }
    }

    // Add the remaining elements
    while (i < inorder1.length) {
        result.push(inorder1[i]);
        i++;
    }
    while (j < inorder2.length) {
        result.push(inorder2[j]);
        j++;
    }

    return result;
};