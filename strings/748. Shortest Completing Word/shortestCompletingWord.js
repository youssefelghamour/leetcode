/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function(licensePlate, words) {
    let lpObj = {};
    let wordObj = {};
    completingWords = [];

    licensePlate = licensePlate.toLowerCase().replace(" ", "");
    for (let char of licensePlate) {
        if (!isNaN(char)) {
            licensePlate = licensePlate.replace(char, "")
        }
    }

    for (let char of licensePlate) {
        if (char in lpObj) {
            lpObj[char] += 1;
        } else {
            lpObj[char] = 1;
        }
    }

    for (let word of words) {
        wordObj = {};
        for (let char of word) {
            if (char in wordObj) {
                wordObj[char] += 1;
            } else {
                wordObj[char] = 1;
            }
        }

        if (Object.keys(lpObj).every(key => (wordObj[key] || 0) >= lpObj[key])) {
            completingWords.push(word);
        }
    }

    let shortestWord = completingWords[0];
    for (let word of completingWords) {
        if (word.length < shortestWord.length) {
            shortestWord = word;
        }
    }

    return shortestWord;
};