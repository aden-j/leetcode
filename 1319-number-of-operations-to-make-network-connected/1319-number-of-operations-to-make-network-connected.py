class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        if len(connections) < n-1:
            return -1
        
        graph = [[] for _ in range(n)]
        for con in connections:
            graph[con[0]].append(con[1])
            graph[con[1]].append(con[0])
        
        visited = set()
        count = 0
        
        # def visit(start):
        #     q = deque([start])
        #     while q:
        #         x = q.popleft()
        #         visited.add(x)
        #         for i in graph[x]:
        #             if i not in visited:
        #                 q.append(i)
                        
        def dfs(start):
            s = [start]
            while s:
                x = s.pop()
                visited.add(x)
                for i in graph[x]:
                    if i not in visited:
                        s.append(i)
                    
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count - 1
    
    