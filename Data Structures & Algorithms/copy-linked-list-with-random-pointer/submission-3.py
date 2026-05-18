"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_copy, curr = {}, head
        while curr:
            if curr not in nodes_copy:
                nodes_copy[curr] = Node(curr.val)
            if curr.next:
                if curr.next not in nodes_copy:
                    nodes_copy[curr.next] = Node(curr.next.val)
                nodes_copy[curr].next = nodes_copy[curr.next]
            if curr.random:
                if curr.random not in nodes_copy:
                    nodes_copy[curr.random] = Node(curr.random.val)
                nodes_copy[curr].random = nodes_copy[curr.random]
            curr = curr.next
        return nodes_copy[head] if head in nodes_copy else None