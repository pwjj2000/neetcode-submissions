# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = None
        carry = 0
        while l1 or l2:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            total = v1 + v2 + carry
            digit, carry = total % 10, total // 10
            if head:
                curr.next = ListNode(digit)
                curr = curr.next
            else:
                head = curr = ListNode(digit)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry:
            curr.next = ListNode(carry)
        return head