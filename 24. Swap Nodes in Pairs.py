# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = ListNode(0)
        head3 = head2
        while(head and head.next and head.next is not None):
            l = ListNode(head.val)
            j = ListNode(head.next.val)
            head2.next = j
            head2 = head2.next
            head2.next = l
            head2 = head2.next
            head = head.next.next
        head2.next = head
        return head3.next
        
        