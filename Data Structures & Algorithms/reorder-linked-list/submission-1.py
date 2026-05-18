# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1, l2 = head, slow.next
        slow.next = None
        prev, curr = None, l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr, l2 = None, prev
        h = None
        while l2:
            n1, n2 = l1, l2
            l1 = l1.next
            l2 = l2.next
            n1.next = n2
            if curr:
                curr.next = n1
                curr = curr.next.next
            else:
                head = n1
                curr = n1
                curr = curr.next
        if l1 and curr:
            curr.next = l1
        return h