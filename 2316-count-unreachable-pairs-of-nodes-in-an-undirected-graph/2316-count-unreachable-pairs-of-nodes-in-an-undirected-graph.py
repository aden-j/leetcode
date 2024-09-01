class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        groups = []
        graph = [[] for _ in range(n)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        for i in range(n):
            if i not in visited:
                count = 0
                q = deque([i])
                while q:
                    x = q.popleft()
                    if x not in visited:
                        visited.add(x)
                        count += 1
                        for k in graph[x]:
                            if k not in visited:
                                q.append(k)
                            
                groups.append(count)
                
        result = n * (n - 1) / 2
        for i in groups:
            print(i)
            result -= (i * (i-1) / 2)
                
        return result      
            
        