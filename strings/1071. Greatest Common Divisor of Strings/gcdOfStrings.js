/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    let minLen = Math.min(str1.length, str2.length);

    for (let i = minLen; i > 0; i--) {
        if (str1.length % i === 0 && str2.length % i === 0) {
            let substring = str1.slice(0, i);

            let num1 = str1.length / i;
            let num2 = str2.length / i;

            if (substring.repeat(num1) === str1 && substring.repeat(num2) === str2) {
                return substring;
            }
        }
    }

    return "";
};