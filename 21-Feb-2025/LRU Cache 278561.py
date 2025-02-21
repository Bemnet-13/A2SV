# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.timeMap = {}
        self.first = Cache()
        self.last = Cache()
        self.first.next = self.last
        self.last.prev = self.first
    
    def updateCache(self, key, value):
        lastSeen = Cache(key, value)
        lastSeen.next = self.last
        prevLast = self.last.prev
        self.last.prev = lastSeen
        lastSeen.prev = prevLast
        prevLast.next = lastSeen
        self.timeMap[key] = lastSeen


    def get(self, key: int) -> int:
        # Shift the key to the front
        node = self.timeMap.get(key, None)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.updateCache(node.key, node.value)         
            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.timeMap:
            if self.occupied >= self.capacity:
                evicted = self.first.next
                self.first.next = self.first.next.next
                self.first.next.prev = self.first
                del self.timeMap[evicted.key]
            else:
                self.occupied += 1
        else:
            node = self.timeMap.get(key, None)
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.updateCache(key, value)

        
class Cache:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)