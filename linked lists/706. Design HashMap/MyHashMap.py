# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyHashMap(object):
    """ Uses a linked list to make a hash map with node values being a list [key, value] """

    def __init__(self):
        self.head = None
        self.tail = None
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = ListNode([key, value])

        if self.get(key) != -1:
            # If the key already exists, update its value
            current = self.head
            while current:
                if current.val[0] == key:
                    current.val[1] = value
                    return
                current = current.next

        if self.head is None:
            # Add the first node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Add to the end
            self.tail = new_node  # Update the tail
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        current = self.head
        while current:
            if current.val[0] == key:
                return current.val[1]
            current = current.next
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        current = self.head
        prev = None

        if current and current.val[0] == key:
            # If the head is the key
            self.head = current.next
            if self.head is None:
                # Update tail if list becomes empty
                self.tail = None
            return

        while current:
            if current.val[0] == key:
                prev.next = current.next
                if prev.next is None:
                    # Update tail if we removed the last node
                    self.tail = prev
                return
            prev = current
            current = current.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)