/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let index = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            temp = nums[index];
            nums[index] = nums[i];
            nums[i] = temp;
            index++;
        }
    }
};