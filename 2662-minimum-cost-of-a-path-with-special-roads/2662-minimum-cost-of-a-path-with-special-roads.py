class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        
        q = [(0, start[0], start[1])]
        visited = set()
        
        while q:
            d,x,y = heapq.heappop(q)
            
            if x == target[0] and y == target[1]:
                return d
            
            if (x,y) not in visited:
                visited.add((x,y))
                
                dist = d + abs(target[0] - x) + abs(target[1] - y)
                heapq.heappush(q, (dist, target[0], target[1]))
                
                for x1, y1, x2, y2, cost in specialRoads:
                    dist = d + abs(x1-x) + abs(y1-y) + cost
                    heapq.heappush(q, (dist, x2, y2))
                                      
        