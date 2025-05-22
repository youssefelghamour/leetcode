var TimeLimitedCache = function() {
    this.cache = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    /* Returns true when we reset an existing non expired key
       Return false when we add a new key
    */
    const now = Date.now();

    // key exists and not expired
    if (this.cache[key] && this.cache[key].expiry > now) {
        // cancel the old timeout
        clearTimeout(this.cache[key].timeout);

        // reset the key with new inputs
        this.cache[key].value = value;
        this.cache[key].expiry = now + duration;
        this.cache[key].timeout = setTimeout(() => {
            delete this.cache[key];
        }, duration);

        return true;
    }

    // new or expired key
    this.cache[key] = {
        "value": value,
        "expiry": now + duration,
        "timeout": setTimeout(() => {
            delete this.cache[key];
        }, duration)
    };

    return false;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();

    if (this.cache[key] && this.cache[key].expiry > now) return this.cache[key].value;
    
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    return Object.values(this.cache).filter(k => k.expiry > now).length;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */