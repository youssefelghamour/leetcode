/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let d = {};
    
    for (let n of nums) {
        if (!d[n]) {
            d[n] = 0;
        }
        d[n]++;
    }
    
    // Sort keys by frequency in descending order
    let keys = Object.keys(d).sort((a, b) => d[b] - d[a]);
    
    // Return the top k frequent elements
    return keys.slice(0, k).map(key => parseInt(key));
};