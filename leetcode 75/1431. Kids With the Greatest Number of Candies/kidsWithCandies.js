/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let maxVal = Math.max(...candies);
    let result = [];

    for (let i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= maxVal) result.push(true);
        else result.push(false);
    }

    return result;
};