/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    let result;

    if (Array.isArray(obj)) {  // if obj is an array
        result = [];  // return type is an array

        for (let i = 0; i < obj.length; i++) {
            // if the element is a subarray recurse to remove falsy values form it
            if (Array.isArray(obj[i])) result.push(compactObject(obj[i]));
            else if (obj[i] !== null && typeof obj[i] === 'object') {
                // recursive call for nested objects
                result.push(compactObject(obj[i]));
            }
            else { if (obj[i]) result.push(obj[i]); }  // if truthy val add directly
        }
    } else {  // if obj is an object
        result = {};  // return type is an object

        for (let [k, v] of Object.entries(obj)) {
            if (Array.isArray(v)) {
                // call the function on the value to remove falsy values from it
                result[k] = compactObject(v);
            } else if (v !== null && typeof v === 'object') {  // null is typeof 'object' (breaks code on recursino)
                // recursive call for nested objects
                result[k] = compactObject(v);
            } else if (v) {  // add it if it's a truthy value not an array
                result[k] = v;
            }
        }
    }

    return result;
};