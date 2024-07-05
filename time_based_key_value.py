from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.timeMap = []
        self.stamps = []
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        insert_position = bisect_left(self.stamps, timestamp)
        self.stamps.insert(insert_position, timestamp)
        self.timeMap.insert(insert_position, [timestamp, key, value])


    def get(self, key: str, timestamp: int) -> str:
        
        def keyFound(index):
            for i in range(index + 1):

                if self.timeMap[i][1] == key:
                    return True
            return False

        res = -1
        l, r = 0, len(self.timeMap) - 1
        while l < r:
            mid = (l + r) // 2
            if timestamp <= self.timeMap[mid][0]:
                r = mid   
            elif keyFound(mid):
                res = max(res, l)
                l = mid + 1
            else:
                print("Here new") 
                r = mid
        
        print(l)
        if self.timeMap[res][1] == key and timestamp >= self.timeMap[res][0]:
            return self.timeMap[res][2]
        else:
            return ""





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# 
tm = TimeMap()
tm.set('love', 'high',10)
tm.set('love', 'low', 20)
# print(tm.get("love", 5))
# print(tm.get('love', 10))
print(tm.get('love', 15))
# print(tm.get('love', 20))
# print(tm.get('love', 25))




# print(tm.timeMap)



# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
