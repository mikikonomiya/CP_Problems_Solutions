'''
You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now slow splits the LL in 2 halves
        head2 = slow.next
        prev = slow.next = None
        # reverse the second half
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        head2 = prev
        while head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head2 = temp2
            head = temp1
