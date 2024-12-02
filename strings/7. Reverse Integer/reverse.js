/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    is_negative = x < 0;
    num = [...Math.abs(x).toString()];
    
    for (let i = 0; i < num.length / 2; i++) {
        temp = num[i];
        num[i] = num[num.length - 1 - i];
        num[num.length - 1 - i] = temp;
    }
    
    result = parseInt(num.join(""));
    
    if (result > Math.pow(2, 31) - 1 || result < -Math.pow(2, 31)) {
        return 0;
    }
    
    return is_negative ? -result : result;
};