# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        total = 0
        while(head2):
            total += 1
            head2 = head2.next
        if (total % 2 == 0):
            total = total/2
        else:
            total = (total - 1)/2
        for i in range(int(total)):
            head = head.next
        
        return head