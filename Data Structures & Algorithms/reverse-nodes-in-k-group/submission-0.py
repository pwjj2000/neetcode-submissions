# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        rev_times = length // k
        
        prev_first_of_k, curr = head, head
        # for _ in range(k):
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        for i in range(rev_times):
            p, prev = curr, None
            for j in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            if i > 0:
                prev_first_of_k.next = prev
                prev_first_of_k = p
            else:
                head = prev
        if length % k != 0:
            prev_first_of_k.next = curr
        return head