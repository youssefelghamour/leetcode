/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let vowels = new Set("aeiouAEIOU");
    let l = 0;
    let r = s.length - 1;
    s = [...s];

    while (l < r) {
        if (vowels.has(s[l]) && vowels.has(s[r])) {
            [s[l], s[r]] = [s[r], s[l]];
            l++;
            r--;
        } else {
            if (!vowels.has(s[l])) l++;
            if (!vowels.has(s[r])) r--;
        }
    }

    return s.join('');
};