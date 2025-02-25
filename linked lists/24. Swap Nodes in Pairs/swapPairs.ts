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

function swapPairs(head: ListNode | null): ListNode | null {
    let curr = head;
    let prev = null;

    if (curr && curr.next) {
        head = curr.next;
    }

    while (curr && curr.next) {
        let nxt = curr.next;

        curr.next = nxt.next;
        nxt.next = curr;

        if (prev) {
            prev.next = nxt;
        }

        prev = curr;
        curr = curr.next;
    }

    return head;
};