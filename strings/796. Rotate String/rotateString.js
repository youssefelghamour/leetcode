/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    for (let i = 0; i < s.length; i++) {
        let firstChar = s[0];
        s = s.slice(1);
        s += firstChar;
        if (s === goal) return true;
    }
    return false;
};