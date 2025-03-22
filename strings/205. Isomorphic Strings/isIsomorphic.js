/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let char_map = {};

    for (let i = 0; i < s.length; i++) {
        // If key doesn't exist in the obj: !Object.keys(char_map).includes(s[i])
        if (!(s[i] in char_map)) {
            if (Object.values(char_map).includes(t[i])) {
                return false;
            }
            char_map[s[i]] = t[i];
        } else {
            if (t[i] !== char_map[s[i]]) {
                return false;
            }
        }
    }

    return true;
};