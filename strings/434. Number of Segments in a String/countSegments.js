/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    let segments = 0;
    let b = 0;

    if (!s) return 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") {
            if (i > b)  segments++;
            b = i + 1;
        }
    }

    if (b !== s.length) segments++;

    return segments;
};