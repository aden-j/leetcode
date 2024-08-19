class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        inf = float('inf')
        
        distn = [inf] * (n+1)
        graph = [[] for _ in range(n+1)]
        distn[n] = 0
        for x,y,d in edges:
            graph[x].append((y,d))
            graph[y].append((x,d))
        
        visited = set()
        q = [(0, n)]
        while q:
            d, x = heapq.heappop(q)
            if x not in visited:
                visited.add(x)
                distn[x] = d
                for y, k in graph[x]:
                    if y not in visited:
                        heapq.heappush(q, (d+k, y))
        
        
        dp = [-1] * (n+1)
        def dfs(start, graph, distn, dp):
            if start == n:
                return 1
            if dp[start] != -1:
                return dp[start]
            
            count = 0
            for x, k in graph[start]:
                if distn[x] < distn[start]:
                    count += dfs(x, graph, distn, dp)
                    count %= 10**9 + 7
            
            dp[start] = count
            return count
        
        return dfs(1, graph, distn, dp)