/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    // Turn into a set then back to list to remove duplicates
    nums = [...new Set(nums)]

    if (nums.length < 3) {
        return Math.max(...nums);
    }

    nums.sort((a, b) => a - b); // Ascending order
    return nums[nums.length - 3];
};