/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let current = head;
    let values = [];

    while (current) {
      values.push(current.val);
      current = current.next;
    }

    let n = values.length;
    for (let i = 0; i < Math.floor(n / 2); i++) {
      if (values[i] !== values[n - 1 - i]) {
        return false;
      }
    }

    return true;
};