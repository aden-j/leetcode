class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(n)]
        for i,j,d in edges:
            graph[i].append((j,d))
            graph[j].append((i,d))
        
        result = [-1] * n
        result[0] = 0
        visited = set()
        
        q = [(0,0)]
        
        while q:
            d, x = heapq.heappop(q)
            if d < disappear[x] and x not in visited:
                visited.add(x)
                result[x] = d 
                for y, dist in graph[x]:
                    if y not in visited:
                        heapq.heappush(q, (d+dist, y))
                        
        return result