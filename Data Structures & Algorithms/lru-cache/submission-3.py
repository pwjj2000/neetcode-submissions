class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes, self.capacity, self.count = {}, capacity, 0
        self.front, self.rear = Node(-1,-1), Node(-1,-1)
        self.front.next = self.rear
        self.rear.prev = self.front

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        value = node.val
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = self.rear
        node.prev = self.rear.prev
        self.rear.prev.next = node
        self.rear.prev = node
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            prev_node, next_node = node.prev, node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = self.rear
            node.prev = self.rear.prev
            self.rear.prev.next = node
            self.rear.prev = node
        else:
            self.nodes[key] = node = Node(key, value)
            node.next = self.rear
            node.prev = self.rear.prev
            self.rear.prev.next = node
            self.rear.prev = node
            self.count += 1
            if self.count > self.capacity:
                front_node = self.front.next
                self.front.next = front_node.next
                front_node.next.prev = self.front
                del self.nodes[front_node.key]


