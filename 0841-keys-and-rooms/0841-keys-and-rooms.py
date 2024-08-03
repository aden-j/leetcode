class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        n = len(rooms)
        visited = set()
        visited.add(0)
        q = deque([0])
        
        while q:
            x = q.popleft()
            #visited.add(x)
            for i in rooms[x]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
                    
        return len(visited) == n