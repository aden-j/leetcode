class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph = [[] for _ in range(n)]
        for i,j in edges:
            graph[j].append(i)
            
        result = -1
        for i in range(n):
            if len(graph[i]) == 0:
                if result == -1:
                    result = i
                else:
                    return -1
                
        return result