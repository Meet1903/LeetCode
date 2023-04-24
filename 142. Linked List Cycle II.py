# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headList = []

        head2 = head
        while (head2):
            if head2 in headList:
                return head2
            else:
                headList.append(head2)
            head2 = head2.next

        return None