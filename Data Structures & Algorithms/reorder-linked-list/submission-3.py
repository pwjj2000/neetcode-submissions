# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h1, h2 = head, slow.next
        slow.next = None
        prev = None
        while h2:
            next = h2.next
            h2.next = prev
            prev, h2 = h2, next
        h, curr, h2 = None, None, prev
        while h1 or h2:
            if h1 and h2:
                next1, next2 = h1.next, h2.next
                h1.next = h2
                if h:
                    curr.next = h1
                    curr = curr.next.next
                else:
                    h = curr = h1
                    curr = curr.next
                h1, h2 = next1, next2
            elif h1:
                if h:
                    curr.next = h1
                    curr = curr.next
                else:
                    h = curr = h1
                h1 = h1.next
            else:
                if h:
                    curr.next = h2
                    curr = curr.next
                else:
                    h = curr = h2
                h2 = h2.next