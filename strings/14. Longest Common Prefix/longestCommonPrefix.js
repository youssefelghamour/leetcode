/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = "";
    
    shortestString = strs[0]
    for (let s of strs) {
        if (s.length < shortestString.length) {
            shortestString = s;
        }
    }
    
    for (let i = 0; i < shortestString.length; i++) {
        if (strs.every(currentString => currentString[i] === shortestString[i])) {
            prefix += shortestString[i];
        } else {
            break;
        }
    }
    
    return prefix;
};