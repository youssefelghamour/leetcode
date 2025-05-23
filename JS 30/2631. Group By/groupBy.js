/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let result = {};

    for (let i = 0; i < this.length; i++) {
        let key = fn(this[i]);

        if (key in result) result[key].push(this[i]);
        else result[key] = [this[i]];
    }

    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */