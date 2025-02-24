/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeElements(head: ListNode | null, val: number): ListNode | null {
    let curr = head;

    while (head && head.val === val) {
        head = head.next ? head.next : null;
        curr = head;
    }  

    while (curr && curr.next) {
        if (curr.next.val == val) {
            curr.next = curr.next.next ? curr.next.next : null;
        } else {
            curr = curr.next;
        }
    }

    return head;
};