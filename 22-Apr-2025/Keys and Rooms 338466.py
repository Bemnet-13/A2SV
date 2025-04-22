# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked = 1

        queue = deque([0])
        visited = [False for _ in range(len(rooms))]
        visited[0] = True

        while queue:
            room = queue.popleft()
            for k in rooms[room]:
                if not visited[k]:
                    queue.append(k)
                    visited[k] = True
                    unlocked += 1
        
        return unlocked == len(rooms)

