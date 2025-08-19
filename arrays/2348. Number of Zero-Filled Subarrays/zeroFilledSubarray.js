/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let result = 0;
    let streak = 0;

    for (let i in nums) {
        if (nums[i] === 0) {
            streak++;
            result += streak;
        } else {
            streak = 0;
        }
    }

    return result;
};