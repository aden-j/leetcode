class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        
        dist = [[float('inf')] * n for _ in range(n)]
        
        for f, t, w in edges:
            dist[f][t] = w
            dist[t][f] = w
            
        for i in range(n):
            dist[i][i] = 0
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
            
        least = n
        greatest = 0 
        for i in range(n):
            count = sum(dist[i][j] <= distanceThreshold for j in range(n))
            if (count <= least):
                least = count 
                greatest = i
                
        return greatest