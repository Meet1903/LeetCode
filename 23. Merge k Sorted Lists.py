# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list2 = []
        for i in lists:
            j = i
            while j is not None:
                list2.append(j.val)
                j = j.next
        list2.sort()
        
        head = ListNode(0)
        head2 = head
        for i in list2:
            l = ListNode(i)
            head.next = l
            head = head.next
        return head2.next
        