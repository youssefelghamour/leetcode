/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let d = {};
    for (let s of strs) {
        let key = s.split('').sort().join('');
        
        if (!d[key]) {
            d[key] = [];
        }
        
        d[key].push(s);
    }
    return Object.values(d);
};