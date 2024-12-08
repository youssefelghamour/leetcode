/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let d = {};

    for (let num of nums) {
        if (num in d) {
            delete d[num];
        } else {
            d[num] = 1;
        }
    }

    return Number(Object.keys(d)[0]);
};