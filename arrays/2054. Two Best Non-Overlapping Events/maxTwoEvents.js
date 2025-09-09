/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    let n = events.length;
    let bestFromHere = new Array(n).fill(0);
    let maxSum = 0;

    events.sort((a, b) => a[0] - b[0]);

    bestFromHere[n - 1] = events[n - 1][2];
    for (let i = n - 2; i >= 0; i--) {
        bestFromHere[i] = Math.max(events[i][2], bestFromHere[i + 1]);
    }

    for (let i = 0; i < n; i++) {
        let currentEventValue = events[i][2]

        let left = i + 1;
        let right = n - 1;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);

            if (events[mid][0] > events[i][1]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        let currentMaxSum = currentEventValue;
        if (left < n) {
            currentMaxSum += bestFromHere[left];
        }

        maxSum = Math.max(maxSum, currentMaxSum);
    }

    return maxSum;
};