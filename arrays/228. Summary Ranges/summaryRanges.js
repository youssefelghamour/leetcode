/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    let ranges = [];
    let i = 0;
    
    while (i <nums.length) {
        let a = nums[i];

        while (i < nums.length - 1 & nums[i] + 1 == nums[i + 1]) {
            i++;
        }

        if (a !== nums[i]) {
            ranges.push(String(a) + "->" + String(nums[i]));
        } else {
            ranges.push(String(a));
        }
        
        i++;
    }

    return ranges;
};