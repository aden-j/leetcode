class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(n)]
        deg = [0] * n
        for f, t in edges:
            graph[f].append(t)
            deg[t] += 1
            
        result = [i for i in range(n) if deg[i] == 0]

                    
        return result