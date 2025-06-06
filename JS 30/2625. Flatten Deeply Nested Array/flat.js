/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n === 0) return arr;

    let result = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            // Spread the result array returned by the recursive call
            result.push(...flat(arr[i], n-1));
        } else {
            result.push(arr[i]);
        }
    }

    return result;
};