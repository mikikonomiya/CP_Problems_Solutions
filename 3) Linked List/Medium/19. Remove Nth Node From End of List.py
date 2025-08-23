'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        if n == 1:
            if not head.next:
                head = None
                return head
            while current.next.next != None:
                current = current.next
            current.next = None
            return head
        current = head
        length = 0
        while current != None:
            current = current.next
            length += 1
        rev_n = length - n 
        current = head
        while rev_n != 0:
            current = current.next
            rev_n -= 1
        current.val = current.next.val
        current.next = current.next.next
        return head