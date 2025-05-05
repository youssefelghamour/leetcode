/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    const n = cost.length;
    for (let i = 2; i < cost.length; i++) {
        cost[i] += Math.min(cost[i-1], cost[i-2]);
    }
    return Math.min(cost[n-2], cost[n-1]);
};