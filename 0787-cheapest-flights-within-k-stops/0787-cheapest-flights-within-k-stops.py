import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        inf = float('inf')
        dist = [[] for _ in range(n)]
        visited = {}
        
        for u,v,w in flights:
            dist[u].append((v,w))
            
        heap = [(0,src,0)]
        
        while heap:
            d,x,f = heapq.heappop(heap)
            if x == dst:
                return d
            if f <= k:
                for v,w in dist[x]:
                    if (v, f) not in visited or d+w < visited[(v, f)]:
                        visited[(v, f)] = d+w
                        heapq.heappush(heap, (d + w, v, f+1))
                    
                        
        return -1