class EventEmitter {
    events = {};  // {'eventName1': [callback1, callback2, ... ]}
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        // handle the event:callbacks key value pair in events
        if (eventName in this.events) this.events[eventName].push(callback);
        else this.events[eventName] = [callback];

        return {
            unsubscribe: () => {
                // get the index of the callback from the value of the eventName key
                let index = this.events[eventName].indexOf(callback);
                // remove the callback from the list of callbacks
                if (index !== -1) this.events[eventName].splice(index, 1);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let result = [];
        // there is no event in events with this name
        if (!this.events[eventName]) return result;
        // execute each callback with the arguments spread, and add the result to results
        for (let cb of this.events[eventName]) result.push(cb(...args));
        return result;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */