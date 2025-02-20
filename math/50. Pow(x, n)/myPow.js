class Solution {
    myPow(x, n) {
        function pow(x, n) {
            if (x === 0) return 0;
            if (n === 0) return 1;
            
            let res = pow(x, Math.floor(n / 2));
            res *= res;
            
            return n % 2 !== 0 ? x * res : res;
        }
        
        return n >= 0 ? pow(x, n) : 1 / pow(x, Math.abs(n));
    }
}
