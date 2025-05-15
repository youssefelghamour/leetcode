/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let d = {};
    let words = s.split(" ");

    if (pattern.length !== words.length) return false;

    for (let i = 0; i < pattern.length; i++) {
        if (pattern[i] in d) {
            if (d[pattern[i]] !== words[i]) return false;
        } else {
            if (Object.values(d).includes(words[i])) return false;
            d[pattern[i]] = words[i];
        }
    }
    return true;
};