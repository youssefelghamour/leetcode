class Solution:
    def countPrimes(self, n: int) -> int:
        """ Uses the Sieve of Eratosthenes to count prime numbers up to n """
        if n <= 2:
            return 0
        
        # Initialize a list to track prime numbers: primes[i] = True if i is prime
        primes = [True] * n
        # 0 and 1 are not prime
        primes[0] = primes[1] = False
        
        # n = x*y, where x < sqrt(n) < y < n. If x divides n, then y divides n (all all divisor pairs like (x,y) are symmetric around the sqrt)
        # That's why, we only check up to sqrt(n) because divisors above it are already paired with those below
        for i in range(2, int(n ** 0.5) + 1):
            # if i is prime
            if primes[i]:
                # Iterate over all multiples of i less than n
                for j in range(i * i, n, i):
                    # Mark multiples of i as not prime, because any mutiple of a prime is not prime (the prime divides it)
                    primes[j] = False
        
        return sum(primes)