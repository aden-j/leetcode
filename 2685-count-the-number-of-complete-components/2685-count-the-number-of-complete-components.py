class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        visited = set()
        
        result = 0
        
        for i in range(n):
            if i not in visited:
                q = deque([i])
                group = []
                while q:
                    x = q.popleft()
                    if x not in visited:
                        group.append(x)
                        visited.add(x)
                        for node in graph[x]:
                            if node not in visited:
                                q.append(node)
                                
                sum = 0
                k = len(group)
                for j in group:
                    sum += len(graph[j])
                    
                if sum == k * (k-1):
                    result += 1
                    
        return result
                        
        