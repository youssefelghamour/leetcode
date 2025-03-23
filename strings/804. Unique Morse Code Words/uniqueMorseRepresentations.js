/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    let transformations = new Set();
    
    for (let word of words) {
        let transf = "";
        for (let char of word) {
            transf += morse[char.charCodeAt(0) - 97];
        }
        transformations.add(transf);
    }
    
    return transformations.size;
};