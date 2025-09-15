/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    let result = 0;
    brokenLetters = new Set(brokenLetters);

    for (let word of text.split(' ')) {
        let correct = true;
        for (let c of word) {
            if (brokenLetters.has(c)) {
                correct = false;
                break;
            }
        }
        if (correct) result++;
    }

    return result;
};