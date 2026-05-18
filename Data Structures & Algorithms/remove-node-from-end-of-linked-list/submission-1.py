# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        rank = length - n
        if rank == 0:
            next = head.next
            head.next = None
            return next
        prev, curr, idx = None, head, 0
        while idx < rank:
            idx += 1
            prev, curr = curr, curr.next
        prev.next = curr.next
        curr.next = None
        return head
