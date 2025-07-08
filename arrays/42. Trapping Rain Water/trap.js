/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let amount = 0;
    let left = 0;
    let right = height.length - 1;
    let leftMaxHeight = height[left];
    let rightMaxHeight = height[right];

    while (left < right) {
        if (height[left] < height[right]) {
            leftMaxHeight = Math.max(leftMaxHeight, height[left]);
            amount += leftMaxHeight - height[left];
            left++;
        } else {
            rightMaxHeight = Math.max(rightMaxHeight, height[right]);
            amount += rightMaxHeight - height[right];
            right--;
        }
    }

    return amount;
};