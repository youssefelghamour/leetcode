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

function intersection(head: ListNode | null): ListNode | null {
    let fast: ListNode | null = head;
    let slow: ListNode | null = head;

    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next!;
        if (fast === slow) return slow;
    }

    return null;
}

function detectCycle(head: ListNode | null): ListNode | null {
    let start: ListNode | null = head;
    let slow: ListNode | null = intersection(head);

    if (!slow) return null;

    while (start !== slow) {
        start = start!.next;
        slow = slow!.next;
    }

    return start;
};