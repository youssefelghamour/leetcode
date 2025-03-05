/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let left = new ListNode(), right = new ListNode();
    let lastLeft = left, lastRight = right, curr = head;

    while (curr) {
        if (curr.val < x) {
            lastLeft.next = curr;
            lastLeft = lastLeft.next;
        } else {
            lastRight.next = curr;
            lastRight = lastRight.next;
        }
        curr = curr.next;
    }

    lastRight.next = null;
    lastLeft.next = right.next;
    return left.next;
};