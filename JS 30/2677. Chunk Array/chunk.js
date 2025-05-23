/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    /*
    let result = [];
    let chunk = [];

    for (let n of arr) {
        chunk.push(n);

        if (chunk.length === size) {
            result.push(chunk);
            chunk = [];
        }
    }

    if (chunk.length > 0) result.push(chunk);

    return result;
    */
    let result = [];

    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }

    return result;
};
