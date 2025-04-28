/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let s = Infinity;
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            let currSum = nums[i] + nums[left] + nums[right];

            if (Math.abs(currSum - target) < Math.abs(s - target)) {
                s = currSum;
            }

            if (currSum < target) left += 1;
            else right -= 1;
        }
    }

    return s;
};