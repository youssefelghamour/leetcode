var mySqrt = function(x) {
    let l = 0, r = x;

    while (l <= r) {
        let mid = Math.floor((l + r) / 2);

        if (mid * mid > x) {
            r = mid - 1;
        } else if (mid * mid < x) {
            l = mid + 1;
        } else {
            return mid;
        }
    }

    return r; // The rounded-down number (r < l, and r^2 <= x)
};
