/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        return new Promise((resolve, reject) => {
            // Set a timeout to reject if it takes too long
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            // Run the original function
            fn(...args)
                .then((res) => {
                    clearTimeout(timer); // Stop the timeout
                    resolve(res);
                })
                .catch((err) => {
                    clearTimeout(timer);
                    reject(err);
                });
        });
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */