/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    const columns = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
        11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
        20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    };

    let result = "";

    while (columnNumber > 0) {
        let mod = columnNumber % 26;

        // Handle case when mod is 0 -> map to 'Z'
        mod = mod === 0 ? 26 : mod;

        let char = columns[mod];
        columnNumber -= mod;
        columnNumber = Math.floor(columnNumber / 26);

        result = char + result;
    }

    return result;
};