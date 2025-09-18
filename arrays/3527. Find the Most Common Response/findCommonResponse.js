/**
 * @param {string[][]} responses
 * @return {string}
 */
var findCommonResponse = function(responses) {
    let occurrences = {};
    let maxOccurrence = 0;
    let result = "";

    for (let i = 0; i < responses.length; i++) {
        let dayResponse = new Set(responses[i]);
        for (let resp of dayResponse) {
            occurrences[resp] = (occurrences[resp] || 0) + 1;
        }
    }

    maxOccurrence = Math.max(...Object.values(occurrences));

    temp = Object.keys(occurrences).filter(resp => occurrences[resp] === maxOccurrence);
    temp.sort();

    result = temp[0];

    return result;
};