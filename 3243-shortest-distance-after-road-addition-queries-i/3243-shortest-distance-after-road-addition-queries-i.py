class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        dist = [n-1-i for i in range(n)]
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i+1)
        result = []
        
        for x,y in queries:
            graph[x].append(y)
            dist[x] = min(dist[x], dist[y] + 1)
            for i in range(x-1, -1, -1):
                for j in graph[i]:
                    dist[i] = min(dist[i],dist[j]+1)
            result.append(dist[0])
        
        return result
                
        