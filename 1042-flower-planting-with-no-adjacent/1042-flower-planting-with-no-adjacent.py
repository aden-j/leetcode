class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(n+1)]
        
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        result = [-1] * n
        def dfs(start):
            color_set = set()
            for x in graph[start]:
                if result[x-1] != -1:
                    color_set.add(result[x-1])
            
            for c in range(1,5):
                if c not in color_set:
                    result[start -1] = c
                    break
                    
            for x in graph[start]:
                if result[x-1] == -1:
                    dfs(x)
            
        
        for i in range(n):
            index = i+1
            if result[i] == -1:
                dfs(index)
                
        return result
        