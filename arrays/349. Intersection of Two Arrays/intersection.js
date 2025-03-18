/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let result = [];
    nums1 = [...new Set(nums1)];
    nums2 = [...new Set(nums2)];

    for (let n of nums1) {
        if (nums2.includes(n)) {
            result.push(n);
        }
    }

    return result;
};