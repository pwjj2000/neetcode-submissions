# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(l1, l2):
            curr, head = None, None
            while l1 and l2:
                if l1.val < l2.val:
                    if curr:
                        curr.next = l1
                        curr = curr.next
                    else:
                        head = curr = l1
                    l1 = l1.next
                else:
                    if curr:
                        curr.next = l2
                        curr = curr.next
                    else:
                        head = curr = l2
                    l2 = l2.next
            if l1:
                if curr:
                    curr.next = l1
                else:
                    head = curr = l1
            if l2:
                if curr:
                    curr.next = l2
                else:
                    head = curr = l2
            return head
        for i in range(1, len(lists)):
            lists[i] = mergeLists(lists[i - 1], lists[i])
        return lists[-1] if len(lists) > 1 else None