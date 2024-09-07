class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        
        graph = [[] for _ in range(n)]
        visited = set()
        res = set(restricted)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        q = deque([0])
        while q:
            x = q.popleft()
            if x not in visited:
                visited.add(x)
                for i in graph[x]:
                    if i not in visited and i not in res:
                        q.append(i)
        
        return len(visited)
