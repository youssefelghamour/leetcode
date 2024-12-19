/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let zeros = 0, ones = 0, twos = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) zeros++;
        else if (nums[i] === 1) ones++;
        else if (nums[i] === 2) twos++;
    }

    for (let i = 0; i < zeros; i++) {
        nums[i] = 0;
    }
    for (let i = zeros; i < zeros + ones; i++) {
        nums[i] = 1;
    }
    for (let i = zeros + ones; i < nums.length; i++) {
        nums[i] = 2;
    }
};