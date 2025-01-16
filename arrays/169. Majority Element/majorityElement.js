/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let counts = {};
    let half = nums.length / 2;
    
    for (let num of nums) {
        if (num in counts) {
            counts[num] += 1;
        } else {
            counts[num] = 1;
        }
    }
    
    for (let [k, v] of Object.entries(counts)) {
        if (v > half) {
            return Number(k);
        }
    }
};