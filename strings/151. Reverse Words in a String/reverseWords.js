/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // split on any whitespace and filter out empty strings
    let words = s.trim().split(/\s+/);
    let l = 0, r = words.length - 1;

    while (l < r) {
        [words[l], words[r]] = [words[r], words[l]]; // swap
        l++;
        r--;
    }

    return words.join(' ');
};