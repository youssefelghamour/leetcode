/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let result = [];
    let visited = {};
    
    for (let i = 0; i < nums.length; i++) {
        if ((target - nums[i]) in visited) {
            result = [i, visited[target - nums[i]]];
        }
        visited[nums[i]] = i;
    }
    
    return result;
};