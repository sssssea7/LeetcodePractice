# https://leetcode.com/problems/lru-cache/description/
# doubly-linked list + hashmap

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {} # key to node
        self.left = Node() # left most dummy
        self.right = Node() # right most dummy
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_mru(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]

        self.remove(node)
        self.add_mru(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.remove(node)
            self.add_mru(node)
            return 

        node = Node(key, value)
        self.nodes[key] = node
        self.add_mru(node)

        if len(self.nodes)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.nodes[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)