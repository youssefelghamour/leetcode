/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    // object with keys being the ids, and the values the actual object from the arrays
    // ex: { '1': { id: 1, x: 1 }, '2': { id: 2, x: 9 }, '3': { id: 3, x: 5 } }
    let result = {};

    // add arr1 to result
    for (let item of arr1) {
        // create a new key value pair in result: 'id': {item}
        result[item.id] = { ...item };
    }

    // add arr2 elements to result
    for (let item of arr2) {
        // if the id doesn't exist in result
        if (!result[item.id]) {
            result[item.id] = {};
        }
        for (let key in item) {
            // overrides if key exists
            result[item.id][key] = item[key];
        }
    }

    // sort by ids an turn into a list
    return Object.values(result).sort((a, b) => a.id - b.id);
};