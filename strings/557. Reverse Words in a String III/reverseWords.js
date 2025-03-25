/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.split(' ');
    
    for (let i = 0; i < s.length; i++) {
        let reversed = "";
        for (let j = s[i].length - 1; j >= 0; j--) {
            reversed += s[i][j];
        }
        s[i] = reversed;
    }

    return s.join(' ');
};