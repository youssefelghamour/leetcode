/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    let sums = {};
    let count = 0;

    for (let i = 1; i <= n; i++) {
        let sumDigits = 0;

        for (let digit of String(i)) {
            sumDigits += Number(digit);
        }

        if (sums[sumDigits]) {
            sums[sumDigits].push(i);
        } else {
            sums[sumDigits] = [i];
        }
    }

    let maxSize = Math.max(...Object.values(sums).map(group => group.length));

    for (let group of Object.values(sums)) {
        if (group.length === maxSize) count++;
    }

    return count;
};