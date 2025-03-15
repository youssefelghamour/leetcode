/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim().split(" ");  // trims trailing white space & seperate into a list of words
    return s[s.length - 1].length;
};