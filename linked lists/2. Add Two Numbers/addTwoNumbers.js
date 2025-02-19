class ListNode {
    constructor(val = 0, next = null) {
      this.val = val;
      this.next = next;
    }
  }
  
  var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode();
    let current = dummy;
    let carry = 0;
  
    while (l1 || l2 || carry) {
      let sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;
      carry = Math.floor(sum / 10);
      
      current.next = new ListNode(sum % 10);
      current = current.next;
      
      if (l1) l1 = l1.next;
      if (l2) l2 = l2.next;
    }
  
    return dummy.next;
  };  