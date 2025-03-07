/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    };
    
    let sum = 0;
    let i = 0;
    
    while (i < s.length) {
        if (i + 1 < s.length && values[s[i] + s[i + 1]]) {  // IV, IX, XL, XC, CD, CM
            sum += values[s[i] + s[i + 1]];
            i += 2;
        } else {
            sum += values[s[i]];
            i += 1;
        }
    }
    
    return sum;
};