/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumPairRemoval = function(nums) {
    let count = 0;

    while (!isSorted(nums)) {
        let minSum = Infinity;
        let j = 0;

        for (let i = 0; i < nums.length - 1; i++) {
            if (nums[i] + nums[i + 1] < minSum) {
                minSum = nums[i] + nums[i + 1];
                j = i;
            }
        }

        nums = [...nums.slice(0, j), minSum, ...nums.slice(j + 2)];
        count++;
    }

    return count;
};

var isSorted = (arr) => {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) return false;
    }
    return true;
}