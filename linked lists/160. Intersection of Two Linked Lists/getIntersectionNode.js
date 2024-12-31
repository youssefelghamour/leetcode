/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    let node = headA;
    let lstA = [];
    while (node) {
        lstA.push(node);
        node = node.next;
    }

    node = headB;
    let lstB = [];
    while (node) {
        lstB.push(node);
        node = node.next;
    }

    const lenA = lstA.length;
    const lenB = lstB.length;

    const diff = Math.abs(lenA - lenB);

    if (lenA > lenB) {
        lstA.splice(0, diff);
    } else {
        lstB.splice(0, diff);
    }

    for (let i = 0; i < Math.min(lenA, lenB); i++) {
        if (lstA[i] == lstB[i]) {
            return lstA[i];
        }
    }

    return null;
};