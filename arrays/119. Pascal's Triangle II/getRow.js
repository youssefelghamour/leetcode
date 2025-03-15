/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generateTriangle = function(numRows) {
    let triangle = [];

    triangle.push([1]);

    for (let i = 1; i <= numRows; i++) {
        let prevRow = triangle[i - 1];
        let currRow = [];

        currRow.push(1);
        for (let j = 1; j < i; j++) {
            currRow.push(prevRow[j - 1] + prevRow[j])
        }
        currRow.push(1);

        triangle.push(currRow);
    }

    return triangle;
};


/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    return generateTriangle(rowIndex)[rowIndex];
};