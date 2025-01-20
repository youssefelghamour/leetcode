/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n <= 2) {
        return 0;
    }

    // 1: prime, 0: not prime
    let primes = new Array(n).fill(1);
    primes[0] = primes[1] = 0;

    for (let i = 2; i <= n ** 0.5; i++) {
        if (primes[i] === 1) {
            for (let j = i * i; j < n; j += i) {
                primes[j] = 0;
            }
        }
    }

    return primes.filter(x => x === 1).length;
}; 