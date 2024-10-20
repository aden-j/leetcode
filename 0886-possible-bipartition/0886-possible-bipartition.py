class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        graph = [[] for _ in range(n+1)]
        
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
            
        node = [-1] * (n+1)
            
        def dfs(start, color):
            node[start] = color
            for x in graph[start]:
                if node[x] == -1:
                    if not dfs(x, 1-color):
                        return False
                elif node[x] != (1-color):
                    return False
            return True
        
        for i in range(1,n+1):
            if node[i] == -1:
                if not dfs(i, 0):
                    return False
        return True