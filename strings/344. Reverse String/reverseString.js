/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    n = s.length;
    for (let i = 0; i < n / 2; i++) {
        temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp ;
    }        
};