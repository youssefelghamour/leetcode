/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    /*
        1- We call the debounced function
        2- It waits t milliseconds before running the original function
        3- If we call it again before those t milliseconds are up, it cancels the previous wait and starts waiting again
        4- This means the function only runs after you stop calling it for t ms

        ex: t = 50ms, and the function was called at 30ms, 60ms, and 100ms.
        - first call at 30ms: cancels the old one so we start the timer again of 50ms
            (will execute at: 30ms(passed) + 50ms(new) = 80ms )
        - second call at 60ms: cancels the prev one and we start a new 50ms timer
            (will execute at: 60ms(passed) + 50ms(new) = 110ms )
        - third call at 100ms: cancels the prev one and we start a new 50ms timer
            (will execute at: 100ms(passed) + 50ms(new) = 150ms )
        
            0         30     50  60     80     100  110      150
            |----------|------a---|------b------|--c----------|
                    Call1       Call2         Call3

            a: before the first call at 30ms it was supposed to execute at 50ms
            b: after 1st call 30ms, it was supposed to execute at 80ms
            c: after 2nd call 60ms, it was supposed to execute at 110ms
            last call at 100ms sets it to execute at 150ms
    */
    let timer;

    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */