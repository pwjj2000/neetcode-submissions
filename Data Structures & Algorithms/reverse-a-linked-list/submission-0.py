# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next
        for i in reversed(range(1, len(arr))):
            arr[i].next = arr[i - 1]
        arr[0].next = None
        return arr[-1]
        