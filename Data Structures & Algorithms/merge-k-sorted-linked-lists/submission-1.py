# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        def merge(l1, l2):
            head = curr = None
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        if head:
                            curr.next = l1
                            curr = curr.next
                        else:
                            head = curr = l1
                        l1 = l1.next
                    else:
                        if head:
                            curr.next = l2
                            curr = curr.next
                        else:
                            head = curr = l2
                        l2 = l2.next
                elif l1:
                    if head:
                        curr.next = l1
                        curr = curr.next
                    else:
                        head = curr = l1
                    l1 = l1.next
                else:
                    if head:
                        curr.next = l2
                        curr = curr.next
                    else:
                        head = curr = l2
                    l2 = l2.next
            return head
        for i in range(1, len(lists)):
            lists[i] = merge(lists[i - 1], lists[i])
        return lists[-1]