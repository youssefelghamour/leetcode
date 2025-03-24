/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    for (let char of t) {
        let countS = 0;
        let countT = 0;

        // Count occurrence of char in s
        for (let j = 0; j < s.length; j++) {
            if (s[j] === char) {
                countS++;
            }
        }

        // Count occurrence of char in t
        for (let j = 0; j < t.length; j++) {
            if (t[j] === char) {
                countT++;
            }
        }

        if (countT > countS) {
            return char;
        }
    }
};