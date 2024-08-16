class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        deg = [0] * n
        for f, t in edges:
            deg[t] += 1
            
        result = [i for i in range(n) if deg[i] == 0]

                    
        return result