'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        n1 = ''
        while head1:
            n1 += str(head1.val)
            head1 = head1.next
        n1 = int(n1[::-1])

        head2 = l2
        n2 = ''
        while head2:
            n2 += str(head2.val)
            head2 = head2.next
        n2 = int(n2[::-1])

        res = list(str(n1 + n2)[::-1])
        l3 = ListNode()
        head3 = l3
        for el in res:
            head3.next = ListNode(int(el))
            head3 = head3.next

        return l3.next