class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(graph)
        ter = list()
        reversed = [[] for _ in range(n)]
        degree = [0] * n
        for i in range(n):
            if (len(graph[i]) == 0):
                ter.append(i)
            for j in graph[i]:
                reversed[j].append(i)
                degree[i] += 1
        
        safe = set(ter)
        q = deque(ter)
        while q:
            x = q.popleft()
            for i in reversed[x]:
                if i not in safe:
                    degree[i] -= 1
                    if degree[i] == 0:
                        q.append(i)
                        safe.add(i)
        
        return sorted(list(safe))
        
            
        