/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        fn(arr[i], i) ? result.push(arr[i]) : null;
    }
    return result;
};