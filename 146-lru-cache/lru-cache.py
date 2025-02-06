class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.prev = None
        self.tail.next = None
        self.head.next = self.tail
        self.tail.prev = self.head
        return None

    def delete(self, node: Node):
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            return self.cache[key].data
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
            node = self.cache[key] if key in self.cache else Node(key,value)
            node.data = value
            if key in self.cache:
                self.delete(node)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            self.cache[key] =node
            if len(self.cache) > self.capacity:
                lastNode = self.tail.prev
                self.delete(lastNode)
                if lastNode.key in self.cache:
                    del self.cache[lastNode.key]
            return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)