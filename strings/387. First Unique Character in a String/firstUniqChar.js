/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let count = {};

    for (let c of s) {
        if (c in count) {
            count[c]++;
        } else {
            count[c] = 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        if (count[s[i]] === 1) {
            return i;
        }
    }

    return -1;
};