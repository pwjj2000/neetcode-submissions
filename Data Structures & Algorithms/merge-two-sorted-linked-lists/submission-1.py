# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, curr = None, None
        while list1 or list2:
            if (list1 and list2 and list1.val < list2.val):
                if head:
                    curr.next = list1
                    curr = curr.next
                else:
                    head = curr = list1
                list1 = list1.next
            elif (list1 and list2) or list2:
                if head:
                    curr.next = list2
                    curr = curr.next
                else:
                    head = curr = list2
                list2 = list2.next
            else:
                if head:
                    curr.next = list1
                    curr = curr.next
                else:
                    head = curr = list1
                list1 = list1.next
        return head
