/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    let start = 0;
    let end = 0;
    let charLastOccurrence = {};
    let result = [];

    for (let i = 0; i < s.length; i++) charLastOccurrence[s[i]] = i;

    for (let i = 0; i < s.length; i++) {
        end = Math.max(end, charLastOccurrence[s[i]]);

        if (i === end) {
            result.push(end + 1 - start);
            start = end + 1;
        }
    }

    return result;
};