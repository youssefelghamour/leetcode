/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = [];
        let count = 0;

        if (functions.length === 0) {
            resolve(results);
        }

        for (let i = 0; i < functions.length; i++) {
            functions[i]()
                .then(res => {
                    results[i] = res;
                    count++;
                    // make sure to resolve when we all promises in functions resolved
                    if (count === functions.length) resolve(results);
                })
                .catch(reject);
        }
    })
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */