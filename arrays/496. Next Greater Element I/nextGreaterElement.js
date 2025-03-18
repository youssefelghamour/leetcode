/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let ans = [];

    for (let n of nums1) {
        let found = false;

        for (let i = 0; i < nums2.length; i++) {
            if (n === nums2[i]) {
                for (let j = i + 1; j < nums2.length; j++) {
                    if (nums2[j] > n) {
                        ans.push(nums2[j]);
                        found = true;
                        break;
                    }
                }
            }
        }

        if (!found) {
            ans.push(-1);
        }
    }
    
    return ans;
};