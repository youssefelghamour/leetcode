/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function(nums) {
    let count = 0;
    let totalDistinct = new Set(nums).size;

    for (let i = 0; i < nums.length; i++) {
        let temp = new Set();
        for (let j = i; j < nums.length; j++) {
            temp.add(nums[j]);

            if (temp.size === totalDistinct) count++;
        }
    }

    return count;
};