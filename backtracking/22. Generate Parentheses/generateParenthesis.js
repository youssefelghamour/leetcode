/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];
    const stack = [];

    function backtrack(open, closed) {
        if (open === n && closed === n) {
            result.push(stack.join(''));
            return;
        }

        if (open < n) {
            stack.push('(');
            backtrack(open + 1, closed);
            stack.pop();
        }

        if (closed < open) {
            stack.push(')');
            backtrack(open, closed + 1);
            stack.pop();
        }
    }

    backtrack(0, 0);

    return result;
};