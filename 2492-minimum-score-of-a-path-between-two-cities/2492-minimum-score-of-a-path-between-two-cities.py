class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        graph = [[] for _ in range(n+1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        # BFS로 최소 경로 점수 탐색
        result = float('inf')
        visited = set([1])
        q = deque([1])

        while q:
            x = q.popleft()
            for node, d in graph[x]:
                result = min(result, d)
                if node not in visited:
                    visited.add(node)
                    q.append(node)

        return result
        