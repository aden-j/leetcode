class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
        graph = [[] for _ in range(n)]

        for i,j in edges:
            graph[j].append(i)

        ancestor = [set() for _ in range(n)]
        visited = [False] * n

        def dfs(start):
            if visited[start]:
                return ancestor[start]
            for x in graph[start]:
                ret = dfs(x)
                ancestor[start].add(x)
                ancestor[start].update(ret)

            visited[start] = True
            return ancestor[start]

        for i in range(n):
            dfs(i)

        return [sorted(list(x)) for x in ancestor]