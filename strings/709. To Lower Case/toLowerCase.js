/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    let result = ""
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (c >= "A" && c <= "Z") {
            c = String.fromCharCode(c.charCodeAt(0) + 32);
        }
        result += c;
    }
    return result;
};