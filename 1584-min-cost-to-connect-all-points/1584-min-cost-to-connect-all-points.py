class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        dist = 0
        q = [(0,0)]
        n = len(points)
        visited = set()
        
        while q:
            c, x = heapq.heappop(q)
            if x not in visited:
                visited.add(x)
                dist += c
                for i in range(n):
                    if i not in visited:
                        d = abs(points[i][0] - points[x][0]) + abs(points[i][1] - points[x][1])
                        heapq.heappush(q, (d,i))
        
        return dist
        