/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let result = [];
    
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < nums.length; i++) {
        // Skip duplicate for i
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        
        let j = i + 1;
        let k = nums.length - 1;
        
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            
            if (sum === 0) {
                result.push([nums[i], nums[j], nums[k]]);
                j += 1;
                k -= 1;
                
                // Skip duplicate for j
                while (j < k && nums[j] === nums[j - 1]) {
                    j += 1;
                }
                
                // Skip duplicate for k
                while (j < k && nums[k] === nums[k + 1]) {
                    k -= 1;
                }
            } else if (sum < 0) {
                j += 1;
            } else if (sum > 0) {
                k -= 1;
            }
        }
    }
    
    return result;
};