/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if (word.split('').every(char => char >= 'A' && char <= 'Z')) {
        return true;
    }

    if (word.split('').every(char => char >= 'a' && char <= 'z')) {
        return true;
    }

    if (word[0] >= 'A' && word[0] <= 'Z' && word.slice(1).split('').every(char => char >= 'a' && char <= 'z')) {
        return true;
    }

    return false;
};