class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = Node(-1, -1)
        self.end = Node(-1, -1)
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next 
            node.next.prev = node.prev

            node.next = self.end
            node.prev = self.end.prev
            self.end.prev = node
            node.prev.next = node
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            node.prev.next = node.next 
            node.next.prev = node.prev

            node.next = self.end
            node.prev = self.end.prev
            self.end.prev = node
            node.prev.next = node
        elif len(self.cache) < self.capacity:
            self.cache[key] = Node(key, value)
            prev_last = self.end.prev
            self.end.prev = self.cache[key]
            prev_last.next = self.cache[key]
            self.cache[key].next = self.end
            self.cache[key].prev = prev_last
        else:
            first = self.start.next
            self.start.next = first.next
            first.next.prev = self.start
            first.next = first.prev = None
            del self.cache[first.key]
            self.cache[key] = Node(key, value)
            prev_last = self.end.prev
            self.end.prev = self.cache[key]
            prev_last.next = self.cache[key]
            self.cache[key].next = self.end
            self.cache[key].prev = prev_last
