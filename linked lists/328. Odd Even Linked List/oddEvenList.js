/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if (!head || !head.next) return head;

    let odd = head;
    let even = head.next;
    let evenHead = even;

    let node = even.next;
    let i = 3;

    while (node) {
        if (i % 2 !== 0) {
            odd.next = node;
            odd = odd.next;
        } else {
            even.next = node;
            even = even.next;
        }
        node = node.next;
        i++;
    }

    even.next = null;
    odd.next = evenHead;

    return head;
};