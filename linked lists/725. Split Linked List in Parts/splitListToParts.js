/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    let result = [];
    let curr = head, length = 0;

    while (curr) {
        length++;
        curr = curr.next;
    }

    let subLen = Math.floor(length / k);
    let remainder = length % k;
    curr = head;

    for (let i = 0; i < k; i++) {
        result.push(curr);
        let l = subLen;
        if (remainder > 0) {
            l++;
            remainder--;
        }
        for (let j = 0; j < l - 1; j++) {
            if (curr) curr = curr.next;
        }
        if (curr) {
            let tmp = curr.next;
            curr.next = null;
            curr = tmp;
        }
    }

    return result;
};