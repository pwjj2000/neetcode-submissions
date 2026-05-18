# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1, length2, c1, c2 = 0, 0, l1, l2 
        while c1:
            length1 += 1
            c1 = c1.next
        while c2:
            length2 += 1
            c2 = c2.next
        if length1 > length2:
            return self.addTwoNumbers(l2, l1)
        head, carry = l2, 0
        while l2:
            total = carry + l2.val
            if l1:
                total += l1.val
            l2.val = total % 10
            carry = total // 10
            if l1:
                l1 = l1.next
            if l2.next or carry == 0:
                l2 = l2.next
            else:
                l2.next = ListNode(1)
                break
        return head 
