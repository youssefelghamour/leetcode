/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    let result = [];
    const firstRow = "qwertyuiop";
    const secondRow = "asdfghjkl";
    const thirdRow = "zxcvbnm";

    for (let word of words) {
        // Turn it into a list so every can be used
        let lowercaseWord = word.toLowerCase().split("")
        if (lowercaseWord.every(char => firstRow.includes(char)) ||
                lowercaseWord.every(char => secondRow.includes(char)) ||
                lowercaseWord.every(char => thirdRow.includes(char)) ) {
            result.push(word);
        }
    }
    
    return result;
};